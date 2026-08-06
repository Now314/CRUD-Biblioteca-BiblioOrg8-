"""Routers para método put."""

from fastapi import APIRouter
from app.services.put_table_service import put_table

router = APIRouter(prefix="/put_table", tags=["put_table"])

@router.put("/prestamos")
def put_loan(register_id: str, data: dict):
    return put_table(table="prestamos", register_id=register_id, data=data,)
