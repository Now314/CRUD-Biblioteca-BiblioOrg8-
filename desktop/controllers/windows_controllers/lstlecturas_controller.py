from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMainWindow

from controllers.utilities.tables_controller import TablesController

from ui.ui_lstlecturas import Ui_LstLecturasWindow


class LstLecturasController(QMainWindow, TablesController):
    def __init__(self, manager):
        super().__init__()

        self.manager = manager

        self.ui = Ui_LstLecturasWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Lista de Lecturas | BiblioOrg8")

        # ...

    def closeEvent(self, event: QCloseEvent):
        self.manager.back()
        event.accept()
