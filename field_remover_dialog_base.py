# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'field_remover_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EmptyFieldRemoverDialogBase(object):
    def setupUi(self, EmptyFieldRemoverDialogBase):
        EmptyFieldRemoverDialogBase.setObjectName("EmptyFieldRemoverDialogBase")
        EmptyFieldRemoverDialogBase.resize(400, 300)
        self.button_box = QtWidgets.QDialogButtonBox(EmptyFieldRemoverDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.label = QtWidgets.QLabel(EmptyFieldRemoverDialogBase)
        self.label.setGeometry(QtCore.QRect(80, 130, 131, 20))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(EmptyFieldRemoverDialogBase)
        self.comboBox.setGeometry(QtCore.QRect(210, 130, 121, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(EmptyFieldRemoverDialogBase)
        self.button_box.accepted.connect(EmptyFieldRemoverDialogBase.accept)
        self.button_box.rejected.connect(EmptyFieldRemoverDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(EmptyFieldRemoverDialogBase)

    def retranslateUi(self, EmptyFieldRemoverDialogBase):
        _translate = QtCore.QCoreApplication.translate
        EmptyFieldRemoverDialogBase.setWindowTitle(_translate("EmptyFieldRemoverDialogBase", "Empty Field Rmover"))
        self.label.setText(_translate("EmptyFieldRemoverDialogBase", "Vector layer to remove fields from"))

