import asyncio

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from db.schemas.courses import ConverterCourseSchema, RateCourseSchema
from courses import get_converted_amount
from crud import update_course, get_one_course, add_course, get_all_courses
from db.config import SessionLocal, get_db

router = APIRouter()


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
    _course = get_all_courses(db)
    return _course


# Эндпоинт для получения актуального курса валют, на вход пара валют, на выход курс
@router.post("/get_course/{from_currency}-{to_currency}")
async def get_course(course: RateCourseSchema, db: Session = Depends(get_db)):
    _course = check_course(course.from_currency, course.to_currency, db)
    return _course


# Фоновая задача для обновления курса валют в бд каждый час
async def background_task_scheduler(db: Session):
    while True:
        await update_course(db)
        await asyncio.sleep(3600)  # ожидание: 1 час


# Запуск фоновой задчи для обновления курса валют в бд
@router.on_event("startup")
async def startup_background_task():
    db = SessionLocal()
    asyncio.create_task(background_task_scheduler(db))


@router.post("/converter/{amount}_{from_currency}-{to_currency}")
async def convert(course: ConverterCourseSchema, db: Session = Depends(get_db)):
    _course = check_course(course.from_currency, course.to_currency, db)
    converted_amounts = get_converted_amount(_course, course.amount, course.from_currency, course.to_currency)
    return converted_amounts
