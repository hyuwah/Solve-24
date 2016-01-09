# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solve24an.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(320, 240)
        Dialog.setMinimumSize(QtCore.QSize(320, 240))
        Dialog.setMaximumSize(QtCore.QSize(320, 240))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 60, 46, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 46, 22))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 46, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 46, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(150, 10, 61, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.bt_ok = QtGui.QPushButton(Dialog)
        self.bt_ok.setGeometry(QtCore.QRect(30, 190, 101, 23))
        self.bt_ok.setObjectName(_fromUtf8("bt_ok"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(150, 30, 141, 191))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 139, 189))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.out_cmbn = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.out_cmbn.setGeometry(QtCore.QRect(0, 0, 141, 191))
        self.out_cmbn.setAutoFillBackground(False)
        self.out_cmbn.setFrameShadow(QtGui.QFrame.Sunken)
        self.out_cmbn.setObjectName(_fromUtf8("out_cmbn"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.in_c1 = QtGui.QSpinBox(Dialog)
        self.in_c1.setGeometry(QtCore.QRect(90, 60, 42, 22))
        self.in_c1.setMinimum(1)
        self.in_c1.setMaximum(10)
        self.in_c1.setObjectName(_fromUtf8("in_c1"))
        self.in_c2 = QtGui.QSpinBox(Dialog)
        self.in_c2.setGeometry(QtCore.QRect(90, 90, 42, 22))
        self.in_c2.setMinimum(1)
        self.in_c2.setMaximum(10)
        self.in_c2.setObjectName(_fromUtf8("in_c2"))
        self.in_c3 = QtGui.QSpinBox(Dialog)
        self.in_c3.setGeometry(QtCore.QRect(90, 120, 42, 22))
        self.in_c3.setMinimum(1)
        self.in_c3.setMaximum(10)
        self.in_c3.setObjectName(_fromUtf8("in_c3"))
        self.in_c4 = QtGui.QSpinBox(Dialog)
        self.in_c4.setGeometry(QtCore.QRect(90, 150, 42, 22))
        self.in_c4.setMinimum(1)
        self.in_c4.setMaximum(10)
        self.in_c4.setObjectName(_fromUtf8("in_c4"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 20, 91, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Solve 24an", None))
        self.label.setText(_translate("Dialog", "Kartu 1: ", None))
        self.label_2.setText(_translate("Dialog", "Kartu 2:", None))
        self.label_3.setText(_translate("Dialog", "Kartu 3:", None))
        self.label_4.setText(_translate("Dialog", "Kartu 4: ", None))
        self.label_5.setText(_translate("Dialog", "Kombinasi: ", None))
        self.bt_ok.setText(_translate("Dialog", "OK", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Solve 24</span></p></body></html>", None))

