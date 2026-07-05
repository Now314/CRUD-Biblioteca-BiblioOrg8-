from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMessageBox, QAbstractItemView
import unicodedata

class BaseController:

    @staticmethod
    def create_model(data, columns=None, hidden_columns=None):

        if hidden_columns is None:
            hidden_columns = []

        model = QStandardItemModel()

        # Si no se reciben columnas, obtenerlas del primer registro
        if columns is None:
            columns = list(data[0].keys())

        # Mantener el orden original y ocultar las necesarias
        keys = [
            key
            for key in columns
            if key not in hidden_columns
        ]

        headers = [
            key.replace("_", " ").title()
            for key in keys
        ]

        model.setHorizontalHeaderLabels(headers)

        for row in data:

            items = []

            for key in keys:
                items.append(
                    QStandardItem(str(row.get(key, "")))
                )

            model.appendRow(items)

        return model

    @staticmethod
    def load_table(table_view, data, hidden_columns=None):

        if hidden_columns is None:
            hidden_columns = []

        if not data:
            table_view.setModel(QStandardItemModel())
            table_view.setProperty("current_data", [])
            return

        columns = table_view.property("table_columns")

        model = BaseController.create_model(
            data,
            columns,
            hidden_columns
        )

        table_view.setModel(model)

        table_view.setProperty(
            "current_data",
            data
        )

    @staticmethod
    def configure_table(table_view):

        table_view.verticalHeader().setVisible(False)

        table_view.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        table_view.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        table_view.setAlternatingRowColors(True)

        table_view.resizeColumnsToContents()

        table_view.horizontalHeader().setStretchLastSection(True)

    @staticmethod
    def get_selected_data(table_view) -> dict | None:

        indexes = table_view.selectionModel().selectedRows()

        if not indexes:
            return None

        row = indexes[0].row()

        data = table_view.property("current_data")

        if data is None:
            return None

        return data[row]

    @staticmethod
    def load_fields(data: dict, fields: dict):
        """
        Carga información de un diccionario en widgets compatibles con setText().
        """

        for field, widget in fields.items():

            if hasattr(widget, "setText"):
                value = data.get(field, "")
                widget.setText("" if value is None else str(value))

    @staticmethod
    def get_fields(fields: dict) -> dict:

        data = {}

        for field, widget in fields.items():

            if hasattr(widget, "text"):
                data[field] = widget.text().strip()

            elif hasattr(widget, "currentText"):
                data[field] = widget.currentText()

            elif hasattr(widget, "value"):
                data[field] = widget.value()

        return data

    @staticmethod
    def filter_table(table_view, text, hidden_columns=None):
        """
        Filtra la información de un QTableView buscando en todas
        las columnas sin distinguir mayúsculas ni tildes.
        """

        data = table_view.property("original_data")

        if data is None:
            return

        search = BaseController.normalize(text)

        # Si el usuario borró el texto,
        # volver a mostrar toda la tabla.
        if not search:
            BaseController.load_table(
                table_view,
                data,
                hidden_columns
            )
            return

        filtered = []

        for row in data:

            for value in row.values():

                value = BaseController.normalize(value)

                if search in value:
                    filtered.append(row)
                    break

        BaseController.load_table(
            table_view,
            filtered,
            hidden_columns
        )

    @staticmethod
    def normalize(text: str) -> str:
        """
        Convierte un texto a una versión normalizada:
        - Sin tildes.
        - En minúsculas.
        """

        text = str(text).strip().lower()

        return "".join(
            char
            for char in unicodedata.normalize("NFD", text)
            if unicodedata.category(char) != "Mn"
        )

    @staticmethod
    def reset_table(table_view, search_box, hidden_columns=None):
        """
        Restaura la tabla a su estado original y limpia el buscador.
        """

        if hidden_columns is None:
            hidden_columns = []

        # Limpiar el buscador
        search_box.clear()

        # Recuperar los datos originales
        data = table_view.property("original_data")

        if data is None:
            return

        # Volver a cargar la tabla
        BaseController.load_table(
            table_view,
            data,
            hidden_columns
        )

    @staticmethod
    def show_error(self, message: str):
        QMessageBox.critical(
            self,
            "Error",
            message
        )

    @staticmethod
    def show_warning(self, message: str):
        QMessageBox.warning(
            self,
            "Advertencia",
            message
        )

    @staticmethod
    def show_info(self, message: str):
        QMessageBox.information(
            self,
            "Información",
            message
        )

    @staticmethod
    def confirm(self, message: str) -> bool:
        response = QMessageBox.question(
            self,
            "Confirmación",
            message,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        return response == QMessageBox.StandardButton.Yes
