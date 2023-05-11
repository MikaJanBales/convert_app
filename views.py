from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from convert_app import crud
from convert_app.db.config import SessionLocal
from convert_app.db.schemas.courses import CurrencySchema

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/get_courses")
async def get_courses(db: Session = Depends(get_db)):
    _currency = crud.get_all_courses(db)
    return _currency


@router.get("/get_course/{course_id}")
async def get_course(course_id: int, db: Session = Depends(get_db)):
    _currency = crud.get_one_courses(db, course_id)
    return _currency

#
# @router.get("/converter")
# async def get_converted_currencies(db: Session = Depends(get_db)):
#     _currency = crud.converting(db)
#     return _currency
