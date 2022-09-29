# main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id : str
    q: str

@app.post("/chat")
async def chatty(d : Item):
    return d