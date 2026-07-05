"""Routers para Ventana Principal"""

from fastapi import APIRouter
from app.services.tables_service import get_principal_table
from app.services.tables_service import get_prestamos_table

router = APIRouter(prefix="/tables", tags=["tables"])

@router.get("/principal")
def get_principal_data():
    return get_principal_table()

@router.get("/prestamos")
def get_prestamos_data():
    return get_prestamos_table()