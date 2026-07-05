# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        if not AdminWindow.objectName():
            AdminWindow.setObjectName(u"AdminWindow")
        AdminWindow.resize(901, 605)
        AdminWindow.setMinimumSize(QSize(901, 605))
        self.actionMapa = QAction(AdminWindow)
        self.actionMapa.setObjectName(u"actionMapa")
        self.actionREcomendaciones = QAction(AdminWindow)
        self.actionREcomendaciones.setObjectName(u"actionREcomendaciones")
        self.actionUsuarios = QAction(AdminWindow)
        self.actionUsuarios.setObjectName(u"actionUsuarios")
        self.actionMapa_2 = QAction(AdminWindow)
        self.actionMapa_2.setObjectName(u"actionMapa_2")
        self.actionContacto = QAction(AdminWindow)
        self.actionContacto.setObjectName(u"actionContacto")
        self.centralwidget = QWidget(AdminWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchtxt = QLineEdit(self.centralwidget)
        self.searchtxt.setObjectName(u"searchtxt")

        self.horizontalLayout.addWidget(self.searchtxt)

        self.resetbtn = QPushButton(self.centralwidget)
        self.resetbtn.setObjectName(u"resetbtn")

        self.horizontalLayout.addWidget(self.resetbtn)

        self.newrequestbtn = QPushButton(self.centralwidget)
        self.newrequestbtn.setObjectName(u"newrequestbtn")

        self.horizontalLayout.addWidget(self.newrequestbtn)

        self.loansbtn = QPushButton(self.centralwidget)
        self.loansbtn.setObjectName(u"loansbtn")

        self.horizontalLayout.addWidget(self.loansbtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.codelabel = QLabel(self.centralwidget)
        self.codelabel.setObjectName(u"codelabel")
        font = QFont()
        font.setItalic(True)
        self.codelabel.setFont(font)

        self.gridLayout.addWidget(self.codelabel, 0, 0, 1, 1)

        self.booklabel = QLabel(self.centralwidget)
        self.booklabel.setObjectName(u"booklabel")
        self.booklabel.setFont(font)

        self.gridLayout.addWidget(self.booklabel, 0, 1, 1, 1)

        self.authorlabel = QLabel(self.centralwidget)
        self.authorlabel.setObjectName(u"authorlabel")
        self.authorlabel.setFont(font)

        self.gridLayout.addWidget(self.authorlabel, 0, 5, 1, 1)

        self.codetxt = QLineEdit(self.centralwidget)
        self.codetxt.setObjectName(u"codetxt")

        self.gridLayout.addWidget(self.codetxt, 1, 0, 1, 1)

        self.booktxt = QLineEdit(self.centralwidget)
        self.booktxt.setObjectName(u"booktxt")

        self.gridLayout.addWidget(self.booktxt, 1, 1, 1, 4)

        self.authortxt = QLineEdit(self.centralwidget)
        self.authortxt.setObjectName(u"authortxt")

        self.gridLayout.addWidget(self.authortxt, 1, 5, 1, 2)

        self.classificationlabel = QLabel(self.centralwidget)
        self.classificationlabel.setObjectName(u"classificationlabel")
        self.classificationlabel.setFont(font)

        self.gridLayout.addWidget(self.classificationlabel, 2, 0, 1, 1)

        self.shelflabel = QLabel(self.centralwidget)
        self.shelflabel.setObjectName(u"shelflabel")
        self.shelflabel.setFont(font)

        self.gridLayout.addWidget(self.shelflabel, 2, 2, 1, 1)

        self.rowlabel = QLabel(self.centralwidget)
        self.rowlabel.setObjectName(u"rowlabel")
        self.rowlabel.setFont(font)

        self.gridLayout.addWidget(self.rowlabel, 2, 3, 1, 1)

        self.numberlabel = QLabel(self.centralwidget)
        self.numberlabel.setObjectName(u"numberlabel")
        self.numberlabel.setFont(font)

        self.gridLayout.addWidget(self.numberlabel, 2, 4, 1, 2)

        self.stocklabel = QLabel(self.centralwidget)
        self.stocklabel.setObjectName(u"stocklabel")
        self.stocklabel.setFont(font)

        self.gridLayout.addWidget(self.stocklabel, 2, 6, 1, 1)

        self.classificationtxt = QLineEdit(self.centralwidget)
        self.classificationtxt.setObjectName(u"classificationtxt")

        self.gridLayout.addWidget(self.classificationtxt, 3, 0, 1, 2)

        self.shelftxt = QLineEdit(self.centralwidget)
        self.shelftxt.setObjectName(u"shelftxt")

        self.gridLayout.addWidget(self.shelftxt, 3, 2, 1, 1)

        self.rowtxt = QLineEdit(self.centralwidget)
        self.rowtxt.setObjectName(u"rowtxt")

        self.gridLayout.addWidget(self.rowtxt, 3, 3, 1, 1)

        self.numbertxt = QLineEdit(self.centralwidget)
        self.numbertxt.setObjectName(u"numbertxt")

        self.gridLayout.addWidget(self.numbertxt, 3, 4, 1, 2)

        self.stocktxt = QLineEdit(self.centralwidget)
        self.stocktxt.setObjectName(u"stocktxt")

        self.gridLayout.addWidget(self.stocktxt, 3, 6, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        AdminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AdminWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 901, 33))
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        self.menuEditar_Lista_de_Lectura = QMenu(self.menubar)
        self.menuEditar_Lista_de_Lectura.setObjectName(u"menuEditar_Lista_de_Lectura")
        self.menuEditar_Registro_Principal = QMenu(self.menubar)
        self.menuEditar_Registro_Principal.setObjectName(u"menuEditar_Registro_Principal")
        self.menuHistorial = QMenu(self.menubar)
        self.menuHistorial.setObjectName(u"menuHistorial")
        self.menuObservaciones = QMenu(self.menubar)
        self.menuObservaciones.setObjectName(u"menuObservaciones")
        AdminWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AdminWindow)
        self.statusbar.setObjectName(u"statusbar")
        AdminWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menubar.addAction(self.menuEditar_Lista_de_Lectura.menuAction())
        self.menubar.addAction(self.menuEditar_Registro_Principal.menuAction())
        self.menubar.addAction(self.menuHistorial.menuAction())
        self.menubar.addAction(self.menuObservaciones.menuAction())
        self.menuAyuda.addAction(self.actionMapa)
        self.menuAyuda.addAction(self.actionMapa_2)
        self.menuAyuda.addAction(self.actionUsuarios)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionREcomendaciones)
        self.menuAyuda.addAction(self.actionContacto)

        self.retranslateUi(AdminWindow)

        QMetaObject.connectSlotsByName(AdminWindow)
    # setupUi

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(QCoreApplication.translate("AdminWindow", u"BiblioOrg | Admin", None))
        self.actionMapa.setText(QCoreApplication.translate("AdminWindow", u"Asistente de Inventario", None))
        self.actionREcomendaciones.setText(QCoreApplication.translate("AdminWindow", u"Recomendaciones", None))
        self.actionUsuarios.setText(QCoreApplication.translate("AdminWindow", u"Usuarios", None))
        self.actionMapa_2.setText(QCoreApplication.translate("AdminWindow", u"Mapa", None))
        self.actionContacto.setText(QCoreApplication.translate("AdminWindow", u"Contacto", None))
        self.resetbtn.setText(QCoreApplication.translate("AdminWindow", u"X", None))
        self.newrequestbtn.setText(QCoreApplication.translate("AdminWindow", u"Nueva Solicitud", None))
        self.loansbtn.setText(QCoreApplication.translate("AdminWindow", u"Prestamos", None))
        self.codelabel.setText(QCoreApplication.translate("AdminWindow", u"C\u00f3digo", None))
        self.booklabel.setText(QCoreApplication.translate("AdminWindow", u"Libro", None))
        self.authorlabel.setText(QCoreApplication.translate("AdminWindow", u"Autor", None))
        self.classificationlabel.setText(QCoreApplication.translate("AdminWindow", u"Clasificaci\u00f3n", None))
        self.shelflabel.setText(QCoreApplication.translate("AdminWindow", u"Estante", None))
        self.rowlabel.setText(QCoreApplication.translate("AdminWindow", u"Fila", None))
        self.numberlabel.setText(QCoreApplication.translate("AdminWindow", u"Cantidad", None))
        self.stocklabel.setText(QCoreApplication.translate("AdminWindow", u"Stock", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("AdminWindow", u"Ayuda", None))
        self.menuEditar_Lista_de_Lectura.setTitle(QCoreApplication.translate("AdminWindow", u"Editar Lista de Lectura", None))
        self.menuEditar_Registro_Principal.setTitle(QCoreApplication.translate("AdminWindow", u"Editar Registro Principal", None))
        self.menuHistorial.setTitle(QCoreApplication.translate("AdminWindow", u"Historial", None))
        self.menuObservaciones.setTitle(QCoreApplication.translate("AdminWindow", u"Observaciones", None))
    # retranslateUi

