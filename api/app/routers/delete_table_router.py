"""Router para eliminar préstamos."""

from fastapi import APIRouter, HTTPException, status

from app.services.delete_table_service import (
    BookNotFoundError,
    LoanNotFoundError,
    delete_loan,
)


router = APIRouter(prefix="/delete_table", tags=["delete_table"])


@router.delete("/prestamos/{register_id}")
def delete_loan_endpoint(register_id: str):
    try:
        return delete_loan(register_id)
    except LoanNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        ) from error
    except BookNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error
