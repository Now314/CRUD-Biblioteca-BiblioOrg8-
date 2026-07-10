"""Routers para método post"""

from fastapi import APIRouter
from app.services.get_table_service import get_principal_table
from app.services.get_table_service import get_prestamos_table
from app.services.post_table_service import post_loan_table

router = APIRouter(prefix="/post_table", tags=["post_table"])

@router.get("/prestamos")
def post_loan(data:dict):
    return post_loan_table(data)
