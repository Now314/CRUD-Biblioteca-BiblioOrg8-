from ui.ui_loans import Ui_LoansWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow
from controllers.base_controller import BaseController
from services.api_client import get


class LoansController(QMainWindow, BaseController):

    def __init__(self, manager):
        super().__init__()
        self.manager = manager

        self.ui = Ui_LoansWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Prestamos|BiblioOrg8")
        self.setWindowIcon(
            QIcon(":/assets/logo/logo.png")
        )

        self.configure_table(self.ui.tableView)

        self.ui.searchtxt.textChanged.connect(self.search)

        self.load_data()

        self.ui.tableView.selectionModel().selectionChanged.connect(
            self.on_row_selected
        )

        self.ui.resetbtn.clicked.connect(self.clear_search)

    def connect_table(self):
        self.ui.tableView.selectionModel().selectionChanged.connect(
            self.on_row_selected
        )

        if self.ui.tableView.model().rowCount() > 0:
            self.ui.tableView.selectRow(0)

    def load_data(self):

        data = get("/tables/prestamos")

        if data is None:
            self.show_error(self, "No se pudo obtener información del servidor.")
            return

        self.ui.tableView.setProperty(
            "original_data",
            data
        )

        self.ui.tableView.setProperty(
            "table_columns",
            list(data[0].keys())
        )

        self.load_table(
            self.ui.tableView,
            data,
            hidden_columns=["id"]
        )

        self.connect_table()

    def on_row_selected(self):

        data = self.get_selected_data(self.ui.tableView)

        if data is None:
            return

        self.load_fields(
            data,
            {
                "codigo": self.ui.codetxt,
                "libro": self.ui.booktxt,
                "nombre": self.ui.nametxt,
                "apellido": self.ui.lastnametxt,
            }
        )

    def search(self, text):

        self.filter_table(
            self.ui.tableView,
            text,
            hidden_columns=["id"]
        )

        self.connect_table()

    def clear_search(self):

        self.reset_table(
            self.ui.tableView,
            self.ui.searchtxt,
            hidden_columns=["id"]
        )

        self.connect_table()