# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'worker.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WorkerDialog(object):
    def setupUi(self, WorkerDialog):
        WorkerDialog.setObjectName("WorkerDialog")
        WorkerDialog.resize(298, 109)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(WorkerDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.fioLabel = QtWidgets.QLabel(WorkerDialog)
        self.fioLabel.setObjectName("fioLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.fioLabel)
        self.fioLineEdit = QtWidgets.QLineEdit(WorkerDialog)
        self.fioLineEdit.setObjectName("fioLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fioLineEdit)
        self.jobTitleLabel = QtWidgets.QLabel(WorkerDialog)
        self.jobTitleLabel.setObjectName("jobTitleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.jobTitleLabel)
        self.jobTitleLineEdit = QtWidgets.QLineEdit(WorkerDialog)
        self.jobTitleLineEdit.setObjectName("jobTitleLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.jobTitleLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CancelPushButton_3 = QtWidgets.QPushButton(WorkerDialog)
        self.CancelPushButton_3.setObjectName("CancelPushButton_3")
        self.horizontalLayout.addWidget(self.CancelPushButton_3)
        self.SavePushButton = QtWidgets.QPushButton(WorkerDialog)
        self.SavePushButton.setObjectName("SavePushButton")
        self.horizontalLayout.addWidget(self.SavePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(WorkerDialog)
        QtCore.QMetaObject.connectSlotsByName(WorkerDialog)

    def retranslateUi(self, WorkerDialog):
        _translate = QtCore.QCoreApplication.translate
        WorkerDialog.setWindowTitle(_translate("WorkerDialog", "Работник"))
        self.fioLabel.setText(_translate("WorkerDialog", "ФИО"))
        self.jobTitleLabel.setText(_translate("WorkerDialog", "Должность"))
        self.CancelPushButton_3.setText(_translate("WorkerDialog", "Отмена"))
        self.SavePushButton.setText(_translate("WorkerDialog", "Сохранить"))
