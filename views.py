from fastapi import APIRouter
from fastapi_utils.tasks import repeat_every

from db.schemas.courses import ConverterCourseSchema, RateCourseSchema
from courses import get_converted_amount
from crud import update_course, get_one_course, add_course, get_all_courses

router = APIRouter()


# Проверка наличия курса в бд
def check_course(from_currency: str, to_currency: str):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    course = get_one_course(from_currency, to_currency)
    if course is None:
        add_course(from_currency, to_currency)
        course = get_one_course(from_currency, to_currency)
    return course


# Эндпоинт для получения списка курсов валют
@router.get("/get_courses")
async def get_courses():
    course = get_all_courses()
    return course


# Эндпоинт для получения актуального курса валют, на вход пара валют, на выход курс
@router.post("/get_course/{from_currency}-{to_currency}")
async def get_course(schema_course: RateCourseSchema):
    course = check_course(schema_course.from_currency, schema_course.to_currency)
    return course


# Запуск фоновой задчи для обновления курса валют в бд
@router.on_event("startup")
@repeat_every(seconds=3600)  # 1 hour
async def startup_background_task():
    await update_course()


@router.post("/converter/{amount}_{from_currency}-{to_currency}")
async def convert(schema_course: ConverterCourseSchema):
    course = check_course(schema_course.from_currency, schema_course.to_currency)
    converted_amounts = get_converted_amount(course, schema_course.amount, schema_course.from_currency,
                                             schema_course.to_currency)
    return converted_amounts
