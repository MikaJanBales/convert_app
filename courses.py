import requests

API_CONVERT = "fc66c1e4fe94bd298f5d8414"


# функция для конвертации валют
def get_converted_currencies(from_wallet, to_wallet):
    # Корреткировка названий валют
    from_wallet = from_wallet.upper()
    to_wallet = to_wallet.upper()

    # URL для доступа к API Exchange Rate
    url = f'https://v6.exchangerate-api.com/v6/{API_CONVERT}/latest/{from_wallet}'

    # Отправляем GET-запрос
    response = requests.get(url)

    # Обрабатываем ответ сервера
    if response.status_code == 200:
        data = response.json()
        course = data["conversion_rates"][to_wallet]
        course = round(course, 3)
        return course
    else:
        raise


print(get_course("RUB", "USD"))
