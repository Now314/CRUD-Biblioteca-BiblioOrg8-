"""Utilidades para cargar y obtener datos desde widgets."""
from datetime import date, datetime

from PySide6.QtCore import QDate, QDateTime
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDoubleSpinBox,
    QLineEdit,
    QPlainTextEdit,
    QSpinBox,
    QTextEdit,
)


class FieldsUtility:
    @staticmethod
    def load_fields(data: dict, fields: dict):
        """
        Carga valores de un diccionario en los widgets indicados.

        Widgets compatibles:
        - QLineEdit
        - QTextEdit
        - QPlainTextEdit
        - QComboBox
        - QSpinBox
        - QDoubleSpinBox
        - QDateEdit
        - QDateTimeEdit
        - QCheckBox
        """

        for field, widget in fields.items():
            value = data.get(field)

            # ---------- QLineEdit ----------
            if isinstance(widget, QLineEdit):
                widget.setText("" if value is None else str(value))

            # ---------- QTextEdit / QPlainTextEdit ----------
            elif isinstance(widget, (QTextEdit, QPlainTextEdit)):
                widget.setPlainText("" if value is None else str(value))

            # ---------- QComboBox ----------
            elif isinstance(widget, QComboBox):
                widget.setCurrentText("" if value is None else str(value))

            # ---------- QSpinBox ----------
            elif isinstance(widget, QSpinBox):
                if isinstance(value, (int, float)):
                    widget.setValue(int(value))
                else:
                    widget.setValue(0)

            # ---------- QDoubleSpinBox ----------
            elif isinstance(widget, QDoubleSpinBox):
                if isinstance(value, (int, float)):
                    widget.setValue(float(value))
                else:
                    widget.setValue(0.0)

            # ---------- QDateEdit ----------
            elif isinstance(widget, QDateEdit):
                if isinstance(value, date):
                    widget.setDate(QDate(value.year, value.month, value.day))

                elif isinstance(value, str):
                    qdate = QDate.fromString(value, "yyyy-MM-dd")

                    if qdate.isValid():
                        widget.setDate(qdate)

                elif isinstance(value, QDate):
                    widget.setDate(value)

            # ---------- QDateTimeEdit ----------
            elif isinstance(widget, QDateTimeEdit):
                if isinstance(value, datetime):
                    widget.setDateTime(
                        QDateTime.fromSecsSinceEpoch(int(value.timestamp()))
                    )

                elif isinstance(value, QDateTime):
                    widget.setDateTime(value)

            # ---------- QCheckBox ----------
            elif isinstance(widget, QCheckBox):
                widget.setChecked(bool(value))

    @staticmethod
    def get_fields(fields: dict) -> dict:
        """
        Obtiene los valores de los widgets y los devuelve en un diccionario.

        Los valores se convierten a tipos nativos de Python.
        """

        data = {}

        for field, widget in fields.items():
            if isinstance(widget, QLineEdit):
                data[field] = widget.text().strip()

            elif isinstance(widget, (QTextEdit, QPlainTextEdit)):
                data[field] = widget.toPlainText().strip()

            elif isinstance(widget, QComboBox):
                data[field] = widget.currentText()

            elif isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                data[field] = widget.value()

            elif isinstance(widget, QDateEdit):
                data[field] = widget.date().toPython()

            elif isinstance(widget, QDateTimeEdit):
                data[field] = widget.dateTime().toPython()

            elif isinstance(widget, QCheckBox):
                data[field] = widget.isChecked()

        return data
