"""Routers para método post"""

from fastapi import APIRouter
from app.services.post_table_service import post_loan_table

router = APIRouter(prefix="/post_table", tags=["post_table"])

@router.post("/prestamos")
def post_loan(data:dict):
    return post_loan_table(data)
