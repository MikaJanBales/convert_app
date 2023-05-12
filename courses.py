import requests
from sqlalchemy.orm import Session

from convert_app.crud import get_one_course

API_KEY = "eGgkuOeHlKFE8UA9LVfnyYR8CGSR0ESH"


# Функция для конвертации валют
def get_course_currencies(from_currency, to_currency):
    # Корреткировка названий валют
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    # URL для доступа к API Open Exchange Rates
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={to_currency}&base={from_currency}"

    payload = {}
    headers = {
        "apikey": "eGgkuOeHlKFE8UA9LVfnyYR8CGSR0ESH"
    }

    # Отправляем GET-запрос
    response = requests.request("GET", url, headers=headers, data=payload)

    # Обрабатываем ответ сервера
    if response.status_code == 200:
        data = response.json()
        course = data["rates"][to_currency]
        course = round(course, 3)
        return course
    else:
        raise


# Конвертация валют
def get_converted_amount(session: Session, amount: int, from_currency: str, to_currency: str):
    course = get_one_course(session, from_currency, to_currency)
    rate = course.rate
    converted_amount = round(amount * rate, 3)
    convert = {
        from_currency: amount,
        to_currency: converted_amount
    }
    return convert
