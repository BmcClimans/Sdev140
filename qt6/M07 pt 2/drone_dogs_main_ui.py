# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drone_dogs_main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.LabelTitle = QLabel(self.centralwidget)
        self.LabelTitle.setObjectName(u"LabelTitle")
        self.LabelTitle.setGeometry(QRect(20, 30, 311, 71))
        self.LabelTitle.setPixmap(QPixmap(u"dronedogs_order_form_title_text.png"))
        self.LabelTitle.setScaledContents(True)
        self.LabelLogo = QLabel(self.centralwidget)
        self.LabelLogo.setObjectName(u"LabelLogo")
        self.LabelLogo.setGeometry(QRect(440, 20, 141, 181))
        self.LabelLogo.setPixmap(QPixmap(u"DroneDogsLogo.png"))
        self.LabelLogo.setScaledContents(True)
        self.LabelBeefDogs = QLabel(self.centralwidget)
        self.LabelBeefDogs.setObjectName(u"LabelBeefDogs")
        self.LabelBeefDogs.setGeometry(QRect(40, 120, 71, 16))
        self.LabelPorkDogs = QLabel(self.centralwidget)
        self.LabelPorkDogs.setObjectName(u"LabelPorkDogs")
        self.LabelPorkDogs.setGeometry(QRect(40, 160, 71, 16))
        self.LabelTurkeyDogs = QLabel(self.centralwidget)
        self.LabelTurkeyDogs.setObjectName(u"LabelTurkeyDogs")
        self.LabelTurkeyDogs.setGeometry(QRect(40, 200, 81, 16))
        self.LabelSubtotal = QLabel(self.centralwidget)
        self.LabelSubtotal.setObjectName(u"LabelSubtotal")
        self.LabelSubtotal.setGeometry(QRect(40, 310, 61, 16))
        self.LabelSalesTax = QLabel(self.centralwidget)
        self.LabelSalesTax.setObjectName(u"LabelSalesTax")
        self.LabelSalesTax.setGeometry(QRect(40, 350, 61, 16))
        self.LabeTotalCost = QLabel(self.centralwidget)
        self.LabeTotalCost.setObjectName(u"LabeTotalCost")
        self.LabeTotalCost.setGeometry(QRect(40, 390, 61, 16))
        self.SpinBoxBeefDogs = QSpinBox(self.centralwidget)
        self.SpinBoxBeefDogs.setObjectName(u"SpinBoxBeefDogs")
        self.SpinBoxBeefDogs.setGeometry(QRect(150, 120, 78, 26))
        self.SpinBoxPorkDogs = QSpinBox(self.centralwidget)
        self.SpinBoxPorkDogs.setObjectName(u"SpinBoxPorkDogs")
        self.SpinBoxPorkDogs.setGeometry(QRect(150, 160, 78, 26))
        self.SpinBoxTurkeyDogs = QSpinBox(self.centralwidget)
        self.SpinBoxTurkeyDogs.setObjectName(u"SpinBoxTurkeyDogs")
        self.SpinBoxTurkeyDogs.setGeometry(QRect(150, 200, 78, 26))
        self.LineEditSubtotal = QLineEdit(self.centralwidget)
        self.LineEditSubtotal.setObjectName(u"LineEditSubtotal")
        self.LineEditSubtotal.setEnabled(False)
        self.LineEditSubtotal.setGeometry(QRect(140, 310, 113, 26))
        self.LineEditSubtotal.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.LineEditSubtotal.setReadOnly(True)
        self.LineEditSalesTax = QLineEdit(self.centralwidget)
        self.LineEditSalesTax.setObjectName(u"LineEditSalesTax")
        self.LineEditSalesTax.setEnabled(False)
        self.LineEditSalesTax.setGeometry(QRect(140, 350, 113, 26))
        self.LineEditSalesTax.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.LineEditSalesTax.setReadOnly(True)
        self.LineEditTotalCost = QLineEdit(self.centralwidget)
        self.LineEditTotalCost.setObjectName(u"LineEditTotalCost")
        self.LineEditTotalCost.setEnabled(False)
        self.LineEditTotalCost.setGeometry(QRect(140, 390, 113, 26))
        self.LineEditTotalCost.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.LineEditTotalCost.setReadOnly(True)
        self.PushButtonCalcOrder = QPushButton(self.centralwidget)
        self.PushButtonCalcOrder.setObjectName(u"PushButtonCalcOrder")
        self.PushButtonCalcOrder.setGeometry(QRect(40, 250, 110, 26))
        self.PushButtonSubmitOrder = QPushButton(self.centralwidget)
        self.PushButtonSubmitOrder.setObjectName(u"PushButtonSubmitOrder")
        self.PushButtonSubmitOrder.setGeometry(QRect(200, 250, 110, 26))
        self.PushButtonExit = QPushButton(self.centralwidget)
        self.PushButtonExit.setObjectName(u"PushButtonExit")
        self.PushButtonExit.setGeometry(QRect(360, 250, 110, 26))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DroneDogs", None))
        self.LabelTitle.setText("")
        self.LabelLogo.setText("")
        self.LabelBeefDogs.setText(QCoreApplication.translate("MainWindow", u"# Beef Dogs", None))
        self.LabelPorkDogs.setText(QCoreApplication.translate("MainWindow", u"# Pork Dogs", None))
        self.LabelTurkeyDogs.setText(QCoreApplication.translate("MainWindow", u"# Turkey Dogs", None))
        self.LabelSubtotal.setText(QCoreApplication.translate("MainWindow", u"Subtotal:", None))
        self.LabelSalesTax.setText(QCoreApplication.translate("MainWindow", u"Sales Tax:", None))
        self.LabeTotalCost.setText(QCoreApplication.translate("MainWindow", u"Total Cost:", None))
        self.PushButtonCalcOrder.setText(QCoreApplication.translate("MainWindow", u"Calculate Order", None))
        self.PushButtonSubmitOrder.setText(QCoreApplication.translate("MainWindow", u"Submit Order", None))
        self.PushButtonExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

