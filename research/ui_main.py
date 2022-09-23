# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(592, 107)
        MainWindow.setStyleSheet(u"background-color: rgb(222, 222, 222);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_endereco = QLineEdit(self.centralwidget)
        self.txt_endereco.setObjectName(u"txt_endereco")
        self.txt_endereco.setEnabled(True)

        self.horizontalLayout.addWidget(self.txt_endereco)

        self.webcam = QCheckBox(self.centralwidget)
        self.webcam.setObjectName(u"webcam")

        self.horizontalLayout.addWidget(self.webcam)

        self.btn_conectar = QPushButton(self.centralwidget)
        self.btn_conectar.setObjectName(u"btn_conectar")
        self.btn_conectar.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")

        self.horizontalLayout.addWidget(self.btn_conectar)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.checkBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#000000;\">Endere\u00e7o C\u00e2mera </span><span style=\" font-size:9pt; font-weight:600; color:#000000;\">IP </span></p></body></html>", None))
        self.txt_endereco.setInputMask("")
        self.txt_endereco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex.: http://88.53.197.250//axis-cgi/mjpg/video.cgi?resolution=320x240", None))
        self.webcam.setText(QCoreApplication.translate("MainWindow", u"Webcam", None))
        self.btn_conectar.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Notifica\u00e7\u00f5es</span></p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Silenciosa", None))
    # retranslateUi

