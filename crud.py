from sqlalchemy.orm import Session

from courses import get_course_currencies
from db.models.courses import Course


# Получение всех курсов из бд
def get_all_courses(session: Session):
    try:
        courses = session.query(Course).all()
        return courses
    except Exception as error:
        print("Ошибка при работе с PostgreSQL", error)


# Получение определенного курса из бд
def get_one_course(session: Session, from_currency: str, to_currency: str):
    try:
        course = session.query(Course).filter(Course.from_currency == from_currency,
                                              Course.to_currency == to_currency).first()
        return course
    except Exception as error:
        print("Ошибка при работе с PostgreSQL", error)


# Добавление курса в бд
def add_course(session: Session, from_currency: str, to_currency: str):
    try:
        rate = get_course_currencies(from_currency, to_currency)
        course = Course(
            from_currency=from_currency,
            to_currency=to_currency,
            rate=rate
        )
        session.add(course)
        session.commit()
    except Exception as error:
        print("Ошибка при работе с PostgreSQL", error)


# Обновление всех курсов в бд
async def update_course(session: Session):
    try:
        courses = session.query(Course).all()
        for course in courses:
            rate = get_course_currencies(course.from_currency, course.to_currency)
            course.rate = rate
        session.add_all(courses)
        session.commit()
    except AttributeError as error:
        print(error)
