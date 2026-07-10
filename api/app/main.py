"""Código Principal del API para BiblioOrg y su Base de Datos PostgreSQL."""

from fastapi import FastAPI
from app.routers.get_table_router import router as get_tables
from app.routers.post_table_router import post_table

app = FastAPI()

app.include_router(get_tables)
app.include_router(post_table)

@app.get("/")
def home():
    return {"message": "BiblioOrg API funcionando"}
