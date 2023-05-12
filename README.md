# convert_app

## Instructions for installing and running the application:

1) Download all the libraries and packages with the required versions required for the project using the command:

```
pip install -r requirements.txt
```

2) We start docker, thereby creating a local database using the command:

```
docker-compose up -d
```

3) Run the application locally using the command:

```
python main.py 
```

## Assignment:

Разработка API для конвертации валют

Задача: Разработать API для конвертации валют, используя FastAPI, SQLAlchemy и Dependency Injector. API должно предоставлять возможность получения актуальных курсов валют и конвертации между ними.

Основные функции API:

1. Получение актуальных курсов валют:
   - Создайте модель для хранения информации о валюте (название, код, курс).
   - Реализуйте функцию, которая будет запрашивать актуальные курсы валют с внешнего API (например, https://exchangeratesapi.io/) и сохранять их в базе данных.

2. Конвертация между валютами:
   - Реализуйте функцию, которая будет принимать на вход две валюты (исходную и целевую) и сумму для конвертации.
   - Функция должна возвращать результат конвертации на основе актуальных курсов валют из базы данных.

3. Создание и настройка API:
   - Используйте FastAPI для создания API с двумя эндпоинтами: один для получения актуальных курсов валют, другой для конвертации между валютами.
   - Настройте взаимодействие с базой данных с помощью SQLAlchemy.
   - Реализуйте внедрение зависимостей с использованием Dependency Injector.