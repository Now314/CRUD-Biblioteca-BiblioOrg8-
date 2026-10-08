"""Services para llamar y extraer tablas de la base de datos."""

import re

from app.database.schema_inspector import SchemaInspector
from app.services.database_service import DatabaseService


def _natural_code_key(code: object) -> tuple[tuple[int, object], ...]:
    """Construye una clave que ordena los segmentos numéricos como números."""

    parts = re.split(r"(\d+)", str(code).casefold())
    return tuple(
        (0, int(part)) if part.isdecimal() else (1, part)
        for part in parts
    )


def get_principal_table():
    """Obtiene los registros de la tabla principal."""

    SchemaInspector.validate(table="principal")

    records = DatabaseService.fetch_all("SELECT * FROM principal")

    return sorted(
        records,
        key=lambda record: _natural_code_key(record["codigo"]),
    )

def get_prestamos_table():
    """Obtiene los registros de la tabla préstamos."""

    SchemaInspector.validate(table="prestamos")

    return DatabaseService.fetch_all(
        "SELECT * FROM prestamos"
    )


