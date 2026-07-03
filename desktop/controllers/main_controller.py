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
        self.load_data()

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
            data
        )
