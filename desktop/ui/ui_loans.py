# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loans.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
)
from PySide6.QtGui import (
    QFont,
)
from PySide6.QtWidgets import (
    QDateEdit,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMenuBar,
    QPushButton,
    QStatusBar,
    QTableView,
    QVBoxLayout,
    QWidget,
)


class Ui_LoansWindow(object):
    def setupUi(self, LoansWindow):
        if not LoansWindow.objectName():
            LoansWindow.setObjectName("LoansWindow")
        LoansWindow.resize(873, 563)
        self.centralwidget = QWidget(LoansWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.tableView.setGeometry(QRect(10, 40, 481, 411))
        self.searchtxt = QLineEdit(self.centralwidget)
        self.searchtxt.setObjectName("searchtxt")
        self.searchtxt.setGeometry(QRect(10, 10, 771, 26))
        self.resetbtn = QPushButton(self.centralwidget)
        self.resetbtn.setObjectName("resetbtn")
        self.resetbtn.setGeometry(QRect(780, 10, 81, 26))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setGeometry(QRect(500, 430, 361, 71))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(500, 50, 361, 371))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.codelabel = QLabel(self.widget)
        self.codelabel.setObjectName("codelabel")
        font = QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.codelabel.setFont(font)

        self.verticalLayout.addWidget(self.codelabel)

        self.codetxt = QLineEdit(self.widget)
        self.codetxt.setObjectName("codetxt")

        self.verticalLayout.addWidget(self.codetxt)

        self.booklabel = QLabel(self.widget)
        self.booklabel.setObjectName("booklabel")
        self.booklabel.setFont(font)

        self.verticalLayout.addWidget(self.booklabel)

        self.booktxt = QLineEdit(self.widget)
        self.booktxt.setObjectName("booktxt")

        self.verticalLayout.addWidget(self.booktxt)

        self.namelabel = QLabel(self.widget)
        self.namelabel.setObjectName("namelabel")
        self.namelabel.setFont(font)

        self.verticalLayout.addWidget(self.namelabel)

        self.nametxt = QLineEdit(self.widget)
        self.nametxt.setObjectName("nametxt")

        self.verticalLayout.addWidget(self.nametxt)

        self.lastnamelabel = QLabel(self.widget)
        self.lastnamelabel.setObjectName("lastnamelabel")
        self.lastnamelabel.setFont(font)

        self.verticalLayout.addWidget(self.lastnamelabel)

        self.lastnametxt = QLineEdit(self.widget)
        self.lastnametxt.setObjectName("lastnametxt")

        self.verticalLayout.addWidget(self.lastnametxt)

        self.departuredatelabel = QLabel(self.widget)
        self.departuredatelabel.setObjectName("departuredatelabel")
        self.departuredatelabel.setFont(font)

        self.verticalLayout.addWidget(self.departuredatelabel)

        self.departuredateEdit = QDateEdit(self.widget)
        self.departuredateEdit.setObjectName("departuredateEdit")
        font1 = QFont()
        font1.setPointSize(11)
        self.departuredateEdit.setFont(font1)

        self.verticalLayout.addWidget(self.departuredateEdit)

        self.datelabel = QLabel(self.widget)
        self.datelabel.setObjectName("datelabel")
        self.datelabel.setFont(font)

        self.verticalLayout.addWidget(self.datelabel)

        self.dateEdit = QDateEdit(self.widget)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setFont(font1)

        self.verticalLayout.addWidget(self.dateEdit)

        self.Historybtn = QPushButton(self.widget)
        self.Historybtn.setObjectName("Historybtn")

        self.verticalLayout.addWidget(self.Historybtn)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName("widget1")
        self.widget1.setGeometry(QRect(10, 460, 481, 41))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.newbtn = QPushButton(self.widget1)
        self.newbtn.setObjectName("newbtn")

        self.horizontalLayout.addWidget(self.newbtn)

        self.addbtn = QPushButton(self.widget1)
        self.addbtn.setObjectName("addbtn")

        self.horizontalLayout.addWidget(self.addbtn)

        self.editbtn = QPushButton(self.widget1)
        self.editbtn.setObjectName("editbtn")

        self.horizontalLayout.addWidget(self.editbtn)

        self.deletbtn = QPushButton(self.widget1)
        self.deletbtn.setObjectName("deletbtn")

        self.horizontalLayout.addWidget(self.deletbtn)

        LoansWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LoansWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 873, 33))
        LoansWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LoansWindow)
        self.statusbar.setObjectName("statusbar")
        LoansWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoansWindow)

        QMetaObject.connectSlotsByName(LoansWindow)

    # setupUi

    def retranslateUi(self, LoansWindow):
        LoansWindow.setWindowTitle(
            QCoreApplication.translate("LoansWindow", "BiblioOrg | Prestamos", None)
        )
        self.resetbtn.setText(QCoreApplication.translate("LoansWindow", "X", None))
        self.codelabel.setText(
            QCoreApplication.translate("LoansWindow", "C\u00f3digo", None)
        )
        self.booklabel.setText(QCoreApplication.translate("LoansWindow", "Libro", None))
        self.namelabel.setText(
            QCoreApplication.translate("LoansWindow", "Nombre", None)
        )
        self.lastnamelabel.setText(
            QCoreApplication.translate("LoansWindow", "Apellido", None)
        )
        self.departuredatelabel.setText(
            QCoreApplication.translate("LoansWindow", "Fecha de Salida", None)
        )
        self.datelabel.setText(
            QCoreApplication.translate("LoansWindow", "Fecha de Devoluci\u00f3n", None)
        )
        self.Historybtn.setText(
            QCoreApplication.translate("LoansWindow", "Historial", None)
        )
        self.newbtn.setText(
            QCoreApplication.translate("LoansWindow", "Nuevo Registro", None)
        )
        self.addbtn.setText(
            QCoreApplication.translate("LoansWindow", "A\u00f1adir", None)
        )
        self.editbtn.setText(QCoreApplication.translate("LoansWindow", "Editar", None))
        self.deletbtn.setText(
            QCoreApplication.translate("LoansWindow", "Eliminar", None)
        )

    # retranslateUi
