from uuid import UUID

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import *
from  cohere_lib import *

app = FastAPI()

class Review(BaseModel):
    review: str

review_list = []

@app.get("/showMovieReviews")
def showReview():
    return data[::-1]


@app.post("/addMovieReviews")
def addMovieReview(review:Review):
    obj = CohereModel()
    response = obj.createClassify(review.review)
    return response



def startServer():
    # print('Starting Server...')

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )


if __name__ == "__main__":
    startServer()
