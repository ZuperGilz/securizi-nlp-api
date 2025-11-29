from fastapi import FastAPI
from app.routers import analyze

app = FastAPI(title="Securizi NLP API")

app.include_router(analyze.router)
