from PySide6.QtCore import QDate
from PySide6.QtGui import QIcon, QCloseEvent
from PySide6.QtWidgets import QMainWindow

from datetime import date

from controllers.utilities.fields_utility import FieldsUtility
from controllers.utilities.notifications_utility import NotificationsUtility
from controllers.windows_controllers.loans_controller import LoansController

from services.crud_service import CRUDService

from ui.ui_newloan import Ui_newloanWindow


class NewLoanController(QMainWindow):
    def __init__(self, manager, book_data):
        super().__init__()

        self.manager = manager
        self.book_data = book_data

        self.ui = Ui_newloanWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("New Loan|BiblioOrg8")
        self.setWindowIcon(QIcon(":/assets/logo/logo.png"))

        self.load_book_data()

        self.ui.addbtn.clicked.connect(self.add_loan)

        # ...

    def load_book_data(self):

        FieldsUtility.load_fields(
            self.book_data,
            {
                "codigo": self.ui.codetxt,
                "libro": self.ui.booktxt,
            },
        )

        self.ui.dateEdit.setDate(QDate.currentDate().addMonths(1))

    from datetime import date

    def add_loan(self):

    # Obtener datos y enviarlos a tabla prestamos.

        data = FieldsUtility.get_fields(
            {
                "codigo": self.ui.codetxt,
                "libro": self.ui.booktxt,
                "nombre": self.ui.nametxt,
                "apellidos": self.ui.lastnametxt,
                "fecha_devolucion": self.ui.dateEdit,
            }
        )

        fecha_salida = date.today()

        data["fecha_salida"] = fecha_salida.isoformat()
        data["fecha_devolucion"] = data["fecha_devolucion"].isoformat()

    # Cambiar stock en principal

        success = CRUDService.create("/post_table/prestamos", data)

        if success:
            NotificationsUtility.show_info(self, "Préstamo registrado correctamente.")

            self.manager.show(LoansController)

        else:
            NotificationsUtility.show_error(
                self, "No fue posible registrar el préstamo."
            )

    def closeEvent(self, event: QCloseEvent):
        self.manager.back()
        event.accept()
