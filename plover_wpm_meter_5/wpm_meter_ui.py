# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wpm_meter.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QHBoxLayout, QLCDNumber, QLabel,
    QSizePolicy, QSpacerItem, QWidget)
from plover_wpm_meter_5 import resources_rc

class Ui_WpmMeter(object):
    def setupUi(self, WpmMeter):
        if not WpmMeter.objectName():
            WpmMeter.setObjectName(u"WpmMeter")
        WpmMeter.resize(180, 151)
        self.layoutWidget = QWidget(WpmMeter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 30, 181, 121))
        self.wpm_meter = QGridLayout(self.layoutWidget)
        self.wpm_meter.setSpacing(0)
        self.wpm_meter.setContentsMargins(0, 0, 0, 0)
        self.wpm_meter.setObjectName(u"wpm_meter")
        self.wpm_meter.setContentsMargins(0, 0, 0, 0)
        self.wpm1 = QLCDNumber(self.layoutWidget)
        self.wpm1.setObjectName(u"wpm1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wpm1.sizePolicy().hasHeightForWidth())
        self.wpm1.setSizePolicy(sizePolicy)
        self.wpm1.setSegmentStyle(QLCDNumber.Flat)
        self.wpm1.setProperty(u"value", 0.000000000000000)

        self.wpm_meter.addWidget(self.wpm1, 0, 0, 1, 1)

        self.wpm1_label = QLabel(self.layoutWidget)
        self.wpm1_label.setObjectName(u"wpm1_label")
        self.wpm1_label.setAlignment(Qt.AlignCenter)

        self.wpm_meter.addWidget(self.wpm1_label, 0, 1, 1, 1)

        self.wpm2 = QLCDNumber(self.layoutWidget)
        self.wpm2.setObjectName(u"wpm2")
        self.wpm2.setSegmentStyle(QLCDNumber.Flat)
        self.wpm2.setProperty(u"value", 0.000000000000000)

        self.wpm_meter.addWidget(self.wpm2, 1, 0, 1, 1)

        self.wpm2_label = QLabel(self.layoutWidget)
        self.wpm2_label.setObjectName(u"wpm2_label")
        self.wpm2_label.setAlignment(Qt.AlignCenter)

        self.wpm_meter.addWidget(self.wpm2_label, 1, 1, 1, 1)

        self.wpm_meter.setColumnStretch(0, 2)
        self.wpm_meter.setColumnStretch(1, 1)
        self.layoutWidget1 = QWidget(WpmMeter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 181, 27))
        self.wpm_controls = QHBoxLayout(self.layoutWidget1)
        self.wpm_controls.setSpacing(-1)
        self.wpm_controls.setContentsMargins(0, 0, 0, 0)
        self.wpm_controls.setObjectName(u"wpm_controls")
        self.wpm_controls.setContentsMargins(0, 0, 0, 0)
        self.wpm_method = QComboBox(self.layoutWidget1)
        self.wpm_method.setObjectName(u"wpm_method")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wpm_method.sizePolicy().hasHeightForWidth())
        self.wpm_method.setSizePolicy(sizePolicy1)

        self.wpm_controls.addWidget(self.wpm_method)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.wpm_controls.addItem(self.horizontalSpacer)

        self.is_pinned_checkbox = QCheckBox(self.layoutWidget1)
        self.is_pinned_checkbox.setObjectName(u"is_pinned_checkbox")
        self.is_pinned_checkbox.setChecked(True)

        self.wpm_controls.addWidget(self.is_pinned_checkbox)


        self.retranslateUi(WpmMeter)

        QMetaObject.connectSlotsByName(WpmMeter)
    # setupUi

    def retranslateUi(self, WpmMeter):
        WpmMeter.setWindowTitle(QCoreApplication.translate("WpmMeter", u"WPM Meter", None))
        self.wpm1_label.setText(QCoreApplication.translate("WpmMeter", u"last 10s", None))
        self.wpm2_label.setText(QCoreApplication.translate("WpmMeter", u"last 1m", None))
        self.is_pinned_checkbox.setText(QCoreApplication.translate("WpmMeter", u"\ud83d\udccc", None))
    # retranslateUi

