"""Código Principal del API para BiblioOrg y su Base de Datos PostgreSQL."""

from fastapi import FastAPI
from app.routers.test import router as test
from app.routers.mainw_router import router as mainw

app = FastAPI()

app.include_router(test)
app.include_router(mainw)

@app.get("/")
def home():
    return {"message": "BiblioOrg API funcionando"}