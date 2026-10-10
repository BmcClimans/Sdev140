# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fancy_drone_dogs_main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.LabelTitle = QLabel(self.centralwidget)
        self.LabelTitle.setObjectName(u"LabelTitle")
        self.LabelTitle.setGeometry(QRect(0, 0, 311, 121))
        self.LabelTitle.setPixmap(QPixmap(u"dronedogs_order_form_title_text.png"))
        self.LabelTitle.setScaledContents(True)
        self.LabelLogo = QLabel(self.centralwidget)
        self.LabelLogo.setObjectName(u"LabelLogo")
        self.LabelLogo.setGeometry(QRect(310, 0, 331, 191))
        self.LabelLogo.setPixmap(QPixmap(u"DroneDogsLogo.png"))
        self.LabelLogo.setScaledContents(True)
        self.FrameOrderSummary = QFrame(self.centralwidget)
        self.FrameOrderSummary.setObjectName(u"FrameOrderSummary")
        self.FrameOrderSummary.setGeometry(QRect(310, 200, 321, 161))
        self.FrameOrderSummary.setStyleSheet(u"QFrame {\n"
"    background-color: #2B2B2E;\n"
"    border-radius: 12px;\n"
"}")
        self.FrameOrderSummary.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameOrderSummary.setFrameShadow(QFrame.Shadow.Raised)
        self.PushButtonCalcOrder = QPushButton(self.FrameOrderSummary)
        self.PushButtonCalcOrder.setObjectName(u"PushButtonCalcOrder")
        self.PushButtonCalcOrder.setGeometry(QRect(50, 120, 221, 31))
        self.PushButtonCalcOrder.setStyleSheet(u"QPushButton {\n"
"    background-color: #B5121B;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D71920;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #850C14;\n"
"}")
        self.LabelOrderSummary = QLabel(self.FrameOrderSummary)
        self.LabelOrderSummary.setObjectName(u"LabelOrderSummary")
        self.LabelOrderSummary.setGeometry(QRect(10, 0, 111, 21))
        self.LabelSubtotal = QLabel(self.FrameOrderSummary)
        self.LabelSubtotal.setObjectName(u"LabelSubtotal")
        self.LabelSubtotal.setGeometry(QRect(20, 40, 49, 16))
        self.LabelSalesTax = QLabel(self.FrameOrderSummary)
        self.LabelSalesTax.setObjectName(u"LabelSalesTax")
        self.LabelSalesTax.setGeometry(QRect(20, 60, 81, 16))
        self.LabelTotal = QLabel(self.FrameOrderSummary)
        self.LabelTotal.setObjectName(u"LabelTotal")
        self.LabelTotal.setGeometry(QRect(20, 90, 49, 16))
        self.LineEditSubtotal = QLineEdit(self.FrameOrderSummary)
        self.LineEditSubtotal.setObjectName(u"LineEditSubtotal")
        self.LineEditSubtotal.setEnabled(False)
        self.LineEditSubtotal.setGeometry(QRect(180, 30, 113, 26))
        self.LineEditSubtotal.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.LineEditSubtotal.setReadOnly(True)
        self.LineEditSalesTax = QLineEdit(self.FrameOrderSummary)
        self.LineEditSalesTax.setObjectName(u"LineEditSalesTax")
        self.LineEditSalesTax.setEnabled(False)
        self.LineEditSalesTax.setGeometry(QRect(180, 60, 113, 26))
        self.LineEditSalesTax.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.LineEditSalesTax.setReadOnly(True)
        self.LineEditTotal = QLineEdit(self.FrameOrderSummary)
        self.LineEditTotal.setObjectName(u"LineEditTotal")
        self.LineEditTotal.setEnabled(False)
        self.LineEditTotal.setGeometry(QRect(180, 90, 113, 26))
        self.LineEditTotal.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.LineEditTotal.setReadOnly(True)
        self.FrameBeefDogs = QFrame(self.centralwidget)
        self.FrameBeefDogs.setObjectName(u"FrameBeefDogs")
        self.FrameBeefDogs.setGeometry(QRect(20, 180, 271, 61))
        self.FrameBeefDogs.setStyleSheet(u"QFrame {\n"
"    background-color: #2B2B2E;\n"
"    border-radius: 12px;\n"
"}")
        self.FrameBeefDogs.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameBeefDogs.setFrameShadow(QFrame.Shadow.Raised)
        self.LabelBeefDogs = QLabel(self.FrameBeefDogs)
        self.LabelBeefDogs.setObjectName(u"LabelBeefDogs")
        self.LabelBeefDogs.setGeometry(QRect(10, 0, 91, 51))
        self.SpinBoxBeefDogs = QSpinBox(self.FrameBeefDogs)
        self.SpinBoxBeefDogs.setObjectName(u"SpinBoxBeefDogs")
        self.SpinBoxBeefDogs.setGeometry(QRect(170, 10, 81, 31))
        self.SpinBoxBeefDogs.setMaximum(99)
        self.FramePorkDogs = QFrame(self.centralwidget)
        self.FramePorkDogs.setObjectName(u"FramePorkDogs")
        self.FramePorkDogs.setGeometry(QRect(20, 270, 271, 61))
        self.FramePorkDogs.setStyleSheet(u"QFrame {\n"
"    background-color: #2B2B2E;\n"
"    border-radius: 12px;\n"
"}")
        self.FramePorkDogs.setFrameShape(QFrame.Shape.StyledPanel)
        self.FramePorkDogs.setFrameShadow(QFrame.Shadow.Raised)
        self.LabelPorkDogs = QLabel(self.FramePorkDogs)
        self.LabelPorkDogs.setObjectName(u"LabelPorkDogs")
        self.LabelPorkDogs.setGeometry(QRect(10, 0, 91, 51))
        self.SpinBoxPorkDogs = QSpinBox(self.FramePorkDogs)
        self.SpinBoxPorkDogs.setObjectName(u"SpinBoxPorkDogs")
        self.SpinBoxPorkDogs.setGeometry(QRect(170, 10, 81, 31))
        self.SpinBoxPorkDogs.setMaximum(99)
        self.FrameHotDogs = QFrame(self.centralwidget)
        self.FrameHotDogs.setObjectName(u"FrameHotDogs")
        self.FrameHotDogs.setGeometry(QRect(20, 360, 271, 61))
        self.FrameHotDogs.setStyleSheet(u"QFrame {\n"
"    background-color: #2B2B2E;\n"
"    border-radius: 12px;\n"
"}")
        self.FrameHotDogs.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameHotDogs.setFrameShadow(QFrame.Shadow.Raised)
        self.LabelTurkeyDogs = QLabel(self.FrameHotDogs)
        self.LabelTurkeyDogs.setObjectName(u"LabelTurkeyDogs")
        self.LabelTurkeyDogs.setGeometry(QRect(10, 0, 111, 51))
        self.SpinBoxTurkeyDogs = QSpinBox(self.FrameHotDogs)
        self.SpinBoxTurkeyDogs.setObjectName(u"SpinBoxTurkeyDogs")
        self.SpinBoxTurkeyDogs.setGeometry(QRect(170, 10, 81, 31))
        self.SpinBoxTurkeyDogs.setMaximum(99)
        self.FrameOrderDivider = QFrame(self.centralwidget)
        self.FrameOrderDivider.setObjectName(u"FrameOrderDivider")
        self.FrameOrderDivider.setGeometry(QRect(20, 70, 271, 80))
        self.FrameOrderDivider.setFrameShape(QFrame.Shape.HLine)
        self.FrameOrderDivider.setFrameShadow(QFrame.Shadow.Raised)
        self.LabelBuildOrder = QLabel(self.FrameOrderDivider)
        self.LabelBuildOrder.setObjectName(u"LabelBuildOrder")
        self.LabelBuildOrder.setGeometry(QRect(50, 60, 171, 21))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.LabelBuildOrder.setFont(font1)
        self.LabelBuildOrder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.PushButtonSubmitOrder = QPushButton(self.centralwidget)
        self.PushButtonSubmitOrder.setObjectName(u"PushButtonSubmitOrder")
        self.PushButtonSubmitOrder.setGeometry(QRect(470, 380, 111, 26))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.PushButtonSubmitOrder.setFont(font2)
        self.PushButtonExit = QPushButton(self.centralwidget)
        self.PushButtonExit.setObjectName(u"PushButtonExit")
        self.PushButtonExit.setGeometry(QRect(370, 380, 81, 26))
        palette = QPalette()
        brush = QBrush(QColor(33, 33, 33, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        self.PushButtonExit.setPalette(palette)
        self.PushButtonExit.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.FrameOrderSummary.raise_()
        self.LabelTitle.raise_()
        self.LabelLogo.raise_()
        self.FrameBeefDogs.raise_()
        self.FramePorkDogs.raise_()
        self.FrameHotDogs.raise_()
        self.FrameOrderDivider.raise_()
        self.PushButtonSubmitOrder.raise_()
        self.PushButtonExit.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.SpinBoxBeefDogs, self.SpinBoxPorkDogs)
        QWidget.setTabOrder(self.SpinBoxPorkDogs, self.SpinBoxTurkeyDogs)
        QWidget.setTabOrder(self.SpinBoxTurkeyDogs, self.PushButtonCalcOrder)
        QWidget.setTabOrder(self.PushButtonCalcOrder, self.PushButtonExit)
        QWidget.setTabOrder(self.PushButtonExit, self.PushButtonSubmitOrder)
        QWidget.setTabOrder(self.PushButtonSubmitOrder, self.LineEditSubtotal)
        QWidget.setTabOrder(self.LineEditSubtotal, self.LineEditSalesTax)
        QWidget.setTabOrder(self.LineEditSalesTax, self.LineEditTotal)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BreeMcClimans- DroneDogs", None))
        self.LabelTitle.setText("")
        self.LabelLogo.setText("")
        self.PushButtonCalcOrder.setText(QCoreApplication.translate("MainWindow", u"Calculate Order", None))
        self.LabelOrderSummary.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Order Summary</span></p></body></html>", None))
        self.LabelSubtotal.setText(QCoreApplication.translate("MainWindow", u"Subtotal", None))
        self.LabelSalesTax.setText(QCoreApplication.translate("MainWindow", u"Sales tax (7%)", None))
        self.LabelTotal.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Total</span></p></body></html>", None))
        self.LabelBeefDogs.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Beef Hot Dogs</span></p><p>2.99 each</p></body></html>", None))
        self.LabelPorkDogs.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Pork Hot Dogs</span></p><p>2.99 each</p></body></html>", None))
        self.LabelTurkeyDogs.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Turkey Hot Dogs</span></p><p>2.99 each</p></body></html>", None))
        self.LabelBuildOrder.setText(QCoreApplication.translate("MainWindow", u"Build Your Order", None))
        self.PushButtonSubmitOrder.setText(QCoreApplication.translate("MainWindow", u"Submit Order", None))
        self.PushButtonExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

