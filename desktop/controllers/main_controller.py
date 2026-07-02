from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMainWindow
from ui.ui_main import Ui_MainWindow
from services.api_client import get

class MainController(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialize()

    def initialize(self):
        self.setWindowTitle("BiblioOrg8")
        self.load_data()

    def load_data(self):

        data = get("/main/principal")
        if data is None:
            print("No se pudo obtener información del servidor.")
            return
        self.fill_table(data)

    def fill_table(self, data):
        """
        Llena el QTableView con los datos obtenidos desde la API.
        Parameters
        ----------
        data : list[dict]
            Lista de diccionarios devuelta por FastAPI.
        """

        # Si no hay datos, limpiar la tabla
        if not data:
            self.ui.tableView.setModel(QStandardItemModel())
            return

        # Crear un modelo vacío
        model = QStandardItemModel()

        # Crear encabezados usando las llaves del primer registro
        headers = list(data[0].keys())
        model.setHorizontalHeaderLabels(headers)

        # Agregar filas
        for row in data:

            items = []

            for header in headers:
                value = row.get(header, "")
                item = QStandardItem(str(value))
                items.append(item)

            model.appendRow(items)

        # Asignar el modelo al TableView
        self.ui.tableView.setModel(model)

        # Ajustar automáticamente el ancho de las columnas
        self.ui.tableView.resizeColumnsToContents()
