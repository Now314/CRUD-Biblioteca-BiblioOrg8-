"""Código Principal del API para BiblioOrg y su Base de Datos PostgreSQL."""

from fastapi import FastAPI
from app.routers.get_table_router import router as get_table
from app.routers.post_table_router import router as post_table
from app.routers.put_table_router import router as put_table

app = FastAPI()

app.include_router(get_table)
app.include_router(post_table)
app.include_router(put_table)

@app.get("/")
def home():
    return {"message": "BiblioOrg API funcionando"}
