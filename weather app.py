# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apw.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json
import pyttsx3
#Created by @Omkar Kanse
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):#Created by @Omkar Kanse
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1047, 718)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-110, 80, 691, 481))
        self.label.setStyleSheet("image: url(:/we/wee.png);")
        self.label.setText("")#Created by @Omkar Kanse
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 531, 131))
        self.label_2.setStyleSheet("font: 75 48pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 460, 311, 61))
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"#Created by @Omkar Kanse
"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 560, 131, 41))
        self.pushButton.setStyleSheet("font: 75 16pt \"Times New Roman\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")#Created by @Omkar Kanse
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(570, 110, 391, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)#Created by @Omkar Kanse
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("image: url(:/map/map.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)#Created by @Omkar Kanse
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 75 16pt \"Times New Roman\";\n"
"color: rgb(0, 0, 0);")
        self.label_3.setText("")#Created by @Omkar Kanse
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("font: 75 16pt \"Times New Roman\";\n"
"color: rgb(0, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("font: 75 16pt \"Times New Roman\";\n"
"color: rgb(0, 0, 0);")
        self.label_6.setText("")#Created by @Omkar Kanse
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setStyleSheet("font: 75 16pt \"Times New Roman\";\n"
"color: rgb(0, 0, 0);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)#Created by @Omkar Kanse
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.api)

    def api(self):
        city = self.lineEdit.text()#Created by @Omkar Kanse
        url = f"https://api.weatherapi.com/v1/current.json?key=d795297768954c8389e112802232510&q={city}"
        r = requests.get(url)
        # print(r.text)
        w = json.loads(r.text)
        first = ("Region:" + " " + w["location"]["region"])
        self.label_3.setText(first)
        second = ("Country:" + " " + w["location"]["country"])
        self.label_5.setText(second)
        third = ("Weather Condtion:"+" " +(w["current"]["condition"]["text"]))
        self.label_6.setText(third)
        fourth = ("Temperature: " + str(w["current"]["temp_c"]) + "℃")
        five=(str(w["current"]["temp_c"]) + "℃")
        self.label_7.setText(fourth)#Created by @Omkar Kanse
        engine = pyttsx3.init()
        engine.say("The Current Weather in " + city + " is " + str(five))  # Created by @Omkar Kanse
        engine.runAndWait()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather Application"))
        self.label_2.setText(_translate("MainWindow", "Weather App"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter the city name"))
        self.pushButton.setText(_translate("MainWindow", "Check"))
import map_rc
import weather_rc#Created by @Omkar Kanse


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()#Created by @Omkar Kanse
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)#Created by @Omkar Kanse
    MainWindow.show()
    sys.exit(app.exec_())
