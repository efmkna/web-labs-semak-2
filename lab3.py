from flask import Blueprint, render_template, request, make_response, redirect

lab3 = Blueprint('lab3', __name__)

# Главная страница лабораторной работы
@lab3.route('/lab3')
def lab():
    # Получаем данные из cookies или используем значения по умолчанию
    name = request.cookies.get('name', 'аноним клиент')
    name_color = request.cookies.get('name_color', 'green')
    age = request.cookies.get('age', 'не указан')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)

# Установка cookies
@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3'))
    resp.set_cookie('name', 'alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp

# Удаление cookies
@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp

# Форма 1 с валидацией
@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Введите возраст!'
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)

# Страница заказа
@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')

# Расчет стоимости заказа
@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('lab3/pay.html', price=price)

# Страница успешного завершения
@lab3.route('/lab3/success')
def success():
    return render_template('lab3/success.html')

# Настройки (цвет, фон, размер шрифта)
@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    background_color = request.args.get('background_color')
    font_size = request.args.get('font_size')
    reset = request.args.get('reset')

    # Сброс настроек
    if reset:
        resp = make_response(redirect('/lab3/settings'))
        resp.delete_cookie('color')
        resp.delete_cookie('background_color')
        resp.delete_cookie('font_size')
        return resp

    # Установка новых настроек
    if color or background_color or font_size:
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if background_color:
            resp.set_cookie('background_color', background_color)
        if font_size:
            resp.set_cookie('font_size', font_size)
        return resp

    # Получение текущих настроек из cookies
    color = request.cookies.get('color')
    background_color = request.cookies.get('background_color')
    font_size = request.cookies.get('font_size')

    # Рендеринг страницы настроек
    return render_template('lab3/settings.html', color=color, background_color=background_color, font_size=font_size)

# Страница оформления билета
@lab3.route('/lab3/trail_ticket')
def trail_ticket():
    return render_template('lab3/trail_ticket.html')

# Расчет стоимости билета
@lab3.route('/lab3/ticket')
def ticket():
    passenger_name = request.args.get('passenger_name')
    passenger_type = request.args.get('passenger_type')
    berth_type = request.args.get('berth_type')
    withunderwear = request.args.get('withunderwear')
    luggage = request.args.get('luggage')
    insurance = request.args.get('insurance')
    passenger_age_str = request.args.get('passenger_age')
    departure_point = request.args.get('departure_point')
    destination = request.args.get('destination')
    travel_date = request.args.get('travel_date')

    # Валидация возраста
    if not passenger_age_str or not passenger_age_str.isdigit():
        return "Ошибка: Возраст должен быть числом", 400
    passenger_age = int(passenger_age_str)
    if not (1 <= passenger_age <= 120):
        return "Ошибка: Возраст должен быть от 1 до 120 лет", 400

    # Расчет стоимости билета
    ticket_price = 700 if passenger_type == 'child' or passenger_age < 18 else 1000
    if berth_type in ['lower', 'lower_side']:
        ticket_price += 100
    if withunderwear == 'on':
        ticket_price += 75
    if luggage == 'on':
        ticket_price += 250
    if insurance == 'on':
        ticket_price += 150

    # Рендеринг страницы с билетом
    return render_template('lab3/ticket.html',
                           passenger_name=passenger_name,
                           passenger_type=passenger_type,
                           berth_type=berth_type,
                           withunderwear=withunderwear,
                           luggage=luggage,
                           insurance=insurance,
                           passenger_age=passenger_age,
                           departure_point=departure_point,
                           destination=destination,
                           travel_date=travel_date,
                           ticket_price=ticket_price)

# Список автомобилей Toyota
cars = [
    {"name": "Toyota Corolla", "price": 22000, "color": "White", "year": 2023},
    {"name": "Toyota Camry", "price": 27000, "color": "Black", "year": 2022},
    {"name": "Toyota Prius", "price": 25000, "color": "Green", "year": 2022},
    {"name": "Toyota Supra", "price": 54000, "color": "Red", "year": 2023},
    {"name": "Toyota Highlander", "price": 45000, "color": "Blue", "year": 2023},
    {"name": "Toyota Sienna", "price": 36000, "color": "Silver", "year": 2023},
    {"name": "Toyota RAV4", "price": 30000, "color": "White", "year": 2023},
    {"name": "Toyota Tacoma", "price": 36000, "color": "Black", "year": 2023},
    {"name": "Toyota Tundra", "price": 52000, "color": "Blue", "year": 2023},
    {"name": "Toyota Avalon", "price": 43000, "color": "Green", "year": 2022},
    {"name": "Toyota Land Cruiser", "price": 85000, "color": "Red", "year": 2021},
    {"name": "Toyota Venza", "price": 33000, "color": "White", "year": 2023},
    {"name": "Toyota Yaris", "price": 17000, "color": "Yellow", "year": 2021},
    {"name": "Toyota Mirai", "price": 58000, "color": "Silver", "year": 2023},
    {"name": "Toyota 4Runner", "price": 51000, "color": "Green", "year": 2023},
    {"name": "Toyota C-HR", "price": 26000, "color": "Black", "year": 2022},
    {"name": "Toyota Sequoia", "price": 67000, "color": "White", "year": 2023},
    {"name": "Toyota Fortuner", "price": 42000, "color": "Blue", "year": 2022},
    {"name": "Toyota Hilux", "price": 55000, "color": "Red", "year": 2023},
    {"name": "Toyota Proace", "price": 32000, "color": "Silver", "year": 2022}
]

# Главная страница с формой для поиска автомобилей
@lab3.route('/lab3/cars')
def index():
    return render_template('lab3/cars.html')

# Обработка результатов поиска автомобилей
@lab3.route('/lab3/result', methods=['POST'])
def result():
    min_price = int(request.form['min_price'])
    max_price = int(request.form['max_price'])

    if min_price > max_price:
        return render_template('lab3/result.html', error="Ошибка: Минимальная цена не может быть выше максимальной")

    # Фильтрация автомобилей по цене
    filtered_cars = [car for car in cars if min_price <= car["price"] <= max_price]
    return render_template('lab3/result.html', cars=filtered_cars, min_price=min_price, max_price=max_price)