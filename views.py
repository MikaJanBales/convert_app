import asyncio

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from db.schemas.courses import ConverterCourseSchema, RateCourseSchema
from courses import get_converted_amount
from crud import update_course, get_one_course, add_course, get_all_courses
from db.config import get_db, db

router = APIRouter()


# Проверка наличия курса в бд
def check_course(from_currency: str, to_currency: str, session: Session):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    course = get_one_course(session, from_currency, to_currency)
    if course is None:
        add_course(session, from_currency, to_currency)
        course = get_one_course(session, from_currency, to_currency)
    return course


# Эндпоинт для получения списка курсов валют
@router.get("/get_courses")
async def get_courses(session: Session = Depends(get_db)):
    course = get_all_courses(session)
    return course


# Эндпоинт для получения актуального курса валют, на вход пара валют, на выход курс
@router.post("/get_course/{from_currency}-{to_currency}")
async def get_course(schema_course: RateCourseSchema, session: Session = Depends(get_db)):
    course = check_course(schema_course.from_currency, schema_course.to_currency, session)
    return course


# Фоновая задача для обновления курса валют в бд каждый час
async def background_task_scheduler(session: Session):
    while True:
        await update_course(session)
        await asyncio.sleep(3600)  # ожидание: 1 час


# Запуск фоновой задчи для обновления курса валют в бд
@router.on_event("startup")
async def startup_background_task():
    asyncio.create_task(background_task_scheduler(db))


@router.post("/converter/{amount}_{from_currency}-{to_currency}")
async def convert(schema_course: ConverterCourseSchema, session: Session = Depends(get_db)):
    course = check_course(schema_course.from_currency, schema_course.to_currency, session)
    converted_amounts = get_converted_amount(course, schema_course.amount, schema_course.from_currency,
                                             schema_course.to_currency)
    return converted_amounts
