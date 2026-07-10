# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
)
from PySide6.QtGui import (
    QAction,
    QFont,
)
from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMenu,
    QMenuBar,
    QPushButton,
    QStatusBar,
    QTableView,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(901, 605)
        MainWindow.setMinimumSize(QSize(901, 605))
        self.actionMapa = QAction(MainWindow)
        self.actionMapa.setObjectName("actionMapa")
        self.actionMapa_2 = QAction(MainWindow)
        self.actionMapa_2.setObjectName("actionMapa_2")
        self.actionRecomendaciones = QAction(MainWindow)
        self.actionRecomendaciones.setObjectName("actionRecomendaciones")
        self.actionContacto = QAction(MainWindow)
        self.actionContacto.setObjectName("actionContacto")
        self.actionPanel_Lista_de_Lecturas = QAction(MainWindow)
        self.actionPanel_Lista_de_Lecturas.setObjectName(
            "actionPanel_Lista_de_Lecturas"
        )
        self.actionPanel_de_Admin = QAction(MainWindow)
        self.actionPanel_de_Admin.setObjectName("actionPanel_de_Admin")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchtxt = QLineEdit(self.centralwidget)
        self.searchtxt.setObjectName("searchtxt")

        self.horizontalLayout.addWidget(self.searchtxt)

        self.resetbtn = QPushButton(self.centralwidget)
        self.resetbtn.setObjectName("resetbtn")

        self.horizontalLayout.addWidget(self.resetbtn)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.codelabel = QLabel(self.centralwidget)
        self.codelabel.setObjectName("codelabel")
        font = QFont()
        font.setItalic(True)
        self.codelabel.setFont(font)

        self.gridLayout.addWidget(self.codelabel, 0, 0, 1, 1)

        self.booklabel = QLabel(self.centralwidget)
        self.booklabel.setObjectName("booklabel")
        self.booklabel.setFont(font)

        self.gridLayout.addWidget(self.booklabel, 0, 1, 1, 1)

        self.authorlabel = QLabel(self.centralwidget)
        self.authorlabel.setObjectName("authorlabel")
        self.authorlabel.setFont(font)

        self.gridLayout.addWidget(self.authorlabel, 0, 5, 1, 1)

        self.codetxt = QLineEdit(self.centralwidget)
        self.codetxt.setObjectName("codetxt")

        self.gridLayout.addWidget(self.codetxt, 1, 0, 1, 1)

        self.booktxt = QLineEdit(self.centralwidget)
        self.booktxt.setObjectName("booktxt")

        self.gridLayout.addWidget(self.booktxt, 1, 1, 1, 4)

        self.authortxt = QLineEdit(self.centralwidget)
        self.authortxt.setObjectName("authortxt")

        self.gridLayout.addWidget(self.authortxt, 1, 5, 1, 2)

        self.classificationlabel = QLabel(self.centralwidget)
        self.classificationlabel.setObjectName("classificationlabel")
        self.classificationlabel.setFont(font)

        self.gridLayout.addWidget(self.classificationlabel, 2, 0, 1, 1)

        self.shelflabel = QLabel(self.centralwidget)
        self.shelflabel.setObjectName("shelflabel")
        self.shelflabel.setFont(font)

        self.gridLayout.addWidget(self.shelflabel, 2, 2, 1, 1)

        self.rowlabel = QLabel(self.centralwidget)
        self.rowlabel.setObjectName("rowlabel")
        self.rowlabel.setFont(font)

        self.gridLayout.addWidget(self.rowlabel, 2, 3, 1, 1)

        self.numberlabel = QLabel(self.centralwidget)
        self.numberlabel.setObjectName("numberlabel")
        self.numberlabel.setFont(font)

        self.gridLayout.addWidget(self.numberlabel, 2, 4, 1, 1)

        self.stocklabel = QLabel(self.centralwidget)
        self.stocklabel.setObjectName("stocklabel")
        self.stocklabel.setFont(font)

        self.gridLayout.addWidget(self.stocklabel, 2, 6, 1, 1)

        self.classificationtxt = QLineEdit(self.centralwidget)
        self.classificationtxt.setObjectName("classificationtxt")

        self.gridLayout.addWidget(self.classificationtxt, 3, 0, 1, 2)

        self.shelftxt = QLineEdit(self.centralwidget)
        self.shelftxt.setObjectName("shelftxt")

        self.gridLayout.addWidget(self.shelftxt, 3, 2, 1, 1)

        self.rowtxt = QLineEdit(self.centralwidget)
        self.rowtxt.setObjectName("rowtxt")

        self.gridLayout.addWidget(self.rowtxt, 3, 3, 1, 1)

        self.numbertxt = QLineEdit(self.centralwidget)
        self.numbertxt.setObjectName("numbertxt")

        self.gridLayout.addWidget(self.numbertxt, 3, 4, 1, 2)

        self.stocktxt = QLineEdit(self.centralwidget)
        self.stocktxt.setObjectName("stocktxt")

        self.gridLayout.addWidget(self.stocktxt, 3, 6, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")

        self.verticalLayout.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 901, 33))
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuLista_de_Lectura = QMenu(self.menubar)
        self.menuLista_de_Lectura.setObjectName("menuLista_de_Lectura")
        self.menuAdmin = QMenu(self.menubar)
        self.menuAdmin.setObjectName("menuAdmin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menubar.addAction(self.menuLista_de_Lectura.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())
        self.menuAyuda.addAction(self.actionMapa_2)
        self.menuAyuda.addAction(self.actionRecomendaciones)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionContacto)
        self.menuLista_de_Lectura.addAction(self.actionPanel_Lista_de_Lecturas)
        self.menuAdmin.addAction(self.actionPanel_de_Admin)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "BiblioOrg | Inicio", None)
        )
        self.actionMapa.setText(QCoreApplication.translate("MainWindow", "Mapa", None))
        self.actionMapa_2.setText(
            QCoreApplication.translate("MainWindow", "Mapa", None)
        )
        self.actionRecomendaciones.setText(
            QCoreApplication.translate("MainWindow", "Recomendaciones", None)
        )
        self.actionContacto.setText(
            QCoreApplication.translate("MainWindow", "Contacto", None)
        )
        self.actionPanel_Lista_de_Lecturas.setText(
            QCoreApplication.translate("MainWindow", "Panel Lista de Lecturas", None)
        )
        self.actionPanel_de_Admin.setText(
            QCoreApplication.translate("MainWindow", "Panel de Admin", None)
        )
        self.resetbtn.setText(QCoreApplication.translate("MainWindow", "X", None))
        self.codelabel.setText(
            QCoreApplication.translate("MainWindow", "C\u00f3digo", None)
        )
        self.booklabel.setText(QCoreApplication.translate("MainWindow", "Libro", None))
        self.authorlabel.setText(
            QCoreApplication.translate("MainWindow", "Autor", None)
        )
        self.classificationlabel.setText(
            QCoreApplication.translate("MainWindow", "Clasificaci\u00f3n", None)
        )
        self.shelflabel.setText(
            QCoreApplication.translate("MainWindow", "Estante", None)
        )
        self.rowlabel.setText(QCoreApplication.translate("MainWindow", "Fila", None))
        self.numberlabel.setText(
            QCoreApplication.translate("MainWindow", "Cantidad", None)
        )
        self.stocklabel.setText(QCoreApplication.translate("MainWindow", "Stock", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", "Ayuda", None))
        self.menuLista_de_Lectura.setTitle(
            QCoreApplication.translate("MainWindow", "Lista de Lectura", None)
        )
        self.menuAdmin.setTitle(QCoreApplication.translate("MainWindow", "Admin", None))

    # retranslateUi
