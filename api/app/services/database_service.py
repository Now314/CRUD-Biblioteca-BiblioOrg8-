"""Servicio para gestionar SQl dentro de la Base de Datos."""

from sqlalchemy import text

from app.database.session import SessionLocal

class DatabaseService:
    """
    Proporciona métodos para ejecutar consultas SQL contra la base de datos.

    Centraliza el acceso a PostgreSQL mediante SQLAlchemy, administrando la
    apertura y cierre de sesiones para evitar duplicar lógica en los servicios
    de la aplicación.
    """

    @staticmethod
    def execute(sql: str, params: dict | None = None):
        """
        Ejecuta una sentencia SQL que modifica la base de datos.

        Args:
            sql: Sentencia SQL a ejecutar.
            params: Parámetros de la consulta.

        Returns:
            True si la operación se realizó correctamente.
        """

        db = SessionLocal()

        try:
            db.execute(text(sql), params or {})
            db.commit()
            return True

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()

    @staticmethod
    def fetch_all(sql: str, params: dict | None = None):
        """
        Ejecuta una consulta SQL y devuelve todos los registros encontrados.

        Args:
            sql: Consulta SQL a ejecutar.
            params: Diccionario con los parámetros de la consulta.

        Returns:
            Una lista de diccionarios, donde cada elemento representa un registro
            obtenido de la base de datos.
        """
        db = SessionLocal()

        try:
            result = db.execute(text(sql), params or {})
            return result.mappings().all()

        finally:
            db.close()

    @staticmethod
    def ping() -> bool:
        db = SessionLocal()

        try:
            db.execute(text("SELECT 1"))
            return True
        finally:
            db.close()