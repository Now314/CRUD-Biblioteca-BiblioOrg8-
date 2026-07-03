"""Services para Ventana Principal"""

from app.services.database_service import DatabaseService

def get_principal_table():
    return DatabaseService.fetch_all(
        "SELECT * FROM principal"
    )
