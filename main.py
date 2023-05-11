import uvicorn
from fastapi import FastAPI
from db.config import Base, engine
from views import router

Base.metadata.create_all(engine)
app = FastAPI(title="Converter")

app.include_router(router, prefix="/convert", tags=["convert"])

if __name__ == "__main__":
    uvicorn.run('main:app', port=8000, host='localhost', reload=True)
