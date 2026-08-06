from PySide6.QtGui import QIcon, QCloseEvent
from PySide6.QtWidgets import QMainWindow

from controllers.utilities.tables_controller import TablesController
from controllers.utilities.notifications_utility import NotificationsUtility
from controllers.utilities.fields_utility import FieldsUtility

from services.api_client import get

from ui.ui_loans import Ui_LoansWindow


class LoansController(QMainWindow, TablesController):
    def __init__(self, manager, book_data=None):

        super().__init__()
        self.manager = manager
        self.book_data = book_data

        self.ui = Ui_LoansWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Prestamos|BiblioOrg8")
        self.setWindowIcon(QIcon(":/assets/logo/logo.png"))

        self.configure_table(self.ui.tableView)

        self.ui.searchtxt.textChanged.connect(self.search)

        self.load_data()

        self.ui.tableView.selectionModel().selectionChanged.connect(
            self.on_row_selected
        )


        self.ui.resetbtn.clicked.connect(self.clear_search)

        # ...

    def load_data(self):

        data = get("/get_table/prestamos")

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
                "nombre": self.ui.nametxt,
                "apellido": self.ui.lastnametxt,
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

    def new_register(self):
        return None

    def closeEvent(self, event: QCloseEvent):
        self.manager.back()
        event.accept()
