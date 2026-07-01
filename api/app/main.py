"""Código Principal del API para BiblioOrg y su Base de Datos PostgreSQL."""

from fastapi import FastAPI
from app.routers.test import router as test

app = FastAPI()

app.include_router(test)

@app.get("/")
def home():
    return {"message": "BiblioOrg API funcionando"}