from sqlalchemy import Integer, Column, String, Float

from convert_app.db.config import Base


class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True)
    from_currency = Column(String(10), nullable=False)
    to_currency = Column(String(10), nullable=False)
    rate = Column(Float, nullable=False)

    def __repr__(self):
        return f'<Course "{self.title}">'
