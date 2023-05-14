# convert_app

## Instructions for installing and running the application:

1) Up docker, thereby creating a local database, download all dependencies and run the application using the command:

```
docker-compose up
```

2) Go to host 127.0.0.1

## API usage examples:

1. Getting up-to-date exchange rates:

- HTTP request: GET /exchange/get_courses
- Answer: a list of currency pairs and rates in JSON format

2. Getting the exchange rate of a certain pair of currencies:

- HTTP request: GET /exchange/get_course/{from_currency}-{to_currency}
  {"from_currency": "USD", "to_currency": "RUB"}
- Answer: currency pair and exchange rate in JSON format
  {"from_currency": "USD", "to_currency": "RUB", "rates": 40.468}

3. Converter:

- HTTP request: GET /exchange/converter/{amount}_{from_currency}-{to_currency}
  {"amount": 1000, "from_currency": "USD", "to_currency": "EUR"}
- Answer: currency pair and conversion amount before and after in JSON format
  {"amount": 1000, "from_currency": "USD", "to_currency": "EUR", "converted_amount": 950}

## Assignment:

Разработка API для конвертации валют

Задача: Разработать API для конвертации валют, используя FastAPI, SQLAlchemy и Dependency Injector. API должно
предоставлять возможность получения актуальных курсов валют и конвертации между ними.

Основные функции API:

1. Получение актуальных курсов валют:
    - Создайте модель для хранения информации о валюте (название, код, курс).
    - Реализуйте функцию, которая будет запрашивать актуальные курсы валют с внешнего API (
      например, https://exchangeratesapi.io/) и сохранять их в базе данных.

2. Конвертация между валютами:
    - Реализуйте функцию, которая будет принимать на вход две валюты (исходную и целевую) и сумму для конвертации.
    - Функция должна возвращать результат конвертации на основе актуальных курсов валют из базы данных.

3. Создание и настройка API:
    - Используйте FastAPI для создания API с двумя эндпоинтами: один для получения актуальных курсов валют, другой для
      конвертации между валютами.
    - Настройте взаимодействие с базой данных с помощью SQLAlchemy.
    - Реализуйте внедрение зависимостей с использованием Dependency Injector.