from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow

from controllers.windows_controllers.admin_controller import AdminController
from controllers.windows_controllers.lstlecturas_controller import LstLecturasController
from controllers.utilities.tables_controller import TablesController
from controllers.utilities.fields_utility import FieldsUtility
from controllers.utilities.notifications_utility import NotificationsUtility

from services.api_client import get

from ui.ui_main import Ui_MainWindow


class MainController(QMainWindow, TablesController):
    def __init__(self, manager):
        super().__init__()

        self.manager = manager
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("BiblioOrg8")
        self.setWindowIcon(QIcon(":/assets/logo/logo.png"))

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

    def load_data(self):

        data = get("/tables/principal")

        if data is None:
            NotificationsUtility.show_error(
                self, "No se pudo obtener información del servidor."
            )
            return

        self.initialize_table(
            self.ui.tableView, data, self.on_row_selected, hidden_columns=["id"]
        )

    def on_row_selected(self):

        data = self.get_selected_data(self.ui.tableView)

        if data is None:
            return

        FieldsUtility.load_fields(
            data,
            {
                "codigo": self.ui.codetxt,
                "libro": self.ui.booktxt,
                "autor": self.ui.authortxt,
                "clasificacion": self.ui.classificationtxt,
                "estante": self.ui.shelftxt,
                "fila": self.ui.rowtxt,
                "cantidad_total": self.ui.numbertxt,
                "stock": self.ui.stocktxt,
            },
        )

    def search(self, text):

        self.filter_table(
            self.ui.tableView, text, self.on_row_selected, hidden_columns=["id"]
        )

    def clear_search(self):

        self.restore_table(
            self.ui.tableView,
            self.ui.searchtxt,
            self.on_row_selected,
            hidden_columns=["id"],
        )

    def go_admin(self):
        self.manager.show(AdminController)

    def go_lstlecturas(self):
        self.manager.show(LstLecturasController)
