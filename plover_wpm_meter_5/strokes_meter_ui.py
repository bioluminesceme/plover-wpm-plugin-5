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
from plover_wpm_meter_5 import resources_rc

class Ui_StrokesMeter(object):
    def setupUi(self, StrokesMeter):
        print("Ui_StrokesMeter.setupUi: Starting")
        if not StrokesMeter.objectName():
            StrokesMeter.setObjectName(u"StrokesMeter")
        print("Ui_StrokesMeter.setupUi: Set object name")
        StrokesMeter.resize(180, 151)
        print("Ui_StrokesMeter.setupUi: Resized window")
        self.layoutWidget = QWidget(StrokesMeter)
        print("Ui_StrokesMeter.setupUi: Created layoutWidget")
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 30, 181, 121))
        print("Ui_StrokesMeter.setupUi: Creating QGridLayout")
        self.strokes_meter = QGridLayout(self.layoutWidget)
        self.strokes_meter.setSpacing(0)
        self.strokes_meter.setContentsMargins(0, 0, 0, 0)
        self.strokes_meter.setObjectName(u"strokes_meter")
        self.strokes_meter.setContentsMargins(0, 0, 0, 0)
        print("Ui_StrokesMeter.setupUi: Creating QLCDNumber strokes1")
        self.strokes1 = QLCDNumber(self.layoutWidget)
        print("Ui_StrokesMeter.setupUi: QLCDNumber strokes1 created")
        self.strokes1.setObjectName(u"strokes1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.strokes1.sizePolicy().hasHeightForWidth())
        self.strokes1.setSizePolicy(sizePolicy)
        print("Ui_StrokesMeter.setupUi: Setting strokes1 segment style")
        self.strokes1.setSegmentStyle(QLCDNumber.Flat)
        print("Ui_StrokesMeter.setupUi: Setting strokes1 value property")
        self.strokes1.setProperty(u"value", 0.000000000000000)
        print("Ui_StrokesMeter.setupUi: Adding strokes1 to grid")

        self.strokes_meter.addWidget(self.strokes1, 0, 0, 1, 1)
        print("Ui_StrokesMeter.setupUi: strokes1 added to grid")

        print("Ui_StrokesMeter.setupUi: Creating strokes1_label")
        self.strokes1_label = QLabel(self.layoutWidget)
        self.strokes1_label.setObjectName(u"strokes1_label")
        self.strokes1_label.setAlignment(Qt.AlignCenter)
        print("Ui_StrokesMeter.setupUi: strokes1_label created")

        self.strokes_meter.addWidget(self.strokes1_label, 0, 1, 1, 1)
        print("Ui_StrokesMeter.setupUi: strokes1_label added to grid")

        print("Ui_StrokesMeter.setupUi: Creating QLCDNumber strokes2")
        self.strokes2 = QLCDNumber(self.layoutWidget)
        print("Ui_StrokesMeter.setupUi: QLCDNumber strokes2 created")
        self.strokes2.setObjectName(u"strokes2")
        print("Ui_StrokesMeter.setupUi: Setting strokes2 segment style")
        self.strokes2.setSegmentStyle(QLCDNumber.Flat)
        print("Ui_StrokesMeter.setupUi: Setting strokes2 value")
        self.strokes2.setProperty(u"value", 0.000000000000000)
        print("Ui_StrokesMeter.setupUi: Adding strokes2 to grid")

        self.strokes_meter.addWidget(self.strokes2, 1, 0, 1, 1)
        print("Ui_StrokesMeter.setupUi: strokes2 added to grid")

        print("Ui_StrokesMeter.setupUi: Creating strokes2_label")
        self.strokes2_label = QLabel(self.layoutWidget)
        print("Ui_StrokesMeter.setupUi: strokes2_label created")
        self.strokes2_label.setObjectName(u"strokes2_label")
        self.strokes2_label.setAlignment(Qt.AlignCenter)

        self.strokes_meter.addWidget(self.strokes2_label, 1, 1, 1, 1)
        print("Ui_StrokesMeter.setupUi: strokes2_label added to grid")

        print("Ui_StrokesMeter.setupUi: Setting column stretches")
        self.strokes_meter.setColumnStretch(0, 2)
        self.strokes_meter.setColumnStretch(1, 1)
        print("Ui_StrokesMeter.setupUi: Creating layoutWidget1")
        self.layoutWidget1 = QWidget(StrokesMeter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 181, 27))
        print("Ui_StrokesMeter.setupUi: Creating horizontalLayout")
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        print("Ui_StrokesMeter.setupUi: horizontalLayout created")
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        print("Ui_StrokesMeter.setupUi: Creating strokes_method QComboBox")
        self.strokes_method = QComboBox(self.layoutWidget1)
        self.strokes_method.setObjectName(u"strokes_method")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.strokes_method.sizePolicy().hasHeightForWidth())
        self.strokes_method.setSizePolicy(sizePolicy1)
        print("Ui_StrokesMeter.setupUi: Adding strokes_method to layout")

        self.horizontalLayout.addWidget(self.strokes_method)

        print("Ui_StrokesMeter.setupUi: Creating horizontal spacer")
        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        print("Ui_StrokesMeter.setupUi: Creating is_pinned_checkbox")
        self.is_pinned_checkbox = QCheckBox(self.layoutWidget1)
        self.is_pinned_checkbox.setObjectName(u"is_pinned_checkbox")
        print("Ui_StrokesMeter.setupUi: Adding is_pinned_checkbox to layout")

        self.horizontalLayout.addWidget(self.is_pinned_checkbox)
        print("Ui_StrokesMeter.setupUi: All widgets created")


        print("Ui_StrokesMeter.setupUi: Calling retranslateUi")
        self.retranslateUi(StrokesMeter)
        print("Ui_StrokesMeter.setupUi: retranslateUi completed")

        print("Ui_StrokesMeter.setupUi: Calling connectSlotsByName")
        QMetaObject.connectSlotsByName(StrokesMeter)
        print("Ui_StrokesMeter.setupUi: COMPLETED SUCCESSFULLY")
    # setupUi

    def retranslateUi(self, StrokesMeter):
        StrokesMeter.setWindowTitle(QCoreApplication.translate("StrokesMeter", u"Strokes Meter", None))
        self.strokes1_label.setText(QCoreApplication.translate("StrokesMeter", u"last 10s", None))
        self.strokes2_label.setText(QCoreApplication.translate("StrokesMeter", u"last 1m", None))
        # IMPORTANT: DO NOT USE EMOJI - causes crash in PySide6 on Windows
        # Original: self.is_pinned_checkbox.setText(QCoreApplication.translate("StrokesMeter", u"\ud83d\udccc", None))
        self.is_pinned_checkbox.setText("Pin")
    # retranslateUi

