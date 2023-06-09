from sqlalchemy import Integer, Column, String, Float

from db.config import Base


class Course(Base):
    __tablename__ = "course"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    from_currency = Column(String(10), nullable=False)
    to_currency = Column(String(10), nullable=False)
    rate = Column(Float, nullable=False)

    def __repr__(self):
        return f'<Course "{self.title}">'
