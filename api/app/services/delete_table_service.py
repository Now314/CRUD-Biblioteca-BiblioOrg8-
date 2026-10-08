"""Servicios para eliminar préstamos y devolver su stock al catálogo."""

from sqlalchemy import text

from app.database.schema_inspector import SchemaInspector
from app.database.session import SessionLocal


class LoanNotFoundError(Exception):
    """No existe un préstamo con el identificador indicado."""


class BookNotFoundError(Exception):
    """El préstamo referencia un libro que ya no existe en el catálogo."""


def delete_loan(register_id: str) -> bool:
    """Elimina un préstamo y repone una unidad de stock en una transacción."""

    SchemaInspector.validate(table="prestamos", columns=["id", "codigo"])
    SchemaInspector.validate(table="principal", columns=["codigo", "stock"])

    with SessionLocal.begin() as db:
        loan = db.execute(
            text("SELECT codigo FROM prestamos WHERE id = :id FOR UPDATE"),
            {"id": register_id},
        ).mappings().first()

        if loan is None:
            raise LoanNotFoundError(
                f"No existe un préstamo con id '{register_id}'."
            )

        deleted = db.execute(
            text("DELETE FROM prestamos WHERE id = :id"),
            {"id": register_id},
        )

        if deleted.rowcount != 1:
            raise LoanNotFoundError(
                f"No existe un préstamo con id '{register_id}'."
            )

        restored = db.execute(
            text(
                """
                UPDATE principal
                SET stock = stock + 1
                WHERE codigo = :codigo
                """
            ),
            {"codigo": loan["codigo"]},
        )

        if restored.rowcount != 1:
            raise BookNotFoundError(
                "No se encontró el libro asociado; se canceló la eliminación "
                "para no perder el préstamo."
            )

    return True
