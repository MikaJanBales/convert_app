from sqlalchemy.orm import Session

from convert_app.db.models.courses import Courses


def get_all_courses(session: Session):
    currencies = session.query(Courses).all()
    return currencies










# def create_user(session: Session, user: CreateUserSchema):
#     db_user = NewUser(**user.dict())
#     session.add(db_user)
#     session.commit()
#     session.refresh(db_user)
#     return db_user
#
#
# def get_user(session: Session, email: str):
#     return session.query(NewUser).filter(NewUser.email == email).one()
#
#
# def get_user_by_id(session: Session, id: int):
#     return session.query(NewUser).filter(NewUser.id == id).one()
#
#
# def list_users(session: Session):
#     return session.query(NewUser).all()
#
#
# def get_user_by_id(session: Session, id: int):
#     return session.query(NewUser).filter(NewUser.id == id).one()
