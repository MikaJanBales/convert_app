import asyncio

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from convert_app import crud
from convert_app.courses import get_converted_amount
from convert_app.crud import update_course, get_one_course, add_course
from convert_app.db.config import SessionLocal


router = APIRouter()


# Подключение к бд
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Проверка наличия курса в бд
def check_course(from_currency: str, to_currency: str, db: Session):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    _course = get_one_course(db, from_currency, to_currency)
    if _course is None:
        add_course(db, from_currency, to_currency)
    _course = get_one_course(db, from_currency, to_currency)
    return _course


# Эндпоинт для получения списка курсов валют
@router.get("/get_courses")
async def get_courses(db: Session = Depends(get_db)):
    _course = crud.get_all_courses(db)
    return _course


# Эндпоинт для получения актуального курса валют, на вход пара валют, на выход курс
@router.get("/get_course/{from_currency}-{to_currency}")
async def get_course(from_currency: str, to_currency: str, db: Session = Depends(get_db)):
    _course = check_course(from_currency, to_currency, db)
    return _course


# Фоновая задача для обновления курса валют в бд каждый час
async def background_task_scheduler(db: Session):
    while True:
        await update_course(db)
        await asyncio.sleep(3600)  # ожидание: 1 час


# Запуск фоновой задчи для обновления курса валют в бд
@router.on_event("startup")
async def startup_event():
    db = SessionLocal()
    asyncio.create_task(background_task_scheduler(db))


# Эндпоинт для конвертации валют, на вход сумма конвертирования и пара валют, на выходе сумма результата конвертации
@router.post("/converter/{amount}_{from_currency}-{to_currency}")
async def convert(amount: int, from_currency: str, to_currency: str, db: Session = Depends(get_db)):
    _course = check_course(from_currency, to_currency, db)
    converted_amounts = get_converted_amount(_course, amount, from_currency, to_currency)
    return converted_amounts
