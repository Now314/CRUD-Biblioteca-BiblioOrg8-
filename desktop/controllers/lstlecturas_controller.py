from PySide6.QtWidgets import QMainWindow
from controllers.base_controller import BaseController
from ui.ui_lstlecturas import Ui_LstLecturasWindow


class LstLecturasController(QMainWindow, BaseController):

    def __init__(self, manager):
        super().__init__()

        self.manager = manager

        self.ui = Ui_LstLecturasWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Lista de Lecturas | BiblioOrg8")