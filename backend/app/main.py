from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title="HistoFakt API (stub)")

origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
