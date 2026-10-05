# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mcclimansBreeanna_Dialogue.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_DialogBree(object):
    def setupUi(self, DialogBree):
        if not DialogBree.objectName():
            DialogBree.setObjectName(u"DialogBree")
        DialogBree.setEnabled(True)
        DialogBree.resize(640, 480)
        self.ButtonBoxBree = QDialogButtonBox(DialogBree)
        self.ButtonBoxBree.setObjectName(u"ButtonBoxBree")
        self.ButtonBoxBree.setGeometry(QRect(10, 440, 621, 32))
        self.ButtonBoxBree.setOrientation(Qt.Orientation.Horizontal)
        self.ButtonBoxBree.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        self.ButtonBoxBree.setCenterButtons(True)
        self.LineEditName = QLineEdit(DialogBree)
        self.LineEditName.setObjectName(u"LineEditName")
        self.LineEditName.setGeometry(QRect(130, 30, 341, 41))
        self.LineEditName.setToolTipDuration(5)
        self.LineEditName.setMaxLength(20)
        self.LabelName = QLabel(DialogBree)
        self.LabelName.setObjectName(u"LabelName")
        self.LabelName.setGeometry(QRect(20, 30, 91, 31))

        self.retranslateUi(DialogBree)
        self.ButtonBoxBree.accepted.connect(DialogBree.accept)
        self.ButtonBoxBree.rejected.connect(DialogBree.reject)

        QMetaObject.connectSlotsByName(DialogBree)
    # setupUi

    def retranslateUi(self, DialogBree):
        DialogBree.setWindowTitle(QCoreApplication.translate("DialogBree", u"Bree's Dialog", None))
#if QT_CONFIG(tooltip)
        self.LineEditName.setToolTip(QCoreApplication.translate("DialogBree", u"Enter your first name", None))
#endif // QT_CONFIG(tooltip)
        self.LineEditName.setPlaceholderText(QCoreApplication.translate("DialogBree", u"Enter First Name", None))
        self.LabelName.setText(QCoreApplication.translate("DialogBree", u"First Name", None))
    # retranslateUi

