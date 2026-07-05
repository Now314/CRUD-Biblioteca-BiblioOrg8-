from PySide6.QtWidgets import QMainWindow
from ui.ui_main import Ui_MainWindow
from services.api_client import get
from controllers.base_controller import BaseController

class MainController(QMainWindow, BaseController):

    def __init__(self, manager):
        super().__init__()

        self.manager = manager

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("BiblioOrg8")

        self.configure_table(self.ui.tableView)

        self.ui.searchtxt.textChanged.connect(self.search)

        self.load_data()

        self.ui.tableView.selectionModel().selectionChanged.connect(
            self.on_row_selected
        )

        self.ui.resetbtn.clicked.connect(self.clear_search)

        self.admin_window = None

        self.ui.actionPanel_de_Admin.triggered.connect(self.go_admin)

        self.ui.actionPanel_Lista_de_Lecturas.triggered.connect(self.go_lstlecturas)


    def connect_table(self):
        self.ui.tableView.selectionModel().selectionChanged.connect(
            self.on_row_selected
        )

        if self.ui.tableView.model().rowCount() > 0:
            self.ui.tableView.selectRow(0)

    def load_data(self):

        data = get("/main/principal")

        if data is None:
            self.show_error(self,"No se pudo obtener información del servidor.")
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
                "autor": self.ui.authortxt,
                "clasificacion": self.ui.classificationtxt,
                "estante": self.ui.shelftxt,
                "fila": self.ui.rowtxt,
                "cantidad_total": self.ui.numbertxt,
                "stock": self.ui.stocktxt
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

    def go_admin(self):
        self.manager.show_admin()

    def go_lstlecturas(self):
        self.manager.show_lstlecturas()