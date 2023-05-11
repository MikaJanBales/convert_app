from pydantic import BaseModel


class CoursesSchema(BaseModel):
    id: int
    title: str
    code: str
    rate: float

    class Config:
        orm_mode = True
