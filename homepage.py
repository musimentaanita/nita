# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homepage(object):
    def setupUi(self, homepage):
        homepage.setObjectName("homepage")
        homepage.resize(1031, 657)
        self.centralwidget = QtWidgets.QWidget(homepage)
        self.centralwidget.setObjectName("centralwidget")
        self.toolbar = QtWidgets.QWidget(self.centralwidget)
        self.toolbar.setGeometry(QtCore.QRect(0, 30, 211, 591))
        self.toolbar.setStyleSheet("background-color: rgb(255,255,255);")
        self.toolbar.setObjectName("toolbar")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.toolbar)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 190, 221, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setMinimumSize(QtCore.QSize(5, 5))
        self.toolButton.setStyleSheet("color: black; font: bold 12pt;")
        self.toolButton.setCheckable(True)
        self.toolButton.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout.addWidget(self.toolButton)
        self.supplierbtn = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.supplierbtn.sizePolicy().hasHeightForWidth())
        self.supplierbtn.setSizePolicy(sizePolicy)
        self.supplierbtn.setMinimumSize(QtCore.QSize(5, 5))
        self.supplierbtn.setStyleSheet("color: rgb(0,0,0); font: bold 12pt\"Cantarell\";border:none;")
        self.supplierbtn.setObjectName("supplierbtn")
        self.verticalLayout.addWidget(self.supplierbtn)
        self.inventorybtn = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inventorybtn.sizePolicy().hasHeightForWidth())
        self.inventorybtn.setSizePolicy(sizePolicy)
        self.inventorybtn.setStyleSheet("color: black;\n"
"font: bold 12pt \"Cantarell\";border: none;\n"
"")
        self.inventorybtn.setObjectName("inventorybtn")
        self.verticalLayout.addWidget(self.inventorybtn)
        self.staffbtn = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.staffbtn.sizePolicy().hasHeightForWidth())
        self.staffbtn.setSizePolicy(sizePolicy)
        self.staffbtn.setMinimumSize(QtCore.QSize(5, 0))
        self.staffbtn.setStyleSheet("color: rgb(0, 0, 0); font: bold 12pt \"Cantarell\";border: none;")
        self.staffbtn.setObjectName("staffbtn")
        self.verticalLayout.addWidget(self.staffbtn)
        self.expensebtn = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expensebtn.sizePolicy().hasHeightForWidth())
        self.expensebtn.setSizePolicy(sizePolicy)
        self.expensebtn.setStyleSheet("color: rgb(0, 0, 0); font: bold 12pt \"Cantarell\";border: none;\n"
"\n"
"")
        self.expensebtn.setObjectName("expensebtn")
        self.verticalLayout.addWidget(self.expensebtn)
        self.salesbtn = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.salesbtn.sizePolicy().hasHeightForWidth())
        self.salesbtn.setSizePolicy(sizePolicy)
        self.salesbtn.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: bold 12pt \"Cantarell\";border: none;")
        self.salesbtn.setObjectName("salesbtn")
        self.verticalLayout.addWidget(self.salesbtn)
        self.reportbtn = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reportbtn.sizePolicy().hasHeightForWidth())
        self.reportbtn.setSizePolicy(sizePolicy)
        self.reportbtn.setStyleSheet("color: rgb(0, 0, 0); font: bold 12pt \"Cantarell\";border: none;")
        self.reportbtn.setObjectName("reportbtn")
        self.verticalLayout.addWidget(self.reportbtn)
        self.settingsbtn = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsbtn.sizePolicy().hasHeightForWidth())
        self.settingsbtn.setSizePolicy(sizePolicy)
        self.settingsbtn.setStyleSheet("color: rgb(0, 0, 0); font: bold 12pt \"Cantarell\";border: none;")
        self.settingsbtn.setObjectName("settingsbtn")
        self.verticalLayout.addWidget(self.settingsbtn)
        self.logoutbtn = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.logoutbtn.setStyleSheet("color: black; font: bold 12pt;border:none;")
        self.logoutbtn.setObjectName("logoutbtn")
        self.verticalLayout.addWidget(self.logoutbtn)
        self.image_widget = QtWidgets.QWidget(self.toolbar)
        self.image_widget.setGeometry(QtCore.QRect(10, 10, 191, 151))
        self.image_widget.setStyleSheet("image: url(:/image_widget/images/bgdimage2.jpeg);")
        self.image_widget.setObjectName("image_widget")
        self.label_2 = QtWidgets.QLabel(self.toolbar)
        self.label_2.setGeometry(QtCore.QRect(200, 60, 66, 19))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(880, 0, 151, 31))
        self.comboBox.setStyleSheet(" border: none; color: black;\n"
"background-color: rgb(246, 211, 45);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1200, 31))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black; font: bold 15pt;")
        self.label.setIndent(100)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 30, 821, 591))
        self.label_3.setStyleSheet("background-image: url(:/image_widget/images/bgdimage6.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 90, 66, 19))
        self.label_4.setStyleSheet("background-color:white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 60, 191, 121))
        self.label_5.setStyleSheet("border-radius: 20px;background-color: white; font: red;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(520, 250, 191, 121))
        self.label_6.setStyleSheet("border-radius: 20px;background-color: white; font: red;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(780, 60, 191, 121))
        self.label_7.setStyleSheet("border-radius: 20px;background-color: white; font: red;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(790, 430, 191, 121))
        self.label_8.setStyleSheet("border-radius:20px;background-color: white; font: red;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(250, 440, 191, 121))
        self.label_9.setStyleSheet("border-radius: 20px;background-color: white; font: red;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(290, 60, 71, 31))
        self.label_10.setStyleSheet("color: red;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(580, 260, 71, 31))
        self.label_11.setStyleSheet("color: red;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(850, 440, 71, 31))
        self.label_12.setStyleSheet("color: red;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(840, 80, 91, 31))
        self.label_13.setStyleSheet("color: red;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(300, 460, 71, 31))
        self.label_14.setStyleSheet("color: red;")
        self.label_14.setObjectName("label_14")
        self.label_3.raise_()
        self.toolbar.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        homepage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(homepage)
        self.statusbar.setObjectName("statusbar")
        homepage.setStatusBar(self.statusbar)

        self.retranslateUi(homepage)
        QtCore.QMetaObject.connectSlotsByName(homepage)

    def retranslateUi(self, homepage):
        _translate = QtCore.QCoreApplication.translate
        homepage.setWindowTitle(_translate("homepage", "MainWindow"))
        self.toolButton.setText(_translate("homepage", "Home"))
        self.supplierbtn.setText(_translate("homepage", "Supplier"))
        self.inventorybtn.setText(_translate("homepage", "Inventory"))
        self.staffbtn.setText(_translate("homepage", "Staff"))
        self.expensebtn.setText(_translate("homepage", "Expenses"))
        self.salesbtn.setText(_translate("homepage", "Sales"))
        self.reportbtn.setText(_translate("homepage", "Reports"))
        self.settingsbtn.setText(_translate("homepage", "Settings"))
        self.logoutbtn.setText(_translate("homepage", "Logout"))
        self.label_2.setText(_translate("homepage", "TextLabel"))
        self.comboBox.setItemText(0, _translate("homepage", "Ware house worker"))
        self.comboBox.setItemText(1, _translate("homepage", "Supplier"))
        self.comboBox.setItemText(2, _translate("homepage", "Customer"))
        self.comboBox.setItemText(3, _translate("homepage", "Administrator"))
        self.label.setText(_translate("homepage", "                                                DRUG INVENTORY MANAGEMENT  "))
        self.label_4.setText(_translate("homepage", "TextLabel"))
        self.label_10.setText(_translate("homepage", "Suppliers"))
        self.label_11.setText(_translate("homepage", "Inventory"))
        self.label_12.setText(_translate("homepage", "Expenses"))
        self.label_13.setText(_translate("homepage", "Destinations"))
        self.label_14.setText(_translate("homepage", "Contacts"))
import images