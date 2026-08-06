"""Servicios para insertar registros en la base de datos."""

from app.services.database_service import DatabaseService

from app.database.schema_inspector import SchemaInspector


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

    return post_command(
        "prestamos",
        data
    )