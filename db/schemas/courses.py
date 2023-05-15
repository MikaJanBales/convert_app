from pydantic import BaseModel, Field


class ConverterCourseSchema(BaseModel):
    amount: float = Field(gt=0)
    from_currency: str
    to_currency: str

    class Config:
        orm_mode = True


class RateCourseSchema(BaseModel):
    from_currency: str
    to_currency: str

    class Config:
        orm_mode = True
