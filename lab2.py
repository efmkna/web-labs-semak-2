from flask import Blueprint, url_for, redirect, render_template, Response, render_template_string, request

lab2 = Blueprint('lab2', __name__)

# Общая функция для получения пути к CSS
def get_css_path():
    return url_for("static", filename="styles.css")

# Маршруты для тестирования слэшей
@lab2.route('/lab2/a')
def a():
    return 'без слэша'

@lab2.route('/lab2/a/')
def a1():
    return 'со слешем'

# Пример страницы с передачей данных
@lab2.route('/lab2/example')
def example():
    name, number, groupe, course = 'Ефимкина Софья', 2, 'ФБИ-24', '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321},
    ]
    return render_template('lab2/example.html', name=name, number=number, groupe=groupe, course=course, fruits=fruits)

# Главная страница лабораторной работы
@lab2.route('/lab2/')
def lab():
    return render_template('lab2/lab2.html')

# Страница с примерами фильтров
@lab2.route('/lab2/filters/')
def filters():
    phrase = '0 <b>сколько</b> <u>нам</u> <i>открытий</i> чудных... '
    return render_template('lab2/filters.html', phrase=phrase)

# Калькулятор
@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return render_template('lab2/calc.html', first=a, second=b)

@lab2.route('/lab2/calc/')
def redcalc():
    return redirect("/lab2/calc/1/1")

@lab2.route('/lab2/calc/<int:a>')
def redcalccc(a):
    return redirect(f"/lab2/calc/{a}/1")

# Список книг
books = [
    {"title": "Человек в поисках смысла", "author": "Виктор Франкл", "genre": "Психология", "pages": 224},
    {"title": "Психология влияния", "author": "Роберт Чалдини", "genre": "Социальная психология", "pages": 384},
    {"title": "Думай медленно... решай быстро", "author": "Даниэль Канеман", "genre": "Когнитивная психология", "pages": 704},
    {"title": "Игры, в которые играют люди", "author": "Эрик Берн", "genre": "Психология", "pages": 544},
    {"title": "Эмоциональный интеллект", "author": "Дэниел Гоулман", "genre": "Психология", "pages": 496},
    {"title": "Тревожные люди", "author": "Фредрик Бакман", "genre": "Социальная психология", "pages": 416},
    {"title": "Сила привычки", "author": "Чарльз Дахигг", "genre": "Психология", "pages": 432},
    {"title": "Самообман", "author": "Эдгар Шейн", "genre": "Психология личности", "pages": 320},
    {"title": "Психология зависимости", "author": "Говард Шаффер", "genre": "Психология", "pages": 384},
    {"title": "Мозг и душа", "author": "Валерий Суворов", "genre": "Нейропсихология", "pages": 256}
]

@lab2.route('/lab2/books/')
def book_list():
    return render_template('lab2/books.html', books=books)

# Список ягод
berries = [
    {"name": "Клубника", "description": "Сладкая и сочная летняя ягода.", "image": "/static/lab2/k.webp"},
    {"name": "Малина", "description": "Ягода с нежным ароматом и вкусом.", "image": "/static/lab2/ma.webp"},
    {"name": "Голубика", "description": "Темная ягода с насыщенным вкусом.", "image": "/static/lab2/g.jpg"},
    {"name": "Ежевика", "description": "Ягода с насыщенным сладким вкусом.", "image": "/static/lab2/e.webp"},
    {"name": "Морошка", "description": "Ягода с кисловатым вкусом", "image": "/static/lab2/mo.webp"}
]

@lab2.route('/lab2/berries/')
def show_berries():
    return render_template('lab2/berries.html', berries=berries)

# Список цветов
flower_list = [
    {'name': 'роза', 'price': 300},
    {'name': 'тюльпан', 'price': 310},
    {'name': 'незабудка', 'price': 320},
    {'name': 'ромашка', 'price': 300},
    {'name': 'георгин', 'price': 300},
    {'name': 'гладиолус', 'price': 310}
]

# Отображение списка цветов
@lab2.route('/lab2/flowers/')
def list_flowers():
    return render_template('lab2/flower_list.html', flowers=flower_list)

# Добавление нового цветка
@lab2.route('/lab2/add_flower/', methods=['GET'])
def add_flower():
    name = request.args.get('name')
    price = request.args.get('price')
    if name and price:
        flower_list.append({'name': name, 'price': int(price)})
    return redirect(url_for('lab2.list_flowers'))

# Удаление цветка
@lab2.route('/lab2/del_flower/<int:flower_id>')
def delete_flower(flower_id):
    if 0 <= flower_id < len(flower_list):
        del flower_list[flower_id]
        return redirect(url_for('lab2.list_flowers'))
    return render_template("404.html"), 404

# Очистка всех цветов
@lab2.route('/lab2/clear_flowers/')
def clear_flowers():
    flower_list.clear()
    return redirect(url_for('lab2.list_flowers'))
