from PySide6.QtGui import QIcon, QCloseEvent
from PySide6.QtWidgets import QMainWindow

from controllers.utilities.fields_utility import FieldsUtility
from controllers.utilities.tables_controller import TablesController
from controllers.utilities.notifications_utility import NotificationsUtility
from controllers.windows_controllers.loans_controller import LoansController
from controllers.windows_controllers.newloan_controller import NewLoanController

from services.api_client import get

from ui.ui_admin import Ui_AdminWindow


class AdminController(QMainWindow, TablesController):
    def __init__(self, manager):
        super().__init__()

        self.manager = manager

        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Admin|BiblioOrg8")
        self.setWindowIcon(QIcon(":/assets/logo/logo.png"))

        self.configure_table(self.ui.tableView)

        self.ui.searchtxt.textChanged.connect(self.search)

        self.load_data()

        self.ui.tableView.selectionModel().selectionChanged.connect(
            self.on_row_selected
        )

        self.ui.resetbtn.clicked.connect(self.clear_search)
        self.ui.loansbtn.clicked.connect(self.go_loans)
        self.ui.newrequestbtn.clicked.connect(self.go_new_loan)

        # ...

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

    def go_new_loan(self):

        data = self.get_selected_data(self.ui.tableView)

        if data is None:
            NotificationsUtility.show_warning(self, "Seleccione un libro, por favor.")
            return

        self.manager.send_data(NewLoanController, data)

    def go_loans(self):
        self.manager.show(LoansController)

    def closeEvent(self, event: QCloseEvent):
        self.manager.back()
        event.accept()
