from flask import Flask
app = Flask(__name__)

@app.route("/")
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

        <footer>
            &copy; Ефимкина Софья, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""