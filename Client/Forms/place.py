# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'place.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlaceDialog(object):
    def setupUi(self, PlaceDialog):
        PlaceDialog.setObjectName("PlaceDialog")
        PlaceDialog.resize(313, 140)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(PlaceDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.NameLabel = QtWidgets.QLabel(PlaceDialog)
        self.NameLabel.setObjectName("NameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.NameLabel)
        self.NameLineEdit = QtWidgets.QLineEdit(PlaceDialog)
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.NameLineEdit)
        self.AddrecLabel = QtWidgets.QLabel(PlaceDialog)
        self.AddrecLabel.setObjectName("AddrecLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.AddrecLabel)
        self.AddresLineEdit = QtWidgets.QLineEdit(PlaceDialog)
        self.AddresLineEdit.setObjectName("AddresLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.AddresLineEdit)
        self.DetailsLabel = QtWidgets.QLabel(PlaceDialog)
        self.DetailsLabel.setObjectName("DetailsLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.DetailsLabel)
        self.DetailsLineEdit = QtWidgets.QLineEdit(PlaceDialog)
        self.DetailsLineEdit.setObjectName("DetailsLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.DetailsLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CancelPushButton_3 = QtWidgets.QPushButton(PlaceDialog)
        self.CancelPushButton_3.setObjectName("CancelPushButton_3")
        self.horizontalLayout.addWidget(self.CancelPushButton_3)
        self.SavePushButton = QtWidgets.QPushButton(PlaceDialog)
        self.SavePushButton.setObjectName("SavePushButton")
        self.horizontalLayout.addWidget(self.SavePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(PlaceDialog)
        QtCore.QMetaObject.connectSlotsByName(PlaceDialog)

    def retranslateUi(self, PlaceDialog):
        _translate = QtCore.QCoreApplication.translate
        PlaceDialog.setWindowTitle(_translate("PlaceDialog", "Место"))
        self.NameLabel.setText(_translate("PlaceDialog", "Название"))
        self.AddrecLabel.setText(_translate("PlaceDialog", "Адрес"))
        self.DetailsLabel.setText(_translate("PlaceDialog", "Дополнение"))
        self.CancelPushButton_3.setText(_translate("PlaceDialog", "Отмена"))
        self.SavePushButton.setText(_translate("PlaceDialog", "Сохранить"))
