from PySide6.QtGui import QCloseEvent, QIcon
from PySide6.QtWidgets import QMainWindow

from controllers.utilities.notifications_utility import NotificationsUtility
from controllers.utilities.tables_controller import TablesController
from services.api_client import get
from ui.ui_history import Ui_HistoryWindow


class HistoryController(QMainWindow, TablesController):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager

        self.ui = Ui_HistoryWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/assets/logo/logo.png"))

        self.configure_table(self.ui.tableView)
        self.ui.searchtxt.textChanged.connect(self.search)
        self.ui.resetbtn.clicked.connect(self.clear_search)
        self.ui.closebtn.clicked.connect(self.close)

        self.load_data()

    def load_data(self):
        data = get("/get_table/historial")
        if data is None:
            NotificationsUtility.show_error(
                self, "No se pudo cargar el historial desde el servidor."
            )
            self.ui.statusbar.showMessage("No se pudo cargar el historial")
            return

        self.initialize_table(
            self.ui.tableView,
            data,
            hidden_columns=["id"],
        )
        self.ui.statusbar.showMessage(f"Préstamos archivados: {len(data)}")

    def search(self, text):
        self.filter_table(
            self.ui.tableView,
            text,
            hidden_columns=["id"],
        )
        model = self.ui.tableView.model()
        if model is not None:
            self.ui.statusbar.showMessage(
                f"Registros encontrados: {model.rowCount()}"
            )

    def clear_search(self):
        self.restore_table(
            self.ui.tableView,
            self.ui.searchtxt,
            hidden_columns=["id"],
        )
        data = self.ui.tableView.property("original_data") or []
        self.ui.statusbar.showMessage(f"Préstamos archivados: {len(data)}")

    def closeEvent(self, event: QCloseEvent):
        self.manager.back()
        event.accept()
