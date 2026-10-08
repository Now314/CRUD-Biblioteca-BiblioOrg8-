"""Servicios para eliminar préstamos y devolver su stock al catálogo."""

from sqlalchemy import text

from app.database.schema_inspector import SchemaInspector
from app.database.session import SessionLocal
from app.services.history_service import ensure_history_table


class LoanNotFoundError(Exception):
    """No existe un préstamo con el identificador indicado."""


class BookNotFoundError(Exception):
    """El préstamo referencia un libro que ya no existe en el catálogo."""


def delete_loan(register_id: str) -> bool:
    """Archiva y elimina un préstamo, y repone el stock atómicamente."""

    SchemaInspector.validate(table="prestamos", columns=["id", "codigo"])
    SchemaInspector.validate(table="principal", columns=["codigo", "stock"])

    with SessionLocal.begin() as db:
        ensure_history_table(db)
        loan = db.execute(
            text("SELECT * FROM prestamos WHERE id = :id FOR UPDATE"),
            {"id": register_id},
        ).mappings().first()

        if loan is None:
            raise LoanNotFoundError(
                f"No existe un préstamo con id '{register_id}'."
            )

        loan_data = dict(loan)
        archive_columns = [
            column for column in loan_data if column != "fecha_eliminacion"
        ]
        column_list = ", ".join(archive_columns + ["fecha_eliminacion"])
        value_list = ", ".join(
            [f":{column}" for column in archive_columns] + ["CURRENT_TIMESTAMP"]
        )
        db.execute(
            text(
                f"""
                INSERT INTO historial ({column_list})
                VALUES ({value_list})
                """
            ),
            {column: loan_data[column] for column in archive_columns},
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
            {"codigo": loan_data["codigo"]},
        )

        if restored.rowcount != 1:
            raise BookNotFoundError(
                "No se encontró el libro asociado; se canceló la eliminación "
                "para no perder el préstamo."
            )

    return True
