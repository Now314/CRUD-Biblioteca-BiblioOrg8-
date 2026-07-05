import sys
from PySide6.QtWidgets import QApplication
from manager.WindowManager import WindowManager


def main():

    app = QApplication(sys.argv)

    manager = WindowManager()

    manager.show_main()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()