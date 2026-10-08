"""Routers para método post"""

from fastapi import APIRouter, HTTPException, status
from app.services.post_table_service import (
    StockUnavailableError,
    post_loan_table,
)

router = APIRouter(prefix="/post_table", tags=["post_table"])

@router.post("/prestamos")
def post_loan(data:dict):
    try:
        return post_loan_table(data)
    except StockUnavailableError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error
