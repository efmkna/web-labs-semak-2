from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<html>
    <head>
        <title>Ефимкина Софья Алексеевна, лаба 1</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, первая лаба
        </header>

        <h1>содержимое первой лабы</h1>
        <p>Flask — это микрофреймворк для веб-разработки на языке Python. 
        Он позволяет создавать веб-приложения быстро и легко.
        Подробнее в <a href="/menu">меню</a>.</p>

        <h2>реализованные роуты</h2>
        <ul>
            <li><a href="/lab1/student">студент</a></li>
            <li><a href="/lab1/python">питон</a></li>
            <li><a href="/lab1/oak">дуб</a></li>
        </ul>

        <footer>
            &copy; Ефимкина Софья, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/menu")
def menu():
     return '''
<!doctype html>
<html>
    <head>
        <title>Ефимкина Софья Алексеевна, лаба 1</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, лаба 1
        </header>
        
        <h1>web-сервер на Flask</h1>

        <ul>
            <li><a href="/lab1">первая лаба</a></li>
        </ul>

        <footer>
            &copy; Ефимкина Софья, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1/oak")
def oak(): 
    return'''
<!doctype html>
<html>
    <head>
        <title>Ефимкина Софья Алексеевна, лаба 1</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
        <footer>
            &copy; Ефимкина Софья, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Студент</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, лаба 1
        </header>

        <h1>Студент</h1>
        <p>Ефимкина Софья Алексеевна, ФБИ-24, 3 курс, 2024</p>
        <img src="''' + url_for('static', filename='nstu.png') + '''">

        <footer>
            &copy; Ефимкина Софья, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1/python")
def python():
    return '''
<!doctype html>
<html>
    <head>
        <title>Python</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, лаба 1
        </header>

        <h1>Python</h1>
        <p>Python — это высокоуровневый язык программирования общего назначения, который широко используется в различных областях, включая веб-разработку, научные вычисления, анализ данных и многое другое.</p>
        <img src="''' + url_for('static', filename='python.png') + '''">
        
        <footer>
            &copy; Ефимкина Софья, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''