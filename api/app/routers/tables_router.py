"""Routers para Ventana Principal"""

from fastapi import APIRouter
from app.services.tables_service import get_principal_table

router = APIRouter(prefix="/tables", tags=["tables"])

@router.get("/principal")
def get_principal_data():
    return get_principal_table()