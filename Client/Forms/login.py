# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(300, 95)
        LoginWindow.setMinimumSize(QtCore.QSize(300, 95))
        LoginWindow.setMaximumSize(QtCore.QSize(300, 95))
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.LabelLogin = QtWidgets.QLabel(self.centralwidget)
        self.LabelLogin.setObjectName("LabelLogin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.LabelLogin)
        self.LineEditLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEditLogin.setObjectName("LineEditLogin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.LineEditLogin)
        self.LabelPassword = QtWidgets.QLabel(self.centralwidget)
        self.LabelPassword.setObjectName("LabelPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.LabelPassword)
        self.LineEditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEditPassword.setObjectName("LineEditPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.LineEditPassword)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout_2.addWidget(self.loginButton)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Вход"))
        self.LabelLogin.setText(_translate("LoginWindow", "Логин"))
        self.LabelPassword.setText(_translate("LoginWindow", "Пароль"))
        self.loginButton.setText(_translate("LoginWindow", "Вход"))