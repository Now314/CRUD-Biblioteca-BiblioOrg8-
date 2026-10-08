"""Interfaz de la ventana de historial de préstamos."""

from PySide6.QtCore import QCoreApplication, QSize
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QStatusBar,
    QTableView,
    QVBoxLayout,
    QWidget,
)


class Ui_HistoryWindow(object):
    def setupUi(self, HistoryWindow):
        HistoryWindow.setObjectName("HistoryWindow")
        HistoryWindow.resize(900, 580)
        HistoryWindow.setMinimumSize(QSize(760, 480))

        self.centralwidget = QWidget(HistoryWindow)
        self.verticalLayout = QVBoxLayout(self.centralwidget)

        self.titlelabel = QLabel(self.centralwidget)
        self.titlelabel.setObjectName("titlelabel")
        self.verticalLayout.addWidget(self.titlelabel)

        self.searchLayout = QHBoxLayout()
        self.searchtxt = QLineEdit(self.centralwidget)
        self.searchtxt.setObjectName("searchtxt")
        self.searchLayout.addWidget(self.searchtxt)

        self.resetbtn = QPushButton(self.centralwidget)
        self.resetbtn.setObjectName("resetbtn")
        self.searchLayout.addWidget(self.resetbtn)
        self.verticalLayout.addLayout(self.searchLayout)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        self.closebtn = QPushButton(self.centralwidget)
        self.closebtn.setObjectName("closebtn")
        self.verticalLayout.addWidget(self.closebtn)

        HistoryWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(HistoryWindow)
        self.statusbar.setObjectName("statusbar")
        HistoryWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HistoryWindow)

    def retranslateUi(self, HistoryWindow):
        HistoryWindow.setWindowTitle(
            QCoreApplication.translate(
                "HistoryWindow", "BiblioOrg | Historial de préstamos", None
            )
        )
        self.titlelabel.setText(
            QCoreApplication.translate(
                "HistoryWindow", "Historial de préstamos", None
            )
        )
        self.searchtxt.setPlaceholderText(
            QCoreApplication.translate(
                "HistoryWindow", "Buscar por libro, código o persona...", None
            )
        )
        self.resetbtn.setText(QCoreApplication.translate("HistoryWindow", "X", None))
        self.closebtn.setText(
            QCoreApplication.translate("HistoryWindow", "Volver", None)
        )
