from flask import Flask, url_for, redirect, render_template, Response, render_template_string
import os
from flask_sqlalchemy import SQLAlchemy
from db import db
from os import path
from db.models import users
from flask_login import LoginManager
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9

app = Flask(__name__)

# Инициализация Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_users(login_Id):
    return users.query.get(int(login_Id))

# Конфигурация приложения
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')
app.config['UPLOAD_FOLDER'] = path.join('static', 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Настройка базы данных
if app.config['DB_TYPE'] == 'postgres':
    db_name = 'orlov_andrey_orm'
    db_user = 'orlov_andrey_orm'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "orlov_andrey_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

# Инициализация базы данных
db.init_app(app)

# Регистрация Blueprint'ов
blueprints = [lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9]
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# Общие функции
def get_css_path():
    return url_for("static", filename="styles.css")

# Маршруты
@app.route("/")
def slesh():
    return redirect('/menu', code=302)

@app.route("/index")
def index():
    return redirect('/lab1/menu', code=302)

@app.errorhandler(404)
def not_found(err):
    return render_template("404.html"), 404

@app.route("/menu")
def menu():
    css_path = get_css_path()
    return f'''
<!DOCTYPE html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" type="text/css" href="{css_path}">       
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <ol>
            <li><a href="/lab1">1 лаба</a></li>
            <li><a href="/lab2">2 лаба</a></li>
            <li><a href="/lab3">3 лаба</a></li>
            <li><a href="/lab4">4 лаба</a></li>
            <li><a href="/lab5">5 лаба</a></li>
            <li><a href="/lab6">6 лаба</a></li>
            <li><a href="/lab7">7 лаба</a></li>
            <li><a href="/lab8">8 лаба</a></li>
            <li><a href="/lab9">9 лаба</a></li>
        </ol>
        <footer>
            &copy; Ефимкина Софья, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>'''

# Обработчики ошибок
@app.route('/400')
def error_400():
    return Response('Неверный запрос', status=400)

@app.route('/401')
def error_401():
    return Response('Неавторизованный доступ', status=401)

@app.route('/402')
def error_402():
    return Response('Необходима оплата', status=402)

@app.route('/403')
def error_403():
    return Response('Доступ запрещён', status=403)

@app.route('/405')
def error_405():
    return Response('Метод не разрешён', status=405)

@app.route('/418')
def error_418():
    return Response('Я чайник', status=418)

@app.route('/error')
def trigger_error():
    result = 1 / 0
    return str(result)

@app.errorhandler(500)
def internal_server_error(err):
    return render_template('500.html'), 500

# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)