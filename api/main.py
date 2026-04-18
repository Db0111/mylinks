from fastapi import FastAPI
from sqlmodel import SQLModel, Session
from contextlib import asynccontextmanager

from db import engine
from model import Link 

#lifespan 함수 정의
@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"message":'Hello FastAPI'}

@app.get('/health')
def health_check():
    return {"status":"ok"}


@app.post("/link")
def add_post(link: Link):
    with Session(engine) as session:
        session.add(link)
        session.commit()
        session.refresh(link)
    return link