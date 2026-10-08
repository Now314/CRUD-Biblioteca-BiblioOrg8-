"""Servicios para editar registros en la base de datos."""

from app.database.schema_inspector import SchemaInspector
from app.database.session import SessionLocal
from sqlalchemy import text


class RegisterNotFoundError(Exception):
    """No existe el registro que se intenta actualizar."""


def put_table(
    table: str,
    register_id: str,
    data: dict,
) -> bool:
    """
    Edita un registro en una tabla.

    Args:
        table: Nombre de la tabla.
        register_id: Identificador del registro.
        data: Diccionario con las columnas y valores a actualizar.

    Returns:
        True si el registro fue editado correctamente.
    """

    SchemaInspector.validate(
        table=table,
        columns=list(data.keys()),
    )

    if not data:
        raise ValueError("Debe enviar al menos un campo para actualizar.")

    set_clause = ", ".join(
        f"{column} = :{column}"
        for column in data
    )

    sql = f"""
        UPDATE {table}
        SET {set_clause}
        WHERE id = :id
    """

    params = {
        **data,
        "id": register_id,
    }

    with SessionLocal.begin() as db:
        result = db.execute(text(sql), params)

        if result.rowcount != 1:
            raise RegisterNotFoundError(
                f"No existe un registro con id '{register_id}'."
            )

    return True
