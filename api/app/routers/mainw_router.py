"""Routers para Ventana Principal"""

from fastapi import APIRouter
from app.services.mainw_service import get_principal

router = APIRouter(prefix="/main", tags=["main"])

@router.get("/principal")
def get_principal_data():
    return get_principal()