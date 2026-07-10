"""Routers para método get"""

from fastapi import APIRouter
from app.services.get_table_service import get_principal_table
from app.services.get_table_service import get_prestamos_table

router = APIRouter(prefix="/get_table", tags=["get_table"])

@router.get("/principal")
def get_principal_data():
    return get_principal_table()

@router.get("/prestamos")
def get_prestamos_data():
    return get_prestamos_table()