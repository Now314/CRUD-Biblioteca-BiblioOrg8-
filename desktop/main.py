# ruff: noqa: F401
import sys

from PySide6.QtWidgets import QApplication

from manager.WindowManager import WindowManager

from controllers.windows_controllers.main_controller import MainController

import resources_rc


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("BiblioOrg8")
    app.setOrganizationName("BiblioOrg")

    manager = WindowManager()
    manager.start(MainController)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
