"""Services Básicos y Generales para BiblioOrg"""

from sqlalchemy import text
from app.database.session import SessionLocal

class DatabaseService:

    @staticmethod
    def fetch_all(sql: str, params: dict | None = None):

        db = SessionLocal()

        try:
            result = db.execute(text(sql), params or {})
            return result.mappings().all()

        finally:
            db.close()