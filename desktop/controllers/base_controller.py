from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMessageBox, QAbstractItemView


class BaseController:

    @staticmethod
    def create_model(data, hidden_columns=None):

        if hidden_columns is None:
            hidden_columns = []

        model = QStandardItemModel()

        keys = [
            key
            for key in data[0].keys()
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

        if not data:
            table_view.setModel(QStandardItemModel())
            return

        model = BaseController.create_model(
            data,
            hidden_columns
        )

        table_view.setModel(model)
        table_view.setProperty("table_data", data)

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

        data = table_view.property("table_data")

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
