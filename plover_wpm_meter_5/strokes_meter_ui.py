# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'strokes_meter.ui'
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
import resources_rc

class Ui_StrokesMeter(object):
    def setupUi(self, StrokesMeter):
        if not StrokesMeter.objectName():
            StrokesMeter.setObjectName(u"StrokesMeter")
        StrokesMeter.resize(180, 151)
        self.layoutWidget = QWidget(StrokesMeter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 30, 181, 121))
        self.strokes_meter = QGridLayout(self.layoutWidget)
        self.strokes_meter.setSpacing(0)
        self.strokes_meter.setContentsMargins(0, 0, 0, 0)
        self.strokes_meter.setObjectName(u"strokes_meter")
        self.strokes_meter.setContentsMargins(0, 0, 0, 0)
        self.strokes1 = QLCDNumber(self.layoutWidget)
        self.strokes1.setObjectName(u"strokes1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.strokes1.sizePolicy().hasHeightForWidth())
        self.strokes1.setSizePolicy(sizePolicy)
        self.strokes1.setSegmentStyle(QLCDNumber.Flat)
        self.strokes1.setProperty(u"value", 0.000000000000000)

        self.strokes_meter.addWidget(self.strokes1, 0, 0, 1, 1)

        self.strokes1_label = QLabel(self.layoutWidget)
        self.strokes1_label.setObjectName(u"strokes1_label")
        self.strokes1_label.setAlignment(Qt.AlignCenter)

        self.strokes_meter.addWidget(self.strokes1_label, 0, 1, 1, 1)

        self.strokes2 = QLCDNumber(self.layoutWidget)
        self.strokes2.setObjectName(u"strokes2")
        self.strokes2.setSegmentStyle(QLCDNumber.Flat)
        self.strokes2.setProperty(u"value", 0.000000000000000)

        self.strokes_meter.addWidget(self.strokes2, 1, 0, 1, 1)

        self.strokes2_label = QLabel(self.layoutWidget)
        self.strokes2_label.setObjectName(u"strokes2_label")
        self.strokes2_label.setAlignment(Qt.AlignCenter)

        self.strokes_meter.addWidget(self.strokes2_label, 1, 1, 1, 1)

        self.strokes_meter.setColumnStretch(0, 2)
        self.strokes_meter.setColumnStretch(1, 1)
        self.layoutWidget1 = QWidget(StrokesMeter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 181, 27))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.strokes_method = QComboBox(self.layoutWidget1)
        self.strokes_method.setObjectName(u"strokes_method")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.strokes_method.sizePolicy().hasHeightForWidth())
        self.strokes_method.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.strokes_method)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.is_pinned_checkbox = QCheckBox(self.layoutWidget1)
        self.is_pinned_checkbox.setObjectName(u"is_pinned_checkbox")

        self.horizontalLayout.addWidget(self.is_pinned_checkbox)


        self.retranslateUi(StrokesMeter)

        QMetaObject.connectSlotsByName(StrokesMeter)
    # setupUi

    def retranslateUi(self, StrokesMeter):
        StrokesMeter.setWindowTitle(QCoreApplication.translate("StrokesMeter", u"Strokes Meter", None))
        self.strokes1_label.setText(QCoreApplication.translate("StrokesMeter", u"last 10s", None))
        self.strokes2_label.setText(QCoreApplication.translate("StrokesMeter", u"last 1m", None))
        self.is_pinned_checkbox.setText(QCoreApplication.translate("StrokesMeter", u"\ud83d\udccc", None))
    # retranslateUi

