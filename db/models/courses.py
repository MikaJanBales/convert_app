from sqlalchemy import Integer, Column, String, Float

from convert_app.db.config import Base


class Courses(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    to_currency = Column(String(10), nullable=False)
    from_currency = Column(String(10), nullable=False)
    rate = Column(Float, nullable=False)

    def __repr__(self):
        return f'<Courses "{self.title}">'
