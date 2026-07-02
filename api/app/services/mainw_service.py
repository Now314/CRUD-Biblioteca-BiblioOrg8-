"""Services para Ventana Principal"""

from sqlalchemy import text
from app.database.session import SessionLocal

def get_principal():
    db = SessionLocal()
    try:
        table = db.execute(text("SELECT * from principal"))
        return table.mappings().all()
    finally:
        db.close()