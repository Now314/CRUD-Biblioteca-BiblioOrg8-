"""Services para llamar y extraer tablas de la base de datos."""

from app.database.schema_inspector import SchemaInspector
from app.services.database_service import DatabaseService


def get_principal_table():
    """Obtiene los registros de la tabla principal."""

    SchemaInspector.validate(table="principal")

    return DatabaseService.fetch_all(
        "SELECT * FROM principal"
    )

def get_prestamos_table():
    """Obtiene los registros de la tabla préstamos."""

    SchemaInspector.validate(table="prestamos")

    return DatabaseService.fetch_all(
        "SELECT * FROM prestamos"
    )


