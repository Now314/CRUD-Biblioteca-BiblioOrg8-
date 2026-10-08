"""Servicios para insertar registros en la base de datos."""

from app.database.schema_inspector import SchemaInspector
from app.database.session import SessionLocal
from app.services.database_service import DatabaseService
from sqlalchemy import text


class StockUnavailableError(Exception):
    """El libro no existe o no tiene unidades disponibles para préstamo."""


def post_command(
    table: str,
    data: dict,
) -> bool:
    """
    Inserta un registro en una tabla.

    Args:
        table: Nombre de la tabla.
        data: Diccionario con las columnas y valores.

    Returns:
        True si el registro fue creado correctamente.
    """

    SchemaInspector.validate(
        table=table,
        columns=list(data.keys()),
    )

    columns = ", ".join(data.keys())

    values = ", ".join(
        f":{column}"
        for column in data.keys()
    )

    sql = f"""
        INSERT INTO {table} ({columns})
        VALUES ({values})
    """

    return DatabaseService.execute(
        sql,
        data,
    )

def post_loan_table(data: dict):
    """Registra un préstamo y descuenta una unidad del stock atómicamente."""

    if "codigo" not in data:
        raise ValueError("El préstamo debe incluir el código del libro.")

    SchemaInspector.validate(
        table="principal",
        columns=["codigo", "stock"],
    )
    SchemaInspector.validate(
        table="prestamos",
        columns=list(data.keys()),
    )

    columns = ", ".join(data.keys())
    values = ", ".join(f":{column}" for column in data.keys())

    # SessionLocal.begin() confirma al salir correctamente y revierte todos
    # los cambios si se produce una excepción en cualquiera de las consultas.
    with SessionLocal.begin() as db:
        stock_update = db.execute(
            text(
                """
                UPDATE principal
                SET stock = stock - 1
                WHERE codigo = :codigo AND stock > 0
                """
            ),
            {"codigo": data["codigo"]},
        )

        if stock_update.rowcount != 1:
            raise StockUnavailableError(
                "No se pudo registrar el préstamo: el libro no existe "
                "o no tiene stock disponible."
            )

        db.execute(
            text(
                f"""
                INSERT INTO prestamos ({columns})
                VALUES ({values})
                """
            ),
            data,
        )

    return True
