from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return """
<!doctype html>
<html>
    <head>
        <title>Ефимкина Софья Алексеевна, лаба 1</title>
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
"""

@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>первая лаба</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, первая лаба
        </header>

        <h1>Содержимое первой лабораторной</h1>

        <footer>
            &copy; Ефимкина Софья, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""

