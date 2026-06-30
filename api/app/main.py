"""Código Principal del API para BiblioOrg y su Base de Datos PostgreSQL."""

from fastapi import FastAPI
from sqlalchemy import text

from app.database.session import engine

app = FastAPI()

@app.get("/")
def home():
    return {"message": "BiblioOrg API funcionando"}

@app.get("/db-test")
def db_test():
    with engine.connect() as conn:
        version = conn.execute(text("SELECT version()"))
        return {"database": version.scalar()}