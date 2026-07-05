"""Código Principal del API para BiblioOrg y su Base de Datos PostgreSQL."""

from fastapi import FastAPI
from app.routers.tables_router import router as main

app = FastAPI()

app.include_router(main)

@app.get("/")
def home():
    return {"message": "BiblioOrg API funcionando"}
