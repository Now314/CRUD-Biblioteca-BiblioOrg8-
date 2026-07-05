"""Services para llamar y extraer tablas de la base de datos."""

from app.services.database_service import DatabaseService

def get_principal_table():
    return DatabaseService.fetch_all(
        "SELECT * FROM principal"
    )

def get_prestamos_table():
    return DatabaseService.fetch_all(
        "SELECT * FROM prestamos"
    )
