from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from convert_app import crud
from convert_app.crud import add_course, get_one_course
from convert_app.db.config import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/get_courses")
async def get_courses(db: Session = Depends(get_db)):
    _course = crud.get_all_courses(db)
    return _course


@router.get("/get_course/{from_currency}-{to_currency}")
async def get_course(from_currency: str, to_currency: str, db: Session = Depends(get_db)):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    _course = get_one_course(db, from_currency, to_currency)
    if _course is None:
        add_course(db, from_currency, to_currency)
        _course = get_one_course(db, from_currency, to_currency)
    return _course


# @router.get("/converter")
# async def get_converting_(db: Session = Depends(get_db)):
#     _currency = crud.converting(db)
#     return _currency
