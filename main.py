from uuid import UUID

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import *

app = FastAPI()

class BOOKS(BaseModel):
    id:UUID
    Author: str
    Descriptions: str
    rating: int
    price:int

Books = []

@app.get("/getBooks")
def getBooks():
    return Books

@app.post("/addBooks")
def addBooks(book:BOOKS):
    Books.append(book)
    return book


def start_server():
    # print('Starting Server...')

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )


if __name__ == "__main__":
    start_server()
