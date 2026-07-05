from controllers.main_controller import MainController
from controllers.admin_controller import AdminController
from controllers.lstlecturas_controller import LstLecturasController


class WindowManager:

    def __init__(self):
        self.window = None

    def show_main(self):
        if self.window:
            self.window.close()

        self.window = MainController(self)
        self.window.show()

    def show_admin(self):
        if self.window:
            self.window.close()

        self.window = AdminController(self)
        self.window.show()

    def show_lstlecturas(self):
        if self.window:
            self.window.close()

        self.window = LstLecturasController(self)
        self.window.show()
