"""Creación y consulta de la tabla persistente de historial de préstamos."""

from sqlalchemy import text

from app.database.schema_inspector import SchemaInspector
from app.database.session import SessionLocal


def ensure_history_table(db) -> None:
    """Crea historial en PostgreSQL si todavía no existe."""

    SchemaInspector.validate(table="prestamos")
    db.execute(
        text(
            """
            CREATE TABLE IF NOT EXISTS historial (
                LIKE prestamos INCLUDING DEFAULTS
            )
            """
        )
    )
    db.execute(
        text(
            """
            ALTER TABLE historial
            ADD COLUMN IF NOT EXISTS fecha_eliminacion TIMESTAMPTZ
            NOT NULL DEFAULT CURRENT_TIMESTAMP
            """
        )
    )


def get_history_table():
    """Devuelve los préstamos archivados, del más reciente al más antiguo."""

    SchemaInspector.validate(table="prestamos")

    with SessionLocal.begin() as db:
        ensure_history_table(db)
        result = db.execute(
            text(
                """
                SELECT * FROM historial
                ORDER BY fecha_eliminacion DESC, id DESC
                """
            )
        )
        return result.mappings().all()
