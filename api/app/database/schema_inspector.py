"""Inspección y validación del esquema de la base de datos."""

from typing import cast

from sqlalchemy import inspect
from sqlalchemy.engine.reflection import Inspector

from app.database.session import engine


class SchemaInspector:
    """Inspecciona y valida el esquema de la base de datos."""

    _schema: dict[str, set[str]] = {}

    @classmethod
    def load_schema(cls) -> None:
        """Carga el esquema de la base de datos."""

        inspector = cast(Inspector, inspect(engine))

        cls._schema = {
            table: {
                column["name"]
                for column in inspector.get_columns(table)
            }
            for table in inspector.get_table_names()
        }

    @classmethod
    def reload_schema(cls) -> None:
        """Recarga el esquema almacenado."""

        cls.load_schema()

    @classmethod
    def get_schema(cls) -> dict[str, set[str]]:
        """Obtiene el esquema almacenado."""

        if not cls._schema:
            cls.load_schema()

        return cls._schema

    @classmethod
    def validate_table(cls, table: str) -> None:
        """Válida que una tabla exista."""

        if table not in cls.get_schema():
            raise ValueError(f"La tabla '{table}' no existe.")

    @classmethod
    def validate_columns(
        cls,
        table: str,
        columns: list[str],
    ) -> None:
        """Válida que las columnas existan."""

        cls.validate_table(table)

        valid_columns = cls.get_schema()[table]

        invalid_columns = set(columns) - valid_columns

        if invalid_columns:
            raise ValueError(
                f"Columnas inválidas en '{table}': "
                f"{', '.join(sorted(invalid_columns))}"
            )

    @classmethod
    def validate(
            cls,
            table: str,
            columns: list[str] | None = None,
    ) -> None:
        """Válida una tabla y, opcionalmente, sus columnas."""

        cls.validate_table(table)

        if columns:
            cls.validate_columns(table, columns)