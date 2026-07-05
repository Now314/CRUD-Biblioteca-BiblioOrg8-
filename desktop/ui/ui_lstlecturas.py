# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lstlecturas.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableView,
    QVBoxLayout, QWidget)

class Ui_LstLecturasWindow(object):
    def setupUi(self, LstLecturasWindow):
        if not LstLecturasWindow.objectName():
            LstLecturasWindow.setObjectName(u"LstLecturasWindow")
        LstLecturasWindow.resize(912, 436)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LstLecturasWindow.sizePolicy().hasHeightForWidth())
        LstLecturasWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(LstLecturasWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchtxt = QLineEdit(self.centralwidget)
        self.searchtxt.setObjectName(u"searchtxt")

        self.horizontalLayout.addWidget(self.searchtxt)

        self.resetbtn = QPushButton(self.centralwidget)
        self.resetbtn.setObjectName(u"resetbtn")

        self.horizontalLayout.addWidget(self.resetbtn)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.codelabel = QLabel(self.centralwidget)
        self.codelabel.setObjectName(u"codelabel")
        font = QFont()
        font.setItalic(True)
        self.codelabel.setFont(font)

        self.verticalLayout.addWidget(self.codelabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.codetxt = QLineEdit(self.centralwidget)
        self.codetxt.setObjectName(u"codetxt")

        self.horizontalLayout_2.addWidget(self.codetxt)

        self.availablelabel = QLabel(self.centralwidget)
        self.availablelabel.setObjectName(u"availablelabel")
        self.availablelabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.availablelabel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_2.addWidget(self.tableView, 1, 1, 5, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.booklabel = QLabel(self.centralwidget)
        self.booklabel.setObjectName(u"booklabel")
        self.booklabel.setFont(font)

        self.verticalLayout_2.addWidget(self.booklabel)

        self.booktxt = QLineEdit(self.centralwidget)
        self.booktxt.setObjectName(u"booktxt")

        self.verticalLayout_2.addWidget(self.booktxt)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.authorlabel = QLabel(self.centralwidget)
        self.authorlabel.setObjectName(u"authorlabel")
        self.authorlabel.setFont(font)

        self.verticalLayout_3.addWidget(self.authorlabel)

        self.authortxt = QLineEdit(self.centralwidget)
        self.authortxt.setObjectName(u"authortxt")

        self.verticalLayout_3.addWidget(self.authortxt)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.classificationlabel = QLabel(self.centralwidget)
        self.classificationlabel.setObjectName(u"classificationlabel")
        self.classificationlabel.setFont(font)

        self.verticalLayout_4.addWidget(self.classificationlabel)

        self.classificationtxt = QLineEdit(self.centralwidget)
        self.classificationtxt.setObjectName(u"classificationtxt")

        self.verticalLayout_4.addWidget(self.classificationtxt)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 4, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.shelflabel = QLabel(self.centralwidget)
        self.shelflabel.setObjectName(u"shelflabel")
        self.shelflabel.setFont(font)

        self.gridLayout.addWidget(self.shelflabel, 0, 0, 1, 1)

        self.rowlabel = QLabel(self.centralwidget)
        self.rowlabel.setObjectName(u"rowlabel")
        self.rowlabel.setFont(font)

        self.gridLayout.addWidget(self.rowlabel, 0, 1, 1, 1)

        self.shelftxt = QLineEdit(self.centralwidget)
        self.shelftxt.setObjectName(u"shelftxt")

        self.gridLayout.addWidget(self.shelftxt, 1, 0, 1, 1)

        self.rowtxt = QLineEdit(self.centralwidget)
        self.rowtxt.setObjectName(u"rowtxt")

        self.gridLayout.addWidget(self.rowtxt, 1, 1, 1, 1)

        self.numberlabel = QLabel(self.centralwidget)
        self.numberlabel.setObjectName(u"numberlabel")
        self.numberlabel.setFont(font)

        self.gridLayout.addWidget(self.numberlabel, 2, 0, 1, 1)

        self.stocklabel = QLabel(self.centralwidget)
        self.stocklabel.setObjectName(u"stocklabel")
        self.stocklabel.setFont(font)

        self.gridLayout.addWidget(self.stocklabel, 2, 1, 1, 1)

        self.numbertxt = QLineEdit(self.centralwidget)
        self.numbertxt.setObjectName(u"numbertxt")

        self.gridLayout.addWidget(self.numbertxt, 3, 0, 1, 1)

        self.stocktxt = QLineEdit(self.centralwidget)
        self.stocktxt.setObjectName(u"stocktxt")

        self.gridLayout.addWidget(self.stocktxt, 3, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 5, 0, 1, 1)

        LstLecturasWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LstLecturasWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 912, 33))
        LstLecturasWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LstLecturasWindow)
        self.statusbar.setObjectName(u"statusbar")
        LstLecturasWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LstLecturasWindow)

        QMetaObject.connectSlotsByName(LstLecturasWindow)
    # setupUi

    def retranslateUi(self, LstLecturasWindow):
        LstLecturasWindow.setWindowTitle(QCoreApplication.translate("LstLecturasWindow", u"BiblioOrg | Lista de Lecturas", None))
        self.resetbtn.setText(QCoreApplication.translate("LstLecturasWindow", u"X", None))
        self.codelabel.setText(QCoreApplication.translate("LstLecturasWindow", u"C\u00f3digo", None))
        self.availablelabel.setText(QCoreApplication.translate("LstLecturasWindow", u"Disponible en Biblioteca", None))
        self.booklabel.setText(QCoreApplication.translate("LstLecturasWindow", u"Libro", None))
        self.authorlabel.setText(QCoreApplication.translate("LstLecturasWindow", u"Autor", None))
        self.classificationlabel.setText(QCoreApplication.translate("LstLecturasWindow", u"Clasificaci\u00f3n", None))
        self.shelflabel.setText(QCoreApplication.translate("LstLecturasWindow", u"Estante", None))
        self.rowlabel.setText(QCoreApplication.translate("LstLecturasWindow", u"Fila", None))
        self.numberlabel.setText(QCoreApplication.translate("LstLecturasWindow", u"Cantidad", None))
        self.stocklabel.setText(QCoreApplication.translate("LstLecturasWindow", u"Stock", None))
    # retranslateUi

