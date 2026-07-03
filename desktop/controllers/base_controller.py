from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMessageBox

class BaseController:

    @staticmethod
    def load_table(table_view, data):
        """
        Llena un QTableView con una lista de diccionarios.

        Parameters
        ----------
        table_view : QTableView
            Tabla donde se mostrarán los datos.

        data : list[dict]
            Información obtenida desde la API.
        """

        # Si no hay datos, limpiar la tabla
        if not data:
            table_view.setModel(QStandardItemModel())
            return

        # Crear el modelo
        model = QStandardItemModel()

        # Encabezados
        headers = list(data[0].keys())
        model.setHorizontalHeaderLabels(headers)

        # Agregar filas
        for row in data:

            items = []

            for header in headers:
                value = row.get(header, "")
                items.append(QStandardItem(str(value)))

            model.appendRow(items)

        # Mostrar modelo
        table_view.setModel(model)

        # Ajustar columnas
        table_view.resizeColumnsToContents()

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
