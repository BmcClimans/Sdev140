# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_pt3.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(358, 450)
        self.LabelTitle = QLabel(Dialog)
        self.LabelTitle.setObjectName(u"LabelTitle")
        self.LabelTitle.setGeometry(QRect(0, 0, 351, 41))
        self.LabelTitle.setPixmap(QPixmap(u"dronedogs_order_form_title_text.png"))
        self.LabelTitle.setScaledContents(True)
        self.LabelLogo = QLabel(Dialog)
        self.LabelLogo.setObjectName(u"LabelLogo")
        self.LabelLogo.setGeometry(QRect(270, 40, 81, 191))
        self.LabelLogo.setPixmap(QPixmap(u"DroneDogsLogo.png"))
        self.LabelLogo.setScaledContents(True)
        self.LabelFirstName = QLabel(Dialog)
        self.LabelFirstName.setObjectName(u"LabelFirstName")
        self.LabelFirstName.setGeometry(QRect(28, 280, 61, 16))
        self.LabelLastName = QLabel(Dialog)
        self.LabelLastName.setObjectName(u"LabelLastName")
        self.LabelLastName.setGeometry(QRect(28, 320, 61, 16))
        self.LabelEmail = QLabel(Dialog)
        self.LabelEmail.setObjectName(u"LabelEmail")
        self.LabelEmail.setGeometry(QRect(28, 360, 49, 16))
        self.LineEditFirstName = QLineEdit(Dialog)
        self.LineEditFirstName.setObjectName(u"LineEditFirstName")
        self.LineEditFirstName.setGeometry(QRect(140, 270, 181, 26))
        self.LineEditLastName = QLineEdit(Dialog)
        self.LineEditLastName.setObjectName(u"LineEditLastName")
        self.LineEditLastName.setGeometry(QRect(140, 310, 181, 26))
        self.LineEditEmail = QLineEdit(Dialog)
        self.LineEditEmail.setObjectName(u"LineEditEmail")
        self.LineEditEmail.setGeometry(QRect(140, 350, 181, 26))
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(18, 250, 321, 191))
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: #2B2B2E;\n"
"    border-radius: 12px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.PushButtonSelectCustomer = QPushButton(self.frame)
        self.PushButtonSelectCustomer.setObjectName(u"PushButtonSelectCustomer")
        self.PushButtonSelectCustomer.setGeometry(QRect(180, 150, 121, 26))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.PushButtonSelectCustomer.setFont(font)
        self.PushButtonAddCustomer = QPushButton(self.frame)
        self.PushButtonAddCustomer.setObjectName(u"PushButtonAddCustomer")
        self.PushButtonAddCustomer.setGeometry(QRect(10, 150, 121, 26))
        self.PushButtonAddCustomer.setFont(font)
        self.ListWidgetCustomerList = QListWidget(Dialog)
        self.ListWidgetCustomerList.setObjectName(u"ListWidgetCustomerList")
        self.ListWidgetCustomerList.setGeometry(QRect(10, 40, 256, 192))
        self.frame.raise_()
        self.LabelTitle.raise_()
        self.LabelLogo.raise_()
        self.LabelFirstName.raise_()
        self.LabelLastName.raise_()
        self.LabelEmail.raise_()
        self.LineEditFirstName.raise_()
        self.LineEditLastName.raise_()
        self.LineEditEmail.raise_()
        self.ListWidgetCustomerList.raise_()
        QWidget.setTabOrder(self.ListWidgetCustomerList, self.LineEditFirstName)
        QWidget.setTabOrder(self.LineEditFirstName, self.LineEditLastName)
        QWidget.setTabOrder(self.LineEditLastName, self.LineEditEmail)
        QWidget.setTabOrder(self.LineEditEmail, self.PushButtonAddCustomer)
        QWidget.setTabOrder(self.PushButtonAddCustomer, self.PushButtonSelectCustomer)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.LabelTitle.setText("")
        self.LabelLogo.setText("")
        self.LabelFirstName.setText(QCoreApplication.translate("Dialog", u"First Name:", None))
        self.LabelLastName.setText(QCoreApplication.translate("Dialog", u"Last Name:", None))
        self.LabelEmail.setText(QCoreApplication.translate("Dialog", u"Email:", None))
        self.PushButtonSelectCustomer.setText(QCoreApplication.translate("Dialog", u"Select Customer", None))
        self.PushButtonAddCustomer.setText(QCoreApplication.translate("Dialog", u"Add Customer", None))
    # retranslateUi

