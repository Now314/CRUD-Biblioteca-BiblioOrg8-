from PySide6.QtCore import QDate
from PySide6.QtGui import QIcon, QCloseEvent
from PySide6.QtWidgets import QInputDialog, QMainWindow

from controllers.utilities.fields_utility import FieldsUtility
from controllers.utilities.notifications_utility import NotificationsUtility
from controllers.utilities.tables_controller import TablesController
from services.api_client import get
from services.crud_service import CRUDService
from ui.ui_loans import Ui_LoansWindow


class LoansController(QMainWindow, TablesController):
    def __init__(self, manager, book_data=None):
        super().__init__()
        self.manager = manager
        self.book_data = book_data
        self._creating_new = False

        self.ui = Ui_LoansWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Préstamos | BiblioOrg8")
        self.setWindowIcon(QIcon(":/assets/logo/logo.png"))

        self.configure_table(self.ui.tableView)
        self.ui.codetxt.setReadOnly(True)
        self.ui.booktxt.setReadOnly(True)

        self.ui.searchtxt.textChanged.connect(self.search)
        self.ui.resetbtn.clicked.connect(self.clear_search)
        self.ui.newbtn.clicked.connect(self.new_register)
        self.ui.addbtn.clicked.connect(self.add_loan)
        self.ui.editbtn.clicked.connect(self.edit_loan)
        self.ui.deletbtn.clicked.connect(self.delete_loan)

        self.load_data()

    def load_data(self):
        data = get("/get_table/prestamos")

        if data is None:
            NotificationsUtility.show_error(
                self, "No se pudieron obtener los préstamos del servidor."
            )
            return

        self.initialize_table(
            self.ui.tableView,
            data,
            callback=self.on_row_selected,
            hidden_columns=["id"],
        )

        if self.ui.tableView.model().rowCount():
            self.ui.tableView.selectRow(0)
        else:
            self.clear_form()

    def on_row_selected(self, *_):
        data = self.get_selected_data(self.ui.tableView)
        if data is None:
            return

        self._creating_new = False
        FieldsUtility.load_fields(
            data,
            {
                "codigo": self.ui.codetxt,
                "libro": self.ui.booktxt,
                "nombre": self.ui.nametxt,
                "apellidos": self.ui.lastnametxt,
                "fecha_salida": self.ui.departuredateEdit,
                "fecha_devolucion": self.ui.dateEdit,
            },
        )

    def search(self, text):
        self.filter_table(
            self.ui.tableView,
            text,
            callback=self.on_row_selected,
            hidden_columns=["id"],
        )

    def clear_search(self):
        self.restore_table(
            self.ui.tableView,
            self.ui.searchtxt,
            callback=self.on_row_selected,
            hidden_columns=["id"],
        )

    def clear_form(self):
        self.ui.codetxt.clear()
        self.ui.booktxt.clear()
        self.ui.nametxt.clear()
        self.ui.lastnametxt.clear()
        self.ui.departuredateEdit.setDate(QDate.currentDate())
        self.ui.dateEdit.setDate(QDate.currentDate().addMonths(1))

    def new_register(self):
        catalog = get("/get_table/principal")
        if catalog is None:
            NotificationsUtility.show_error(
                self, "No se pudo cargar el catálogo para seleccionar un libro."
            )
            return

        available_books = [
            book
            for book in catalog
            if self._stock_value(book.get("stock")) > 0
        ]
        if not available_books:
            NotificationsUtility.show_warning(
                self, "No hay libros con stock disponible para prestar."
            )
            return

        labels = [
            f"{book.get('codigo', '')} — {book.get('libro', '')} "
            f"(stock: {book.get('stock', 0)})"
            for book in available_books
        ]
        selection, accepted = QInputDialog.getItem(
            self,
            "Nuevo préstamo",
            "Seleccione el libro:",
            labels,
            0,
            False,
        )
        if not accepted:
            return

        book = available_books[labels.index(selection)]
        self.ui.tableView.clearSelection()
        self.clear_form()
        FieldsUtility.load_fields(
            book,
            {"codigo": self.ui.codetxt, "libro": self.ui.booktxt},
        )
        self._creating_new = True

    @staticmethod
    def _stock_value(value) -> int:
        try:
            return int(value or 0)
        except (TypeError, ValueError):
            return 0

    def _loan_form_data(self) -> dict | None:
        data = FieldsUtility.get_fields(
            {
                "codigo": self.ui.codetxt,
                "libro": self.ui.booktxt,
                "nombre": self.ui.nametxt,
                "apellidos": self.ui.lastnametxt,
                "fecha_salida": self.ui.departuredateEdit,
                "fecha_devolucion": self.ui.dateEdit,
            }
        )

        required_text = ("codigo", "libro", "nombre", "apellidos")
        if any(not data[field] for field in required_text):
            NotificationsUtility.show_warning(
                self, "Complete el libro y los datos de la persona."
            )
            return None

        if data["fecha_devolucion"] < data["fecha_salida"]:
            NotificationsUtility.show_warning(
                self, "La fecha de devolución no puede ser anterior a la salida."
            )
            return None

        data["fecha_salida"] = data["fecha_salida"].isoformat()
        data["fecha_devolucion"] = data["fecha_devolucion"].isoformat()
        return data

    def add_loan(self):
        if not self._creating_new:
            NotificationsUtility.show_warning(
                self, "Presione 'Nuevo Registro' y seleccione un libro primero."
            )
            return

        data = self._loan_form_data()
        if data is None:
            return

        if CRUDService.create("/post_table/prestamos", data):
            NotificationsUtility.show_info(self, "Préstamo registrado correctamente.")
            self._creating_new = False
            self.load_data()
        else:
            NotificationsUtility.show_error(
                self,
                "No se pudo registrar el préstamo. Compruebe el stock disponible "
                "y la conexión con el servidor.",
            )

    def edit_loan(self):
        selected = self.get_selected_data(self.ui.tableView)
        if selected is None:
            NotificationsUtility.show_warning(
                self, "Seleccione el préstamo que desea editar."
            )
            return

        data = self._loan_form_data()
        if data is None:
            return

        # El código y el título identifican el préstamo y se mantienen fijos;
        # editar esos valores requeriría ajustar el stock de ambos libros.
        editable_data = {
            key: data[key]
            for key in ("nombre", "apellidos", "fecha_salida", "fecha_devolucion")
        }
        endpoint = f"/put_table/prestamos?register_id={selected['id']}"

        if CRUDService.update(endpoint, editable_data):
            NotificationsUtility.show_info(self, "Préstamo actualizado correctamente.")
            self.load_data()
        else:
            NotificationsUtility.show_error(
                self, "No se pudo actualizar el préstamo."
            )

    def delete_loan(self):
        selected = self.get_selected_data(self.ui.tableView)
        if selected is None:
            NotificationsUtility.show_warning(
                self, "Seleccione el préstamo que desea eliminar."
            )
            return

        confirmed = NotificationsUtility.confirm(
            self,
            "¿Eliminar este préstamo? Se devolverá una unidad al stock del libro.",
        )
        if not confirmed:
            return

        endpoint = f"/delete_table/prestamos/{selected['id']}"
        if CRUDService.delete(endpoint):
            NotificationsUtility.show_info(
                self, "Préstamo eliminado y stock actualizado correctamente."
            )
            self.load_data()
        else:
            NotificationsUtility.show_error(
                self, "No se pudo eliminar el préstamo ni modificar el stock."
            )

    def closeEvent(self, event: QCloseEvent):
        self.manager.back()
        event.accept()
