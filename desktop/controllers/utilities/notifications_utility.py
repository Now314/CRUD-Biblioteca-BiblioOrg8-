from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox


class NotificationsUtility(QObject):
    @staticmethod
    def show_error(self, message: str):
        QMessageBox.critical(self, "Error", message)

    @staticmethod
    def show_warning(self, message: str):
        QMessageBox.warning(self, "Advertencia", message)

    @staticmethod
    def show_info(self, message: str):
        QMessageBox.information(self, "Información", message)

    @staticmethod
    def confirm(self, message: str) -> bool:
        response = QMessageBox.question(
            self,
            "Confirmación",
            message,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )

        return response == QMessageBox.StandardButton.Yes
