from sqlalchemy.orm import Session

from convert_app.courses import get_course_currencies
from convert_app.db.models.courses import Course


def get_all_courses(session: Session):
    courses = session.query(Course).all()
    return courses


def get_one_course(session: Session, from_currency: str, to_currency: str):
    course = session.query(Course).filter(Course.from_currency == from_currency,
                                          Course.to_currency == to_currency).first()
    return course


def add_course(session: Session, from_currency: str, to_currency: str):
    rate = get_course_currencies(from_currency, to_currency)
    course = Course(
        from_currency=from_currency,
        to_currency=to_currency,
        rate=rate
    )
    session.add(course)
    session.commit()


def get_converted_amount(session: Session, amount: int, from_currency: str, to_currency: str):
    course = get_one_course(session, from_currency, to_currency)
    rate = course.rate
    converted_amount = round(amount * rate, 2)
    convert = {
        from_currency: amount,
        to_currency: converted_amount
    }
    return convert
