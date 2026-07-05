from PySide6.QtWidgets import QMainWindow
from controllers.base_controller import BaseController
from ui.ui_admin import Ui_AdminWindow


class AdminController(QMainWindow, BaseController):

    def __init__(self, manager):
        super().__init__()

        self.manager = manager

        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Admin | BiblioOrg8")

