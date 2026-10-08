"""Routers para método put."""

from fastapi import APIRouter, HTTPException, status
from app.services.put_table_service import RegisterNotFoundError, put_table

router = APIRouter(prefix="/put_table", tags=["put_table"])

@router.put("/prestamos")
def put_loan(register_id: str, data: dict):
    try:
        return put_table(table="prestamos", register_id=register_id, data=data)
    except RegisterNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        ) from error
