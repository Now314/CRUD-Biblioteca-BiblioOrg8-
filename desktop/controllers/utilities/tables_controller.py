import unicodedata

from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QAbstractItemView


class TablesController:
    @staticmethod
    def build_model(data, columns=None, hidden_columns=None):

        if hidden_columns is None:
            hidden_columns = []

        model = QStandardItemModel()

        # Si no se reciben columnas, intentar obtenerlas de los datos
        if columns is None:
            if data:
                columns = list(data[0].keys())
            else:
                columns = []

        # Mantener el orden original y ocultar columnas
        keys = [key for key in columns if key not in hidden_columns]

        headers = [key.replace("_", " ").title() for key in keys]

        model.setHorizontalHeaderLabels(headers)

        # Agregar filas (si existen)
        for row in data:
            items = []

            for key in keys:
                items.append(QStandardItem(str(row.get(key, ""))))

            model.appendRow(items)

        return model

    @staticmethod
    def populate_table(table_view, data, callback=None, hidden_columns=None):

        if hidden_columns is None:
            hidden_columns = []

        if data is None:
            data = []

        columns = table_view.property("table_columns")

        model = TablesController.build_model(data, columns, hidden_columns)

        table_view.setModel(model)

        table_view.setProperty("current_data", data)

        if callback is not None:
            table_view.selectionModel().selectionChanged.connect(callback)

            if model.rowCount() > 0:
                table_view.selectRow(0)

    @staticmethod
    def configure_table(table_view):

        table_view.verticalHeader().setVisible(False)

        table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        table_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        table_view.setAlternatingRowColors(True)

        table_view.resizeColumnsToContents()

        table_view.horizontalHeader().setStretchLastSection(True)

    @staticmethod
    def initialize_table(table_view, data, callback=None, hidden_columns=None):

        if hidden_columns is None:
            hidden_columns = []

        if data is None:
            data = []

        table_view.setProperty("original_data", data)

        # Solo obtener columnas si existen datos
        if data:
            columns = list(data[0].keys())
        else:
            # Si ya existían columnas (por ejemplo tras recargar), conservarlas
            columns = table_view.property("table_columns") or []

        table_view.setProperty("table_columns", columns)

        TablesController.populate_table(table_view, data, callback, hidden_columns)

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
    def filter_table(table_view, text, callback=None, hidden_columns=None):
        """
        Filtra la información de un QTableView buscando en todas
        las columnas sin distinguir mayúsculas ni tildes.
        """

        data = table_view.property("original_data")

        if data is None:
            return

        search = TablesController.normalize(text)

        # Si el usuario borró el texto,
        # volver a mostrar toda la tabla.
        if not search:
            TablesController.populate_table(table_view, data, callback, hidden_columns)
            return

        filtered = []

        for row in data:
            for value in row.values():
                value = TablesController.normalize(value)

                if search in value:
                    filtered.append(row)
                    break

        TablesController.populate_table(table_view, filtered, callback, hidden_columns)

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
    def restore_table(table_view, search_box, callback=None, hidden_columns=None):
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
        TablesController.populate_table(table_view, data, callback, hidden_columns)
