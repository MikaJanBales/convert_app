from pydantic import BaseModel


class CourseSchema(BaseModel):
    id: int
    title: str
    code: str
    rate: float

    class Config:
        orm_mode = True
