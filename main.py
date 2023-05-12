import uvicorn
from fastapi import FastAPI

from db.models.courses import Base
from db.config import engine
from views import router

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Exchange", docs_url="/", redoc_url=None)

app.include_router(router, prefix="/exchange", tags=["exchange"])

if __name__ == "__main__":
    uvicorn.run('main:app', port=8000, host='localhost', reload=True)
