# -*- coding: utf-8 -*-


# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#import buttonSettingFunc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(837, 539)
        MainWindow.setObjectName("MainWindow")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 321, 221))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.SearchLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.SearchLayout.setContentsMargins(0, 0, 0, 0)
        self.SearchLayout.setObjectName("SearchLayout")

        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_Service = QtWidgets.QLabel(self.groupBox_2)
        self.label_Service.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.label_Service.setObjectName("label_Service")

        self.comboBox_smallService = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_smallService.setGeometry(QtCore.QRect(80, 60, 231, 21))
        self.comboBox_smallService.setObjectName("comboBox_smallService")

        self.label_City = QtWidgets.QLabel(self.groupBox_2)
        self.label_City.setGeometry(QtCore.QRect(40, 140, 41, 21))
        self.label_City.setObjectName("label_City")

        self.comboBox_Area = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_Area.setGeometry(QtCore.QRect(80, 100, 231, 21))
        self.comboBox_Area.setObjectName("comboBox_Area")

        self.comboBox_Service = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_Service.setGeometry(QtCore.QRect(80, 20, 151, 21))
        self.comboBox_Service.setAcceptDrops(False)
        self.comboBox_Service.setObjectName("comboBox_Service")

        self.label_Area = QtWidgets.QLabel(self.groupBox_2)
        self.label_Area.setGeometry(QtCore.QRect(50, 100, 31, 21))
        self.label_Area.setObjectName("label_Area")

        self.comboBox_City = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_City.setGeometry(QtCore.QRect(80, 140, 231, 21))
        self.comboBox_City.setObjectName("comboBox_City")

        self.label_smallService = QtWidgets.QLabel(self.groupBox_2)
        self.label_smallService.setGeometry(QtCore.QRect(40, 60, 41, 21))
        self.label_smallService.setObjectName("label_smallService")

        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(210, 172, 101, 31))
        self.pushButton.setObjectName("pushButton")

        self.SearchLayout.addWidget(self.groupBox_2)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(340, 10, 481, 221))
        self.listView.setObjectName("listView")



        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 240, 819, 249))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 817, 247))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(800, 0, 16, 241))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")

        self.graphicsView = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView.setGeometry(QtCore.QRect(10, 30, 321, 211))
        self.graphicsView.setObjectName("graphicsView")

        self.labelName = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelName.setGeometry(QtCore.QRect(10, 10, 31, 21))
        self.labelName.setObjectName("labelName")

        self.labelAddress_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelAddress_2.setGeometry(QtCore.QRect(350, 130, 24, 12))
        self.labelAddress_2.setObjectName("labelAddress_2")

        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setGeometry(QtCore.QRect(340, 120, 191, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(340, 10, 451, 111))
        self.groupBox.setObjectName("groupBox")

        self.labelNum = QtWidgets.QLabel(self.groupBox)
        self.labelNum.setGeometry(QtCore.QRect(10, 20, 52, 20))
        self.labelNum.setObjectName("labelNum")

        self.labePage = QtWidgets.QLabel(self.groupBox)
        self.labePage.setGeometry(QtCore.QRect(10, 50, 48, 12))
        self.labePage.setObjectName("labePage")

        self.labelAddress = QtWidgets.QLabel(self.groupBox)
        self.labelAddress.setGeometry(QtCore.QRect(20, 80, 36, 12))
        self.labelAddress.setObjectName("labelAddress")

        self.lineEditNum = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditNum.setGeometry(QtCore.QRect(70, 20, 371, 20))
        self.lineEditNum.setObjectName("lineEditNum")

        self.lineEditHome = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditHome.setGeometry(QtCore.QRect(70, 50, 371, 20))
        self.lineEditHome.setObjectName("lineEditHome")

        self.lineEditAddress = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditAddress.setGeometry(QtCore.QRect(70, 80, 371, 20))
        self.lineEditAddress.setObjectName("lineEditAddress")

        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 120, 241, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(350, 150, 431, 121))
        self.textEdit.setObjectName("textEdit")

        self.lineEditName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditName.setGeometry(QtCore.QRect(40, 10, 291, 20))
        self.lineEditName.setObjectName("lineEditName")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 837, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Search"))
        self.label_Service.setText(_translate("MainWindow", "서비스 분류"))
        self.label_City.setText(_translate("MainWindow", "시군구"))
        self.label_Area.setText(_translate("MainWindow", "지역"))
        self.label_smallService.setText(_translate("MainWindow", "소분류"))
        self.pushButton.setText(_translate("MainWindow", "검색"))
        self.labelName.setText(_translate("MainWindow", "이름"))
        self.labelAddress_2.setText(_translate("MainWindow", "개요"))
        self.groupBox.setTitle(_translate("MainWindow", "Info"))
        self.labelNum.setText(_translate("MainWindow", "우편번호"))
        self.labePage.setText(_translate("MainWindow", "홈페이지"))
        self.labelAddress.setText(_translate("MainWindow", "   주소"))
        self.pushButton_2.setText(_translate("MainWindow", "View Map"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

