from typing import Union, Annotated

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

history={}

@app.get("/")
def read_root():
    return {"Conn": "OK"}


class Item(BaseModel):
    name: str

@app.get("/greeting")
async def read_items(greeting_name: Annotated[Item, Query()]):
    if "name" in history:
        history["name"].append(dict(greeting_name)["name"])
    else:
        history["name"]=[dict(greeting_name)["name"]]

    return history