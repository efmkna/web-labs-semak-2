from flask import Blueprint, url_for, redirect, Response, render_template_string

lab1 = Blueprint('lab1', __name__)

# Общая функция для получения пути к CSS
def get_css_path():
    return url_for("static", filename="lab1/lab1.css")

# Главная страница лабораторной работы
@lab1.route('/lab1')
def lab():
    css_path = get_css_path()
    return f'''
<!doctype html>
<html>
    <head>
        <title>Ефимкина Софья Алексеевна, Лабораторная 1</title>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <header>
            Лабораторная работа 1
        </header>
        <h1>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности. <br>        
            <a href="/">Меню</a>
        </h1>
        <h2>Реализованные роуты</h2>
        <div>
            <ol>
                <li><a href="/lab1/oak">Дуб</a></li>
                <li><a href="/lab1/web">веб-сервер на фласк</a></li>
                <li><a href="/lab1/author">студент-группа - факультет</a></li>
                <li><a href="/lab1/counter">Счетчик</a></li>
                <li><a href="/lab1/created">201 код</a></li>
                <li><a href="404"> ошибка 404</a></li>
                <li><a href="400">Ошибка 400</a></li>
                <li><a href="401">Ошибка 401</a></li>
                <li><a href="402">Ошибка 402</a></li>
                <li><a href="403">Ошибка 403</a></li>
                <li><a href="405">Ошибка 405</a></li>
                <li><a href="418">Ошибка 418</a></li>
                <li><a href="/about"> заголовки</a></li>
                <li><a href="/error">ошибка 500</a></li>
                <li><a href="/lab1/web1"> веб-сервер на flask</a></li>
            </ol>
        </div>
        <footer>
            &copy; Ефимкина Софья, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

# Страница "web"
@lab1.route("/lab1/web")
def web():
    css_path = get_css_path()
    return f'''<!doctype html> 
<html> 
    <head>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body> 
        <h1>web-сервер на flask</h1> 
        <a href="/lab1/author">author</a>
    </body> 
</html>'''

# Страница "author"
@lab1.route("/lab1/author")
def author():
    css_path = get_css_path()
    name = "Ефимкина Софья Алексеевна"
    group = "ФБИ-24"
    faculty = "FB"
    return f'''<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <p>Студент: {name}</p>
        <p>Группа: {group}</p>
        <p>Факультет: {faculty}</p>
        <a href="/lab1/web">web</a>
    </body>
</html>'''

# Страница "oak"
@lab1.route('/lab1/oak')
def oak():
    css_path = get_css_path()
    path = url_for("static", filename="lab1/oak.jpg")
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="{path}">
    </body>
</html>'''

# Счетчик
count = 0

@lab1.route('/lab1/counter')
def counter():
    css_path = get_css_path()
    global count
    count += 1
    reset_url = url_for('lab1.reset_counter')
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        Сколько раз вы сюда заходили: {count}
        <a href="{reset_url}">Сбросить счётчик</a>
    </body>
</html>'''

@lab1.route('/lab1/reset_counter')
def reset_counter():
    css_path = get_css_path()
    global count
    count = 0
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <p>Счётчик сброшен!</p>
        <a href="/lab1/counter">Вернуться к счётчику</a>
    </body>
</html>'''

# Перенаправление на страницу "author"
@lab1.route("/lab1/info")
def info():
    return redirect("/lab1/author")

# Страница "created"
@lab1.route("/lab1/created")
def created():
    css_path = get_css_path()
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
    </body>
</html>
''', 201

# Страница "about"
@lab1.route('/lab1/about')
def about():
    css_path = get_css_path()
    path = url_for("static", filename="lab1/river.jpg")
    html_content = f'''
<!doctype html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Осень</title>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <h1>Река</h1>
        <p>
            В далекой уютной деревне, среди заливных полей и высоких холмов, тянется одна из красивейших рек. 
            Ее прозрачная вода и благоухающие берега притягивают к себе множество путешественников и любителей природы. Здесь, где время замирает, 
            каждый камень и каждое дерево имеют свою историю, свою тайну, которые манят гостей раскрывать незабываемые загадки природы.
        </p>
        <p>
            В этих краях ты находишься в полном единении с природой. Шум воды, пение птиц и шелест листвы наполняют сердце и дарят умиротворение. Здесь можно встретить оленей и зайцев, которые бесстрашно прогуливаются 
            по полям и лесам. Каждый шаг вдоль реки открывает все новые и новые красоты, заставляя погрузиться в завораживающую симфонию природы.
        </p>
        <p>
            В моменты, когда солнце падает за горизонт, а небосвод окрашивается в огненные оттенки, река приобретает особую магию. 
            Ее рассветы и закаты — подарок для каждого, кто позволяет себе остановиться и насладиться этой красотой. 
            Здесь, среди деревьев и воды, ты найдешь покой и вдохновение, открывая новые грани своего внутреннего мира.
        </p>
        <img src="{path}">
    </body>
</html>'''

    response = Response(render_template_string(html_content))
    response.headers['Content-Language'] = 'ru'
    response.headers['Content-Type'] = 'text/html'
    response.headers['Content-Length'] = response.calculate_content_length()
    return response