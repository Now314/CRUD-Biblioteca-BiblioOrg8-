"""Código Principal del API para BiblioOrg y su Base de Datos PostgreSQL."""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}