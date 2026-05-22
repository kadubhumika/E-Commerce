from fastapi import FastAPI

from core.db import engine
from models.base import Base

import models


app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/")
def home():

    return {
        "message":"Ecommerce Backend Running"
    }