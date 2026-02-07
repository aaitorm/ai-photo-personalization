from typing import Union
from fastapi import FastAPI

import helpers
app= FastAPI()

@app.get("/")
def read_root():
    #helpers.generate_image()
    return{ "hello": "world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None]= None):
    return{"item_id": item_id, "q": q }