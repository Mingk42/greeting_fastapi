from typing import Union, Annotated

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Conn": "OK"}


class Item(BaseModel):
    name: str

@app.get("/greeting")
async def read_items(greeting_name: Annotated[Item, Query()]):
    return greeting_name