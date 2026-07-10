# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lstlecturas.ui'
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
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTableView,
    QVBoxLayout,
    QWidget,
)


class Ui_LstLecturasWindow(object):
    def setupUi(self, LstLecturasWindow):
        if not LstLecturasWindow.objectName():
            LstLecturasWindow.setObjectName("LstLecturasWindow")
        LstLecturasWindow.resize(912, 436)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LstLecturasWindow.sizePolicy().hasHeightForWidth())
        LstLecturasWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(LstLecturasWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchtxt = QLineEdit(self.centralwidget)
        self.searchtxt.setObjectName("searchtxt")

        self.horizontalLayout.addWidget(self.searchtxt)

        self.resetbtn = QPushButton(self.centralwidget)
        self.resetbtn.setObjectName("resetbtn")

        self.horizontalLayout.addWidget(self.resetbtn)

        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.codelabel = QLabel(self.centralwidget)
        self.codelabel.setObjectName("codelabel")
        font = QFont()
        font.setItalic(True)
        self.codelabel.setFont(font)

        self.verticalLayout.addWidget(self.codelabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.codetxt = QLineEdit(self.centralwidget)
        self.codetxt.setObjectName("codetxt")

        self.horizontalLayout_2.addWidget(self.codetxt)

        self.availablelabel = QLabel(self.centralwidget)
        self.availablelabel.setObjectName("availablelabel")
        self.availablelabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.availablelabel)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")

        self.gridLayout_2.addWidget(self.tableView, 1, 1, 5, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.booklabel = QLabel(self.centralwidget)
        self.booklabel.setObjectName("booklabel")
        self.booklabel.setFont(font)

        self.verticalLayout_2.addWidget(self.booklabel)

        self.booktxt = QLineEdit(self.centralwidget)
        self.booktxt.setObjectName("booktxt")

        self.verticalLayout_2.addWidget(self.booktxt)

        self.gridLayout_2.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.authorlabel = QLabel(self.centralwidget)
        self.authorlabel.setObjectName("authorlabel")
        self.authorlabel.setFont(font)

        self.verticalLayout_3.addWidget(self.authorlabel)

        self.authortxt = QLineEdit(self.centralwidget)
        self.authortxt.setObjectName("authortxt")

        self.verticalLayout_3.addWidget(self.authortxt)

        self.gridLayout_2.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.classificationlabel = QLabel(self.centralwidget)
        self.classificationlabel.setObjectName("classificationlabel")
        self.classificationlabel.setFont(font)

        self.verticalLayout_4.addWidget(self.classificationlabel)

        self.classificationtxt = QLineEdit(self.centralwidget)
        self.classificationtxt.setObjectName("classificationtxt")

        self.verticalLayout_4.addWidget(self.classificationtxt)

        self.gridLayout_2.addLayout(self.verticalLayout_4, 4, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.shelflabel = QLabel(self.centralwidget)
        self.shelflabel.setObjectName("shelflabel")
        self.shelflabel.setFont(font)

        self.gridLayout.addWidget(self.shelflabel, 0, 0, 1, 1)

        self.rowlabel = QLabel(self.centralwidget)
        self.rowlabel.setObjectName("rowlabel")
        self.rowlabel.setFont(font)

        self.gridLayout.addWidget(self.rowlabel, 0, 1, 1, 1)

        self.shelftxt = QLineEdit(self.centralwidget)
        self.shelftxt.setObjectName("shelftxt")

        self.gridLayout.addWidget(self.shelftxt, 1, 0, 1, 1)

        self.rowtxt = QLineEdit(self.centralwidget)
        self.rowtxt.setObjectName("rowtxt")

        self.gridLayout.addWidget(self.rowtxt, 1, 1, 1, 1)

        self.numberlabel = QLabel(self.centralwidget)
        self.numberlabel.setObjectName("numberlabel")
        self.numberlabel.setFont(font)

        self.gridLayout.addWidget(self.numberlabel, 2, 0, 1, 1)

        self.stocklabel = QLabel(self.centralwidget)
        self.stocklabel.setObjectName("stocklabel")
        self.stocklabel.setFont(font)

        self.gridLayout.addWidget(self.stocklabel, 2, 1, 1, 1)

        self.numbertxt = QLineEdit(self.centralwidget)
        self.numbertxt.setObjectName("numbertxt")

        self.gridLayout.addWidget(self.numbertxt, 3, 0, 1, 1)

        self.stocktxt = QLineEdit(self.centralwidget)
        self.stocktxt.setObjectName("stocktxt")

        self.gridLayout.addWidget(self.stocktxt, 3, 1, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 5, 0, 1, 1)

        LstLecturasWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LstLecturasWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 912, 33))
        LstLecturasWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LstLecturasWindow)
        self.statusbar.setObjectName("statusbar")
        LstLecturasWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LstLecturasWindow)

        QMetaObject.connectSlotsByName(LstLecturasWindow)

    # setupUi

    def retranslateUi(self, LstLecturasWindow):
        LstLecturasWindow.setWindowTitle(
            QCoreApplication.translate(
                "LstLecturasWindow", "BiblioOrg | Lista de Lecturas", None
            )
        )
        self.resetbtn.setText(
            QCoreApplication.translate("LstLecturasWindow", "X", None)
        )
        self.codelabel.setText(
            QCoreApplication.translate("LstLecturasWindow", "C\u00f3digo", None)
        )
        self.availablelabel.setText(
            QCoreApplication.translate(
                "LstLecturasWindow", "Disponible en Biblioteca", None
            )
        )
        self.booklabel.setText(
            QCoreApplication.translate("LstLecturasWindow", "Libro", None)
        )
        self.authorlabel.setText(
            QCoreApplication.translate("LstLecturasWindow", "Autor", None)
        )
        self.classificationlabel.setText(
            QCoreApplication.translate("LstLecturasWindow", "Clasificaci\u00f3n", None)
        )
        self.shelflabel.setText(
            QCoreApplication.translate("LstLecturasWindow", "Estante", None)
        )
        self.rowlabel.setText(
            QCoreApplication.translate("LstLecturasWindow", "Fila", None)
        )
        self.numberlabel.setText(
            QCoreApplication.translate("LstLecturasWindow", "Cantidad", None)
        )
        self.stocklabel.setText(
            QCoreApplication.translate("LstLecturasWindow", "Stock", None)
        )

    # retranslateUi
