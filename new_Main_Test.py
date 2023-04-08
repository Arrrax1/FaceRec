from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 550)
        MainWindow.setMinimumSize(QtCore.QSize(900, 550))
        MainWindow.setMaximumSize(QtCore.QSize(900, 550))
        MainWindow.setStyleSheet("")
        self.defaultWindowFlags = MainWindow.windowFlags()
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(900, 550))
        self.centralwidget.setMaximumSize(QtCore.QSize(900, 550))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.shadow = QtWidgets.QWidget(self.page)
        self.shadow.setGeometry(QtCore.QRect(0, 0, 901, 551))
        self.shadow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.shadow.setStyleSheet("background-color: rgba(149, 1, 60,0.02);")
        self.shadow.setObjectName("shadow")
        self.input_frame = QtWidgets.QFrame(self.shadow)
        self.input_frame.setGeometry(QtCore.QRect(120, 80, 650, 401))
        self.input_frame.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.input_frame.setStyleSheet("border-radius: 25px;\n"
"background-color: rgb(255, 255, 255);")
        self.input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame.setLineWidth(1)
        self.input_frame.setObjectName("input_frame")
        self.label_logged = QtWidgets.QLabel(self.input_frame)
        self.label_logged.setGeometry(QtCore.QRect(390, 100, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_logged.setFont(font)
        self.label_logged.setStyleSheet("color: rgb(171, 8, 61);\n"
"background-color: rgba(0, 0, 0,0.0);")
        self.label_logged.setObjectName("label_logged")
        self.user_add = QtWidgets.QPushButton(self.input_frame)
        self.user_add.setGeometry(QtCore.QRect(100, 80, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.user_add.setFont(font)
        self.user_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.user_add.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(155, 33, 78);\n"
"border-radius:3px;\n"
"color: rgb(155, 33, 78);\n"
 
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155, 33, 78);\n"
"color:rgb(255,255,255);\n"
"}")
        self.user_add.setObjectName("user_add")
        self.start_btn = QtWidgets.QPushButton(self.input_frame)
        self.start_btn.setGeometry(QtCore.QRect(100, 280, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.start_btn.setFont(font)
        self.start_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_btn.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(155, 33, 78);\n"
"border-radius:3px;\n"
"color: rgb(155, 33, 78);\n"
 
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155, 33, 78);\n"
"color:rgb(255,255,255);\n"
"}")
        self.start_btn.setObjectName("start_btn")
        self.user_delete = QtWidgets.QPushButton(self.input_frame)
        self.user_delete.setGeometry(QtCore.QRect(70, 130, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.user_delete.setFont(font)
        self.user_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.user_delete.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(155, 33, 78);\n"
"border-radius:3px;\n"
"color: rgb(155, 33, 78);\n"
 
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155, 33, 78);\n"
"color:rgb(255,255,255);\n"
"}")
        self.user_delete.setObjectName("user_delete")
        self.user_upload = QtWidgets.QPushButton(self.input_frame)
        self.user_upload.setGeometry(QtCore.QRect(50, 180, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.user_upload.setFont(font)
        self.user_upload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.user_upload.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(155, 33, 78);\n"
"border-radius:3px;\n"
"color: rgb(155, 33, 78);\n"
 
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155, 33, 78);\n"
"color:rgb(255,255,255);\n"
"}")
        self.user_upload.setObjectName("user_upload")
        self.user_export = QtWidgets.QPushButton(self.input_frame)
        self.user_export.setGeometry(QtCore.QRect(70, 230, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.user_export.setFont(font)
        self.user_export.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.user_export.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(155, 33, 78);\n"
"border-radius:3px;\n"
"color: rgb(155, 33, 78);\n"
 
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155, 33, 78);\n"
"color:rgb(255,255,255);\n"
"}")
        self.user_export.setObjectName("user_export")
        self.current_user = QtWidgets.QLabel(self.input_frame)
        self.current_user.setGeometry(QtCore.QRect(350, 180, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.current_user.setFont(font)
        self.current_user.setStyleSheet("color: rgb(171, 8, 61);\n"
"background-color: rgba(0, 0, 0,0.0);\n"
"text-align : center;")
        self.current_user.setAlignment(QtCore.Qt.AlignCenter)
        self.current_user.setObjectName("current_user")
        self.user_rank = QtWidgets.QLabel(self.input_frame)
        self.user_rank.setGeometry(QtCore.QRect(350, 250, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.user_rank.setFont(font)
        self.user_rank.setStyleSheet("color: rgb(171, 8, 61);\n"
"background-color: rgba(0, 0, 0,0.0);\n"
"text-align : center;")
        self.user_rank.setAlignment(QtCore.Qt.AlignCenter)
        self.user_rank.setObjectName("user_rank")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 901, 551))
        self.label.setMinimumSize(QtCore.QSize(901, 551))
        self.label.setMaximumSize(QtCore.QSize(901, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./old-V/images/svg/svg.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.shadow.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.shadow_2 = QtWidgets.QWidget(self.page_2)
        self.shadow_2.setGeometry(QtCore.QRect(0, 0, 901, 551))
        self.shadow_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.shadow_2.setStyleSheet("background-color: rgba(149, 1, 60,0.02);")
        self.shadow_2.setObjectName("shadow_2")
        self.input_frame_2 = QtWidgets.QFrame(self.shadow_2)
        self.input_frame_2.setGeometry(QtCore.QRect(120, 80, 650, 391))
        self.input_frame_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.input_frame_2.setStyleSheet("border-radius: 25px;\n"
"background-color: rgb(255, 255, 255);")
        self.input_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame_2.setLineWidth(1)
        self.input_frame_2.setObjectName("input_frame_2")
        self.label_logged_2 = QtWidgets.QLabel(self.input_frame_2)
        self.label_logged_2.setGeometry(QtCore.QRect(360, 110, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_logged_2.setFont(font)
        self.label_logged_2.setStyleSheet("color: rgb(171, 8, 61);\n"
"background-color: rgba(0, 0, 0,0.0);")
        self.label_logged_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logged_2.setObjectName("label_logged_2")
        self.user_add_2 = QtWidgets.QPushButton(self.input_frame_2)
        self.user_add_2.setGeometry(QtCore.QRect(390, 220, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.user_add_2.setFont(font)
        self.user_add_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.user_add_2.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(155, 33, 78);\n"
"border-radius:3px;\n"
"color: rgb(155, 33, 78);\n"
 
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155, 33, 78);\n"
"color:rgb(255,255,255);\n"
"}")
        self.user_add_2.setObjectName("user_add_2")
        self.text_fullname = QtWidgets.QLineEdit(self.input_frame_2)
        self.text_fullname.setGeometry(QtCore.QRect(70, 70, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.text_fullname.setFont(font)
        self.text_fullname.setStyleSheet("border-bottom:1px solid rgb(149,1,60);\n"
"background-color: rgb(255, 244, 248);\n"
"padding:5px 10px;\n"
"border-top-left-radius :0;\n"
"border-top-right-radius : 15px;\n"
"border-bottom-left-radius : 15px; \n"
"border-bottom-right-radius : 0;\n"
"color:rgb(50,50,50);")
        self.text_fullname.setText("")
        self.text_fullname.setObjectName("text_fullname")
        self.text_email = QtWidgets.QLineEdit(self.input_frame_2)
        self.text_email.setGeometry(QtCore.QRect(70, 140, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.text_email.setFont(font)
        self.text_email.setStyleSheet("border-bottom:1px solid rgb(149,1,60);\n"
"background-color: rgb(255, 244, 248);\n"
"padding:5px 10px;\n"
"border-top-left-radius :0;\n"
"border-top-right-radius : 15px;\n"
"border-bottom-left-radius : 15px; \n"
"border-bottom-right-radius : 0;\n"
"color:rgb(50,50,50);")
        self.text_email.setText("")
        self.text_email.setObjectName("text_email")
        self.text_password = QtWidgets.QLineEdit(self.input_frame_2)
        self.text_password.setGeometry(QtCore.QRect(70, 210, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.text_password.setFont(font)
        self.text_password.setStyleSheet("border-bottom:1px solid rgb(149,1,60);\n"
"background-color: rgb(255, 244, 248);\n"
"padding:5px 10px;\n"
"border-top-left-radius :0;\n"
"border-top-right-radius : 15px;\n"
"border-bottom-left-radius : 15px; \n"
"border-bottom-right-radius : 0;\n"
"color:rgb(50,50,50);")
        self.text_password.setText("")
        self.text_password.setObjectName("text_password")
        self.text_confirm = QtWidgets.QLineEdit(self.input_frame_2)
        self.text_confirm.setGeometry(QtCore.QRect(70, 280, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.text_confirm.setFont(font)
        self.text_confirm.setStyleSheet("border-bottom:1px solid rgb(149,1,60);\n"
"background-color: rgb(255, 244, 248);\n"
"padding:5px 10px;\n"
"border-top-left-radius :0;\n"
"border-top-right-radius : 15px;\n"
"border-bottom-left-radius : 15px; \n"
"border-bottom-right-radius : 0;\n"
"color:rgb(50,50,50);")
        self.text_confirm.setText("")
        self.text_confirm.setObjectName("text_confirm")
        self.label_logged_3 = QtWidgets.QLabel(self.input_frame_2)
        self.label_logged_3.setGeometry(QtCore.QRect(70, 40, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_logged_3.setFont(font)
        self.label_logged_3.setStyleSheet("color: rgb(171, 8, 61);\n"
"background-color: rgba(0, 0, 0,0.0);")
        self.label_logged_3.setObjectName("label_logged_3")
        self.label_logged_4 = QtWidgets.QLabel(self.input_frame_2)
        self.label_logged_4.setGeometry(QtCore.QRect(70, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_logged_4.setFont(font)
        self.label_logged_4.setStyleSheet("color: rgb(171, 8, 61);\n"
"background-color: rgba(0, 0, 0,0.0);")
        self.label_logged_4.setObjectName("label_logged_4")
        self.label_logged_5 = QtWidgets.QLabel(self.input_frame_2)
        self.label_logged_5.setGeometry(QtCore.QRect(70, 180, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_logged_5.setFont(font)
        self.label_logged_5.setStyleSheet("color: rgb(171, 8, 61);\n"
"background-color: rgba(0, 0, 0,0.0);")
        self.label_logged_5.setObjectName("label_logged_5")
        self.label_logged_6 = QtWidgets.QLabel(self.input_frame_2)
        self.label_logged_6.setGeometry(QtCore.QRect(70, 250, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_logged_6.setFont(font)
        self.label_logged_6.setStyleSheet("color: rgb(171, 8, 61);\n"
"background-color: rgba(0, 0, 0,0.0);")
        self.label_logged_6.setObjectName("label_logged_6")
        self.error_label = QtWidgets.QLabel(self.input_frame_2)
        self.error_label.setGeometry(QtCore.QRect(420, 270, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet("color: rgb(50, 50, 50);\n"
"background-color: rgba(0, 0, 0,0.0);")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.return_btn = QtWidgets.QPushButton(self.input_frame_2)
        self.return_btn.setGeometry(QtCore.QRect(570, 20, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.return_btn.setFont(font)
        self.return_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.return_btn.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(155, 33, 78);\n"
"border-radius:3px;\n"
"color: rgb(155, 33, 78);\n"
 
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155, 33, 78);\n"
"color:rgb(255,255,255);\n"
"}")
        self.return_btn.setObjectName("return_btn")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 901, 551))
        self.label_2.setMinimumSize(QtCore.QSize(901, 551))
        self.label_2.setMaximumSize(QtCore.QSize(901, 551))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./old-V/images/svg/svg.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.shadow_2.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        # self.user_add.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.user_add.clicked.connect(lambda : self.openNewUser(MainWindow))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openNewUser(self, MainWindow):
        #MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        #MainWindow.setWindowFlags(self.defaultWindowFlags)
        MainWindow.setWindowFlags(QtCore.Qt.WindowType.CustomizeWindowHint | QtCore.Qt.WindowType.WindowCloseButtonHint | QtCore.Qt.WindowType.WindowMinimizeButtonHint |QtCore.Qt.WindowType.WindowMaximizeButtonHint) 
        MainWindow.setMinimumSize(QtCore.QSize(300, 250))
        MainWindow.setMaximumSize(QtCore.QSize(10000, 10550))
        MainWindow.show()
        # self.stackedWidget.setCurrentWidget(self.page_2)
        # self. .setWindowFlags(Qt.FramelessWindowHint)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_logged.setText(_translate("MainWindow", "Logged in as :"))
        self.user_add.setText(_translate("MainWindow", "Add User"))
        self.start_btn.setText(_translate("MainWindow", "Use App"))
        self.user_delete.setText(_translate("MainWindow", "Delete User"))
        self.user_upload.setText(_translate("MainWindow", "Upload Data"))
        self.user_export.setText(_translate("MainWindow", "Export Data"))
        self.current_user.setText(_translate("MainWindow", "Youcef Rida"))
        self.user_rank.setText(_translate("MainWindow", "Lieutenant"))
        self.label_logged_2.setText(_translate("MainWindow", "Please fill in\n"
"the informations"))
        self.user_add_2.setText(_translate("MainWindow", "Add User"))
        self.label_logged_3.setText(_translate("MainWindow", "Full Name :"))
        self.label_logged_4.setText(_translate("MainWindow", "Email :"))
        self.label_logged_5.setText(_translate("MainWindow", "Password :"))
        self.label_logged_6.setText(_translate("MainWindow", "Confirm Password :"))
        self.error_label.setText(_translate("MainWindow", "User Added"))
        self.return_btn.setText(_translate("MainWindow", "⮑"))

class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()

    def mousePressEvent(self, event):                                 # +
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):                                  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

      import sys
      app = QtWidgets.QApplication(sys.argv)
        # MainWindow = QtWidgets.QMainWindow()
        # ui = Ui_MainWindow()
        # ui.setupUi(MainWindow)
        # MainWindow.show()
      w = MyWin()
      w.show()
      sys.exit(app.exec_())
