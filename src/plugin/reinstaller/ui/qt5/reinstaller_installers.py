# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Repos\ModOrganizer-Plugins\src\plugin\reinstaller\ui\reinstaller_installers.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_reinstallerInstallers(object):
    def setupUi(self, reinstallerInstallers):
        reinstallerInstallers.setObjectName("reinstallerInstallers")
        reinstallerInstallers.resize(541, 336)
        reinstallerInstallers.setMinimumSize(QtCore.QSize(541, 336))
        self.verticalLayout = QtWidgets.QVBoxLayout(reinstallerInstallers)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(reinstallerInstallers)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(9, -1, 9, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_4)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.txtName = QtWidgets.QLineEdit(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtName.sizePolicy().hasHeightForWidth())
        self.txtName.setSizePolicy(sizePolicy)
        self.txtName.setObjectName("txtName")
        self.verticalLayout_3.addWidget(self.txtName)
        self.horizontalLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.ddlDownloads = QtWidgets.QComboBox(self.widget_5)
        self.ddlDownloads.setObjectName("ddlDownloads")
        self.verticalLayout_4.addWidget(self.ddlDownloads)
        self.horizontalLayout.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.widget_6)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.btnAdd = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout_5.addWidget(self.btnAdd)
        self.horizontalLayout.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(reinstallerInstallers)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.widget_7)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.lstInstallers = QtWidgets.QListWidget(self.widget_7)
        self.lstInstallers.setObjectName("lstInstallers")
        self.verticalLayout_6.addWidget(self.lstInstallers)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(reinstallerInstallers)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(9, -1, 9, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ddlInstaller = QtWidgets.QComboBox(self.widget_2)
        self.ddlInstaller.setObjectName("ddlInstaller")
        self.horizontalLayout_2.addWidget(self.ddlInstaller)
        self.btnInstall = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnInstall.sizePolicy().hasHeightForWidth())
        self.btnInstall.setSizePolicy(sizePolicy)
        self.btnInstall.setObjectName("btnInstall")
        self.horizontalLayout_2.addWidget(self.btnInstall)
        self.btnDelete = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout_2.addWidget(self.btnDelete)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(reinstallerInstallers)
        QtCore.QMetaObject.connectSlotsByName(reinstallerInstallers)

    def retranslateUi(self, reinstallerInstallers):
        _translate = QtCore.QCoreApplication.translate
        reinstallerInstallers.setWindowTitle(_translate("reinstallerInstallers", "Form"))
        self.label.setText(_translate("reinstallerInstallers", "Name"))
        self.label_2.setText(_translate("reinstallerInstallers", "Downloads"))
        self.btnAdd.setText(_translate("reinstallerInstallers", "Add"))
        self.label_4.setText(_translate("reinstallerInstallers", "Installers"))
        self.btnInstall.setText(_translate("reinstallerInstallers", "Install"))
        self.btnDelete.setText(_translate("reinstallerInstallers", "Delete"))
