from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="HistoFakt API (stub)")


class Ask(BaseModel):
    query: str
    language: str = "en"


@app.get("/")
def root():
    return {"msg": "HistoFakt API up!"}


@app.post("/ask")
async def ask(request: Ask):
    return {
        "answer": "Hello World",
        "sources": [],
        "mode": "local-stub"
    }
