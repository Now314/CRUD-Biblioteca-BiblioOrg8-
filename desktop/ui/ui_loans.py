# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loans.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_LoansWindow(object):
    def setupUi(self, LoansWindow):
        if not LoansWindow.objectName():
            LoansWindow.setObjectName(u"LoansWindow")
        LoansWindow.resize(873, 563)
        self.centralwidget = QWidget(LoansWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 40, 481, 411))
        self.searchtxt = QLineEdit(self.centralwidget)
        self.searchtxt.setObjectName(u"searchtxt")
        self.searchtxt.setGeometry(QRect(10, 10, 771, 26))
        self.resetbtn = QPushButton(self.centralwidget)
        self.resetbtn.setObjectName(u"resetbtn")
        self.resetbtn.setGeometry(QRect(780, 10, 81, 26))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(500, 430, 361, 71))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(500, 50, 361, 371))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.codelabel = QLabel(self.widget)
        self.codelabel.setObjectName(u"codelabel")
        font = QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.codelabel.setFont(font)

        self.verticalLayout.addWidget(self.codelabel)

        self.codetxt = QLineEdit(self.widget)
        self.codetxt.setObjectName(u"codetxt")

        self.verticalLayout.addWidget(self.codetxt)

        self.booklabel = QLabel(self.widget)
        self.booklabel.setObjectName(u"booklabel")
        self.booklabel.setFont(font)

        self.verticalLayout.addWidget(self.booklabel)

        self.booktxt = QLineEdit(self.widget)
        self.booktxt.setObjectName(u"booktxt")

        self.verticalLayout.addWidget(self.booktxt)

        self.namelabel = QLabel(self.widget)
        self.namelabel.setObjectName(u"namelabel")
        self.namelabel.setFont(font)

        self.verticalLayout.addWidget(self.namelabel)

        self.nametxt = QLineEdit(self.widget)
        self.nametxt.setObjectName(u"nametxt")

        self.verticalLayout.addWidget(self.nametxt)

        self.lastnamelabel = QLabel(self.widget)
        self.lastnamelabel.setObjectName(u"lastnamelabel")
        self.lastnamelabel.setFont(font)

        self.verticalLayout.addWidget(self.lastnamelabel)

        self.lastnametxt = QLineEdit(self.widget)
        self.lastnametxt.setObjectName(u"lastnametxt")

        self.verticalLayout.addWidget(self.lastnametxt)

        self.departuredatelabel = QLabel(self.widget)
        self.departuredatelabel.setObjectName(u"departuredatelabel")
        self.departuredatelabel.setFont(font)

        self.verticalLayout.addWidget(self.departuredatelabel)

        self.departuredateEdit = QDateEdit(self.widget)
        self.departuredateEdit.setObjectName(u"departuredateEdit")
        font1 = QFont()
        font1.setPointSize(11)
        self.departuredateEdit.setFont(font1)

        self.verticalLayout.addWidget(self.departuredateEdit)

        self.datelabel = QLabel(self.widget)
        self.datelabel.setObjectName(u"datelabel")
        self.datelabel.setFont(font)

        self.verticalLayout.addWidget(self.datelabel)

        self.dateEdit = QDateEdit(self.widget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setFont(font1)

        self.verticalLayout.addWidget(self.dateEdit)

        self.Historybtn = QPushButton(self.widget)
        self.Historybtn.setObjectName(u"Historybtn")

        self.verticalLayout.addWidget(self.Historybtn)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 460, 481, 41))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.newbtn = QPushButton(self.widget1)
        self.newbtn.setObjectName(u"newbtn")

        self.horizontalLayout.addWidget(self.newbtn)

        self.addbtn = QPushButton(self.widget1)
        self.addbtn.setObjectName(u"addbtn")

        self.horizontalLayout.addWidget(self.addbtn)

        self.editbtn = QPushButton(self.widget1)
        self.editbtn.setObjectName(u"editbtn")

        self.horizontalLayout.addWidget(self.editbtn)

        self.deletbtn = QPushButton(self.widget1)
        self.deletbtn.setObjectName(u"deletbtn")

        self.horizontalLayout.addWidget(self.deletbtn)

        LoansWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LoansWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 873, 33))
        LoansWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LoansWindow)
        self.statusbar.setObjectName(u"statusbar")
        LoansWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoansWindow)

        QMetaObject.connectSlotsByName(LoansWindow)
    # setupUi

    def retranslateUi(self, LoansWindow):
        LoansWindow.setWindowTitle(QCoreApplication.translate("LoansWindow", u"BiblioOrg | Prestamos", None))
        self.resetbtn.setText(QCoreApplication.translate("LoansWindow", u"X", None))
        self.codelabel.setText(QCoreApplication.translate("LoansWindow", u"C\u00f3digo", None))
        self.booklabel.setText(QCoreApplication.translate("LoansWindow", u"Libro", None))
        self.namelabel.setText(QCoreApplication.translate("LoansWindow", u"Nombre", None))
        self.lastnamelabel.setText(QCoreApplication.translate("LoansWindow", u"Apellido", None))
        self.departuredatelabel.setText(QCoreApplication.translate("LoansWindow", u"Fecha de Salida", None))
        self.datelabel.setText(QCoreApplication.translate("LoansWindow", u"Fecha de Devoluci\u00f3n", None))
        self.Historybtn.setText(QCoreApplication.translate("LoansWindow", u"Historial", None))
        self.newbtn.setText(QCoreApplication.translate("LoansWindow", u"Nuevo Registro", None))
        self.addbtn.setText(QCoreApplication.translate("LoansWindow", u"A\u00f1adir", None))
        self.editbtn.setText(QCoreApplication.translate("LoansWindow", u"Editar", None))
        self.deletbtn.setText(QCoreApplication.translate("LoansWindow", u"Eliminar", None))
    # retranslateUi

