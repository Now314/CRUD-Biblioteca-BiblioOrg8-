"""Servicios para editar registros en la base de datos."""

from app.database.schema_inspector import SchemaInspector
from app.services.database_service import DatabaseService


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

    return DatabaseService.execute(
        sql,
        params,
    )
