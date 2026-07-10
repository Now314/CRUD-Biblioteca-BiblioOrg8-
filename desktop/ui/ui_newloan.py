# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newloan.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDateEdit,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class Ui_newloanWindow(object):
    def setupUi(self, newloanWindow):
        if not newloanWindow.objectName():
            newloanWindow.setObjectName("newloanWindow")
        newloanWindow.resize(360, 453)
        newloanWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(newloanWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.codelabel = QLabel(self.centralwidget)
        self.codelabel.setObjectName("codelabel")
        font = QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.codelabel.setFont(font)

        self.verticalLayout_6.addWidget(self.codelabel)

        self.codetxt = QLineEdit(self.centralwidget)
        self.codetxt.setObjectName("codetxt")

        self.verticalLayout_6.addWidget(self.codetxt)

        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.booklabel = QLabel(self.centralwidget)
        self.booklabel.setObjectName("booklabel")
        self.booklabel.setFont(font)

        self.verticalLayout_5.addWidget(self.booklabel)

        self.booktxt = QLineEdit(self.centralwidget)
        self.booktxt.setObjectName("booktxt")

        self.verticalLayout_5.addWidget(self.booktxt)

        self.gridLayout.addLayout(self.verticalLayout_5, 1, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.namelabel = QLabel(self.centralwidget)
        self.namelabel.setObjectName("namelabel")
        self.namelabel.setFont(font)

        self.verticalLayout_4.addWidget(self.namelabel)

        self.nametxt = QLineEdit(self.centralwidget)
        self.nametxt.setObjectName("nametxt")

        self.verticalLayout_4.addWidget(self.nametxt)

        self.gridLayout.addLayout(self.verticalLayout_4, 2, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lastnamelabel = QLabel(self.centralwidget)
        self.lastnamelabel.setObjectName("lastnamelabel")
        self.lastnamelabel.setFont(font)

        self.verticalLayout_3.addWidget(self.lastnamelabel)

        self.lastnametxt = QLineEdit(self.centralwidget)
        self.lastnametxt.setObjectName("lastnametxt")

        self.verticalLayout_3.addWidget(self.lastnametxt)

        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.datelabel = QLabel(self.centralwidget)
        self.datelabel.setObjectName("datelabel")
        self.datelabel.setFont(font)

        self.verticalLayout_2.addWidget(self.datelabel)

        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName("dateEdit")
        font1 = QFont()
        font1.setPointSize(11)
        self.dateEdit.setFont(font1)

        self.verticalLayout_2.addWidget(self.dateEdit)

        self.gridLayout.addLayout(self.verticalLayout_2, 4, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer, 5, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.addbtn = QPushButton(self.centralwidget)
        self.addbtn.setObjectName("addbtn")

        self.verticalLayout.addWidget(self.addbtn)

        self.cancelbtn = QPushButton(self.centralwidget)
        self.cancelbtn.setObjectName("cancelbtn")

        self.verticalLayout.addWidget(self.cancelbtn)

        self.gridLayout.addLayout(self.verticalLayout, 6, 0, 1, 1)

        newloanWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(newloanWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 360, 33))
        newloanWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(newloanWindow)
        self.statusbar.setObjectName("statusbar")
        newloanWindow.setStatusBar(self.statusbar)

        self.retranslateUi(newloanWindow)

        QMetaObject.connectSlotsByName(newloanWindow)

    # setupUi

    def retranslateUi(self, newloanWindow):
        newloanWindow.setWindowTitle(
            QCoreApplication.translate(
                "newloanWindow", "BiblioOrg | Nueva Solicitud", None
            )
        )
        self.codelabel.setText(
            QCoreApplication.translate("newloanWindow", "C\u00f3digo", None)
        )
        self.booklabel.setText(
            QCoreApplication.translate("newloanWindow", "Libro", None)
        )
        self.namelabel.setText(
            QCoreApplication.translate("newloanWindow", "Nombre", None)
        )
        self.lastnamelabel.setText(
            QCoreApplication.translate("newloanWindow", "Apellido", None)
        )
        self.datelabel.setText(
            QCoreApplication.translate(
                "newloanWindow", "Fecha de Devoluci\u00f3n", None
            )
        )
        self.addbtn.setText(
            QCoreApplication.translate("newloanWindow", "A\u00f1adir", None)
        )
        self.cancelbtn.setText(
            QCoreApplication.translate("newloanWindow", "Cancelar", None)
        )

    # retranslateUi
