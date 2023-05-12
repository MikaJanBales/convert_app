from sqlalchemy.orm import Session

from convert_app.courses import get_course_currencies
from convert_app.db.models.courses import Course


# Получение всех курсов из бд
def get_all_courses(session: Session):
    courses = session.query(Course).all()
    return courses


# Получение определенного курса из бд
def get_one_course(session: Session, from_currency: str, to_currency: str):
    course = session.query(Course).filter(Course.from_currency == from_currency,
                                          Course.to_currency == to_currency).first()
    return course


# Добавление курса в бд
def add_course(session: Session, from_currency: str, to_currency: str):
    rate = get_course_currencies(from_currency, to_currency)
    course = Course(
        from_currency=from_currency,
        to_currency=to_currency,
        rate=rate
    )
    session.add(course)
    session.commit()


# Обновление курса из бд
def update_course(session: Session, from_currency: str, to_currency: str):
    rate = get_course_currencies(from_currency, to_currency)
    session.query(Course).filter(Course.from_currency == from_currency,
                                 Course.to_currency == to_currency).update({"rate": rate},
                                                                           synchronize_session='fetch')
    session.commit()
