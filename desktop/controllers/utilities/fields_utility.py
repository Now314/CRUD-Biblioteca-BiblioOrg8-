"""Utilidades para cargar y obtener datos desde widgets."""

from PySide6.QtCore import QObject, QDate


class FieldsUtility(QObject):
    @staticmethod
    def load_fields(data: dict, fields: dict):
        """
        Carga valores de un diccionario en los widgets indicados.

        El diccionario debe tener la forma:
            {
                "campo_bd": widget
            }

        Widgets compatibles:
        - QLineEdit
        - QTextEdit
        - QPlainTextEdit
        - QComboBox
        - QSpinBox
        - QDoubleSpinBox
        - QDateEdit
        - QCheckBox
        """

        for field, widget in fields.items():
            value = data.get(field)

            if value is None:
                value = ""

            # QLineEdit
            if hasattr(widget, "setText"):
                widget.setText(str(value))

            # QTextEdit / QPlainTextEdit
            elif hasattr(widget, "setPlainText"):
                widget.setPlainText(str(value))

            elif hasattr(widget, "setHtml"):
                widget.setPlainText(str(value))

            # QComboBox
            elif hasattr(widget, "setCurrentText"):
                widget.setCurrentText(str(value))

            # QSpinBox / QDoubleSpinBox
            elif hasattr(widget, "setValue") and isinstance(value, (int, float)):
                widget.setValue(value)

            # QDateEdit
            elif hasattr(widget, "setDate"):
                if isinstance(value, QDate):
                    widget.setDate(value)

                elif value:
                    date = QDate.fromString(str(value), "yyyy-MM-dd")

                    if date.isValid():
                        widget.setDate(date)

            # QCheckBox
            elif hasattr(widget, "setChecked"):
                widget.setChecked(bool(value))

    @staticmethod
    def get_fields(fields: dict) -> dict:
        """
        Obtiene los valores de los widgets y los devuelve en un diccionario.

        Devuelve un diccionario con la forma:
            {
                "campo_bd": valor
            }
        """

        data = {}

        for field, widget in fields.items():
            # QLineEdit
            if hasattr(widget, "text"):
                data[field] = widget.text().strip()

            # QTextEdit
            elif hasattr(widget, "toPlainText"):
                data[field] = widget.toPlainText().strip()

            # QComboBox
            elif hasattr(widget, "currentText"):
                data[field] = widget.currentText()

            # QSpinBox / QDoubleSpinBox
            elif hasattr(widget, "value"):
                data[field] = widget.value()

            # QDateEdit
            elif hasattr(widget, "date"):
                data[field] = widget.date().toString("yyyy-MM-dd")

            # QCheckBox
            elif hasattr(widget, "isChecked"):
                data[field] = widget.isChecked()

        return data
