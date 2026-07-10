# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
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


class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        if not AdminWindow.objectName():
            AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(901, 605)
        AdminWindow.setMinimumSize(QSize(901, 605))
        self.actionInventario = QAction(AdminWindow)
        self.actionInventario.setObjectName("actionInventario")
        self.actionRecomendaciones = QAction(AdminWindow)
        self.actionRecomendaciones.setObjectName("actionRecomendaciones")
        self.actionUsuarios = QAction(AdminWindow)
        self.actionUsuarios.setObjectName("actionUsuarios")
        self.actionMapa = QAction(AdminWindow)
        self.actionMapa.setObjectName("actionMapa")
        self.actionContacto = QAction(AdminWindow)
        self.actionContacto.setObjectName("actionContacto")
        self.centralwidget = QWidget(AdminWindow)
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

        self.newrequestbtn = QPushButton(self.centralwidget)
        self.newrequestbtn.setObjectName("newrequestbtn")

        self.horizontalLayout.addWidget(self.newrequestbtn)

        self.loansbtn = QPushButton(self.centralwidget)
        self.loansbtn.setObjectName("loansbtn")

        self.horizontalLayout.addWidget(self.loansbtn)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.classificationlabel = QLabel(self.centralwidget)
        self.classificationlabel.setObjectName("classificationlabel")
        font = QFont()
        font.setItalic(True)
        self.classificationlabel.setFont(font)

        self.gridLayout.addWidget(self.classificationlabel, 2, 0, 1, 1)

        self.rowlabel = QLabel(self.centralwidget)
        self.rowlabel.setObjectName("rowlabel")
        self.rowlabel.setFont(font)

        self.gridLayout.addWidget(self.rowlabel, 2, 3, 1, 1)

        self.stocktxt = QLineEdit(self.centralwidget)
        self.stocktxt.setObjectName("stocktxt")

        self.gridLayout.addWidget(self.stocktxt, 3, 6, 1, 1)

        self.shelftxt = QLineEdit(self.centralwidget)
        self.shelftxt.setObjectName("shelftxt")

        self.gridLayout.addWidget(self.shelftxt, 3, 2, 1, 1)

        self.shelflabel = QLabel(self.centralwidget)
        self.shelflabel.setObjectName("shelflabel")
        self.shelflabel.setFont(font)

        self.gridLayout.addWidget(self.shelflabel, 2, 2, 1, 1)

        self.codetxt = QLineEdit(self.centralwidget)
        self.codetxt.setObjectName("codetxt")

        self.gridLayout.addWidget(self.codetxt, 1, 0, 1, 1)

        self.authortxt = QLineEdit(self.centralwidget)
        self.authortxt.setObjectName("authortxt")

        self.gridLayout.addWidget(self.authortxt, 1, 5, 1, 2)

        self.numberlabel = QLabel(self.centralwidget)
        self.numberlabel.setObjectName("numberlabel")
        self.numberlabel.setFont(font)

        self.gridLayout.addWidget(self.numberlabel, 2, 4, 1, 2)

        self.classificationtxt = QLineEdit(self.centralwidget)
        self.classificationtxt.setObjectName("classificationtxt")

        self.gridLayout.addWidget(self.classificationtxt, 3, 0, 1, 2)

        self.booklabel = QLabel(self.centralwidget)
        self.booklabel.setObjectName("booklabel")
        self.booklabel.setFont(font)

        self.gridLayout.addWidget(self.booklabel, 0, 1, 1, 1)

        self.authorlabel = QLabel(self.centralwidget)
        self.authorlabel.setObjectName("authorlabel")
        self.authorlabel.setFont(font)

        self.gridLayout.addWidget(self.authorlabel, 0, 5, 1, 1)

        self.rowtxt = QLineEdit(self.centralwidget)
        self.rowtxt.setObjectName("rowtxt")

        self.gridLayout.addWidget(self.rowtxt, 3, 3, 1, 1)

        self.numbertxt = QLineEdit(self.centralwidget)
        self.numbertxt.setObjectName("numbertxt")

        self.gridLayout.addWidget(self.numbertxt, 3, 4, 1, 2)

        self.stocklabel = QLabel(self.centralwidget)
        self.stocklabel.setObjectName("stocklabel")
        self.stocklabel.setFont(font)

        self.gridLayout.addWidget(self.stocklabel, 2, 6, 1, 1)

        self.codelabel = QLabel(self.centralwidget)
        self.codelabel.setObjectName("codelabel")
        self.codelabel.setFont(font)

        self.gridLayout.addWidget(self.codelabel, 0, 0, 1, 1)

        self.booktxt = QLineEdit(self.centralwidget)
        self.booktxt.setObjectName("booktxt")

        self.gridLayout.addWidget(self.booktxt, 1, 1, 1, 4)

        self.verticalLayout.addLayout(self.gridLayout)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")

        self.verticalLayout.addWidget(self.tableView)

        AdminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AdminWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 901, 33))
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuEditar_Lista_de_Lectura = QMenu(self.menubar)
        self.menuEditar_Lista_de_Lectura.setObjectName("menuEditar_Lista_de_Lectura")
        self.menuEditar_Registro_Principal = QMenu(self.menubar)
        self.menuEditar_Registro_Principal.setObjectName(
            "menuEditar_Registro_Principal"
        )
        self.menuHistorial = QMenu(self.menubar)
        self.menuHistorial.setObjectName("menuHistorial")
        self.menuObservaciones = QMenu(self.menubar)
        self.menuObservaciones.setObjectName("menuObservaciones")
        AdminWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AdminWindow)
        self.statusbar.setObjectName("statusbar")
        AdminWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menubar.addAction(self.menuEditar_Lista_de_Lectura.menuAction())
        self.menubar.addAction(self.menuEditar_Registro_Principal.menuAction())
        self.menubar.addAction(self.menuHistorial.menuAction())
        self.menubar.addAction(self.menuObservaciones.menuAction())
        self.menuAyuda.addAction(self.actionInventario)
        self.menuAyuda.addAction(self.actionMapa)
        self.menuAyuda.addAction(self.actionUsuarios)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionRecomendaciones)
        self.menuAyuda.addAction(self.actionContacto)

        self.retranslateUi(AdminWindow)

        QMetaObject.connectSlotsByName(AdminWindow)

    # setupUi

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(
            QCoreApplication.translate("AdminWindow", "BiblioOrg | Admin", None)
        )
        self.actionInventario.setText(
            QCoreApplication.translate("AdminWindow", "Asistente de Inventario", None)
        )
        self.actionRecomendaciones.setText(
            QCoreApplication.translate("AdminWindow", "Recomendaciones", None)
        )
        self.actionUsuarios.setText(
            QCoreApplication.translate("AdminWindow", "Usuarios", None)
        )
        self.actionMapa.setText(QCoreApplication.translate("AdminWindow", "Mapa", None))
        self.actionContacto.setText(
            QCoreApplication.translate("AdminWindow", "Contacto", None)
        )
        self.resetbtn.setText(QCoreApplication.translate("AdminWindow", "X", None))
        self.newrequestbtn.setText(
            QCoreApplication.translate("AdminWindow", "Nueva Solicitud", None)
        )
        self.loansbtn.setText(
            QCoreApplication.translate("AdminWindow", "Prestamos", None)
        )
        self.classificationlabel.setText(
            QCoreApplication.translate("AdminWindow", "Clasificaci\u00f3n", None)
        )
        self.rowlabel.setText(QCoreApplication.translate("AdminWindow", "Fila", None))
        self.shelflabel.setText(
            QCoreApplication.translate("AdminWindow", "Estante", None)
        )
        self.numberlabel.setText(
            QCoreApplication.translate("AdminWindow", "Cantidad", None)
        )
        self.booklabel.setText(QCoreApplication.translate("AdminWindow", "Libro", None))
        self.authorlabel.setText(
            QCoreApplication.translate("AdminWindow", "Autor", None)
        )
        self.stocklabel.setText(
            QCoreApplication.translate("AdminWindow", "Stock", None)
        )
        self.codelabel.setText(
            QCoreApplication.translate("AdminWindow", "C\u00f3digo", None)
        )
        self.menuAyuda.setTitle(
            QCoreApplication.translate("AdminWindow", "Ayuda", None)
        )
        self.menuEditar_Lista_de_Lectura.setTitle(
            QCoreApplication.translate("AdminWindow", "Editar Lista de Lectura", None)
        )
        self.menuEditar_Registro_Principal.setTitle(
            QCoreApplication.translate("AdminWindow", "Editar Registro Principal", None)
        )
        self.menuHistorial.setTitle(
            QCoreApplication.translate("AdminWindow", "Historial", None)
        )
        self.menuObservaciones.setTitle(
            QCoreApplication.translate("AdminWindow", "Observaciones", None)
        )

    # retranslateUi
