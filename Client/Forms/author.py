# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AuthorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthorDialog(object):
    def setupUi(self, AuthorDialog):
        AuthorDialog.setObjectName("AuthorDialog")
        AuthorDialog.resize(298, 109)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AuthorDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.fioLabel = QtWidgets.QLabel(AuthorDialog)
        self.fioLabel.setObjectName("fioLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.fioLabel)
        self.fioLineEdit = QtWidgets.QLineEdit(AuthorDialog)
        self.fioLineEdit.setObjectName("fioLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fioLineEdit)
        self.jobTitleLabel = QtWidgets.QLabel(AuthorDialog)
        self.jobTitleLabel.setObjectName("jobTitleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.jobTitleLabel)
        self.jobTitleLineEdit = QtWidgets.QLineEdit(AuthorDialog)
        self.jobTitleLineEdit.setObjectName("jobTitleLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.jobTitleLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CancelPushButton_3 = QtWidgets.QPushButton(AuthorDialog)
        self.CancelPushButton_3.setObjectName("CancelPushButton_3")
        self.horizontalLayout.addWidget(self.CancelPushButton_3)
        self.SavePushButton = QtWidgets.QPushButton(AuthorDialog)
        self.SavePushButton.setObjectName("SavePushButton")
        self.horizontalLayout.addWidget(self.SavePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(AuthorDialog)
        QtCore.QMetaObject.connectSlotsByName(AuthorDialog)

    def retranslateUi(self, AuthorDialog):
        _translate = QtCore.QCoreApplication.translate
        AuthorDialog.setWindowTitle(_translate("AuthorDialog", "Автор"))
        self.fioLabel.setText(_translate("AuthorDialog", "ФИО"))
        self.jobTitleLabel.setText(_translate("AuthorDialog", "Должность"))
        self.CancelPushButton_3.setText(_translate("AuthorDialog", "Отмена"))
        self.SavePushButton.setText(_translate("AuthorDialog", "Сохранить"))

