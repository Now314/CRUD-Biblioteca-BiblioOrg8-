from PySide6.QtWidgets import QMainWindow
from ui.ui_main import Ui_MainWindow
from services.api_client import get
from controllers.base_controller import BaseController

class MainController(QMainWindow, BaseController):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("BiblioOrg8")

        self.configure_table(self.ui.tableView)

        self.load_data()

        self.ui.tableView.selectionModel().selectionChanged.connect(
            self.on_row_selected
        )

    def load_data(self):

        data = get("/main/principal")

        if data is None:
            BaseController.show_error(
                self,
                "No se pudo obtener información del servidor."
            )
            return

        self.load_table(
            self.ui.tableView,
            data, hidden_columns="id"
        )

    def on_row_selected(self):

        data = self.get_selected_data(self.ui.tableView)

        if data is None:
            return

        self.load_fields(
            data,
            {
                "codigo": self.ui.codetxt,
                "libro": self.ui.booktxt,
                "autor": self.ui.authortxt,
                "clasificacion": self.ui.classificationtxt,
                "estante": self.ui.shelftxt,
                "fila": self.ui.rowtxt,
                "cantidad_total": self.ui.numbertxt,
                "stock": self.ui.stocktxt
            }
        )
