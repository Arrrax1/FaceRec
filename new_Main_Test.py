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
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(900, 550))
        self.centralwidget.setMaximumSize(QtCore.QSize(900, 550))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.login_panel = QtWidgets.QWidget()
        self.login_panel.setObjectName("login_panel")
        self.shadow_3 = QtWidgets.QWidget(self.login_panel)
        self.shadow_3.setGeometry(QtCore.QRect(0, 0, 901, 551))
        self.shadow_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.shadow_3.setStyleSheet("background-color: rgba(149, 1, 60,0.02);")
        self.shadow_3.setObjectName("shadow_3")
        self.input_frame_3 = QtWidgets.QFrame(self.login_panel)
        self.input_frame_3.setGeometry(QtCore.QRect(275, 120, 350, 281))
        self.input_frame_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.input_frame_3.setStyleSheet("border-radius: 25px;\n"
"background-color: rgb(255, 255, 255);")
        self.input_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame_3.setLineWidth(1)
        self.input_frame_3.setObjectName("input_frame_3")
        self.buttons_frame = QtWidgets.QFrame(self.input_frame_3)
        self.buttons_frame.setGeometry(QtCore.QRect(30, 200, 291, 81))
        self.buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons_frame.setObjectName("buttons_frame")
        self.pushButton = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton.setGeometry(QtCore.QRect(100, 0, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border: 2px solid rgba(17, 94, 8,0.7);\n"
"border-radius:3px;\n"
"color:rgba(0,0,0,0.8);\n"

"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgba(17, 94, 8,0.6);\n"
"color:rgb(255,255,255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 40, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgba(177, 0, 2,0.9);\n"
"color:rgb(255,255,255);\n"
"border-radius:3px;\n"

"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(144,12,62);\n"
"color:rgb(255,255,255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.username_input = QtWidgets.QLineEdit(self.input_frame_3)
        self.username_input.setGeometry(QtCore.QRect(70, 60, 210, 41))
        self.username_input.setStyleSheet("border : 1px solid rgba(0,0,0,0.2);\n"
"border-radius: 7px;")
        self.username_input.setAlignment(QtCore.Qt.AlignCenter)
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(self.input_frame_3)
        self.password_input.setGeometry(QtCore.QRect(70, 140, 211, 41))
        self.password_input.setStyleSheet("border : 1px solid rgba(0,0,0,0.2);\n"
"border-radius: 7px;")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setAlignment(QtCore.Qt.AlignCenter)
        self.password_input.setObjectName("password_input")
        self.username_lbl = QtWidgets.QLabel(self.input_frame_3)
        self.username_lbl.setGeometry(QtCore.QRect(130, 40, 90, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.username_lbl.setFont(font)
        self.username_lbl.setStyleSheet("color: rgba(0, 0, 0,0.9);")
        self.username_lbl.setObjectName("username_lbl")
        self.password_lbl = QtWidgets.QLabel(self.input_frame_3)
        self.password_lbl.setGeometry(QtCore.QRect(134, 124, 82, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.password_lbl.setFont(font)
        self.password_lbl.setStyleSheet("color: rgba(0, 0, 0,0.9);")
        self.password_lbl.setObjectName("password_lbl")
        self.label_3 = QtWidgets.QLabel(self.login_panel)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 901, 551))
        self.label_3.setMinimumSize(QtCore.QSize(901, 551))
        self.label_3.setMaximumSize(QtCore.QSize(901, 551))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./old-V/images/svg/svg.svg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.shadow_3.raise_()
        self.input_frame_3.raise_()
        self.stackedWidget.addWidget(self.login_panel)
        self.admin_panel = QtWidgets.QWidget()
        self.admin_panel.setObjectName("admin_panel")
        self.shadow = QtWidgets.QWidget(self.admin_panel)
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
        self.data_upload = QtWidgets.QPushButton(self.input_frame)
        self.data_upload.setGeometry(QtCore.QRect(50, 180, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.data_upload.setFont(font)
        self.data_upload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.data_upload.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(155, 33, 78);\n"
"border-radius:3px;\n"
"color: rgb(155, 33, 78);\n"

"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155, 33, 78);\n"
"color:rgb(255,255,255);\n"
"}")
        self.data_upload.setObjectName("data_upload")
        self.data_edit = QtWidgets.QPushButton(self.input_frame)
        self.data_edit.setGeometry(QtCore.QRect(70, 230, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.data_edit.setFont(font)
        self.data_edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.data_edit.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(155, 33, 78);\n"
"border-radius:3px;\n"
"color: rgb(155, 33, 78);\n"

"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155, 33, 78);\n"
"color:rgb(255,255,255);\n"
"}")
        self.data_edit.setObjectName("data_edit")
        self.current_user = QtWidgets.QLabel(self.input_frame)
        self.current_user.setGeometry(QtCore.QRect(330, 180, 291, 41))
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
        self.pushButton_3 = QtWidgets.QPushButton(self.input_frame)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 340, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: rgba(177, 0, 2,0.9);\n"
"color:rgb(255,255,255);\n"
"border-radius:3px;\n"

"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(144,12,62);\n"
"color:rgb(255,255,255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.admin_panel)
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
        self.stackedWidget.addWidget(self.admin_panel)
        self.add_user_panel = QtWidgets.QWidget()
        self.add_user_panel.setObjectName("add_user_panel")
        self.shadow_2 = QtWidgets.QWidget(self.add_user_panel)
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
        self.label_2 = QtWidgets.QLabel(self.add_user_panel)
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
        self.stackedWidget.addWidget(self.add_user_panel)
        self.delete_user_panel = QtWidgets.QWidget()
        self.delete_user_panel.setObjectName("delete_user_panel")
        self.label_4 = QtWidgets.QLabel(self.delete_user_panel)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 901, 551))
        self.label_4.setMinimumSize(QtCore.QSize(901, 551))
        self.label_4.setMaximumSize(QtCore.QSize(901, 551))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("./old-V/images/svg/svg.svg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.shadow_4 = QtWidgets.QWidget(self.delete_user_panel)
        self.shadow_4.setGeometry(QtCore.QRect(0, 0, 901, 551))
        self.shadow_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.shadow_4.setStyleSheet("background-color: rgba(149, 1, 60,0.02);")
        self.shadow_4.setObjectName("shadow_4")
        self.input_frame_4 = QtWidgets.QFrame(self.shadow_4)
        self.input_frame_4.setGeometry(QtCore.QRect(120, 80, 650, 391))
        self.input_frame_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.input_frame_4.setStyleSheet("border-radius: 25px;\n"
"background-color: rgb(255, 255, 255);")
        self.input_frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame_4.setLineWidth(1)
        self.input_frame_4.setObjectName("input_frame_4")
        self.label_logged_7 = QtWidgets.QLabel(self.input_frame_4)
        self.label_logged_7.setGeometry(QtCore.QRect(90, 30, 461, 121))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_logged_7.setFont(font)
        self.label_logged_7.setStyleSheet("color: rgb(171, 8, 61);\n"
"background-color: rgba(0, 0, 0,0.0);")
        self.label_logged_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logged_7.setObjectName("label_logged_7")
        self.user_delete_2 = QtWidgets.QPushButton(self.input_frame_4)
        self.user_delete_2.setGeometry(QtCore.QRect(250, 260, 151, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.user_delete_2.setFont(font)
        self.user_delete_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.user_delete_2.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(155, 33, 78);\n"
"border-radius:3px;\n"
"color: rgb(155, 33, 78);\n"

"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155, 33, 78);\n"
"color:rgb(255,255,255);\n"
"}")
        self.user_delete_2.setObjectName("user_delete_2")
        self.text_email_2 = QtWidgets.QLineEdit(self.input_frame_4)
        self.text_email_2.setGeometry(QtCore.QRect(220, 200, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.text_email_2.setFont(font)
        self.text_email_2.setStyleSheet("border-bottom:1px solid rgb(149,1,60);\n"
"background-color: rgb(255, 244, 248);\n"
"padding:5px 10px;\n"
"border-top-left-radius :0;\n"
"border-top-right-radius : 15px;\n"
"border-bottom-left-radius : 15px; \n"
"border-bottom-right-radius : 0;\n"
"color:rgb(50,50,50);")
        self.text_email_2.setText("")
        self.text_email_2.setObjectName("text_email_2")
        self.label_logged_8 = QtWidgets.QLabel(self.input_frame_4)
        self.label_logged_8.setGeometry(QtCore.QRect(270, 160, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_logged_8.setFont(font)
        self.label_logged_8.setStyleSheet("color: rgb(171, 8, 61);\n"
"background-color: rgba(0, 0, 0,0.0);")
        self.label_logged_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logged_8.setObjectName("label_logged_8")
        self.error_label_2 = QtWidgets.QLabel(self.input_frame_4)
        self.error_label_2.setGeometry(QtCore.QRect(270, 320, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.error_label_2.setFont(font)
        self.error_label_2.setStyleSheet("color: rgb(50, 50, 50);\n"
"background-color: rgba(0, 0, 0,0.0);")
        self.error_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label_2.setObjectName("error_label_2")
        self.return_btn_2 = QtWidgets.QPushButton(self.input_frame_4)
        self.return_btn_2.setGeometry(QtCore.QRect(570, 20, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.return_btn_2.setFont(font)
        self.return_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.return_btn_2.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(155, 33, 78);\n"
"border-radius:3px;\n"
"color: rgb(155, 33, 78);\n"

"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155, 33, 78);\n"
"color:rgb(255,255,255);\n"
"}")
        self.return_btn_2.setObjectName("return_btn_2")
        self.stackedWidget.addWidget(self.delete_user_panel)
        self.upload_data_panel = QtWidgets.QWidget()
        self.upload_data_panel.setObjectName("upload_data_panel")
        self.label_5 = QtWidgets.QLabel(self.upload_data_panel)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 901, 551))
        self.label_5.setMinimumSize(QtCore.QSize(901, 551))
        self.label_5.setMaximumSize(QtCore.QSize(901, 551))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("./old-V/images/svg/svg.svg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.shadow_5 = QtWidgets.QWidget(self.upload_data_panel)
        self.shadow_5.setGeometry(QtCore.QRect(0, 0, 901, 551))
        self.shadow_5.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.shadow_5.setStyleSheet("background-color: rgba(149, 1, 60,0.02);")
        self.shadow_5.setObjectName("shadow_5")
        self.input_frame_5 = QtWidgets.QFrame(self.shadow_5)
        self.input_frame_5.setGeometry(QtCore.QRect(120, 80, 650, 391))
        self.input_frame_5.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.input_frame_5.setStyleSheet("border-radius: 25px;\n"
"background-color: rgb(255, 255, 255);")
        self.input_frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame_5.setLineWidth(1)
        self.input_frame_5.setObjectName("input_frame_5")
        self.label_logged_9 = QtWidgets.QLabel(self.input_frame_5)
        self.label_logged_9.setGeometry(QtCore.QRect(110, 30, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_logged_9.setFont(font)
        self.label_logged_9.setStyleSheet("color: rgb(171, 8, 61);\n"
"background-color: rgba(0, 0, 0,0.0);")
        self.label_logged_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logged_9.setObjectName("label_logged_9")
        self.upload_btn = QtWidgets.QPushButton(self.input_frame_5)
        self.upload_btn.setGeometry(QtCore.QRect(80, 240, 151, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.upload_btn.setFont(font)
        self.upload_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.upload_btn.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(155, 33, 78);\n"
"border-radius:3px;\n"
"color: rgb(155, 33, 78);\n"

"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155, 33, 78);\n"
"color:rgb(255,255,255);\n"
"}")
        self.upload_btn.setObjectName("upload_btn")
        self.text_email_3 = QtWidgets.QLineEdit(self.input_frame_5)
        self.text_email_3.setGeometry(QtCore.QRect(50, 180, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.text_email_3.setFont(font)
        self.text_email_3.setStyleSheet("border-bottom:1px solid rgb(149,1,60);\n"
"background-color: rgb(255, 244, 248);\n"
"padding:5px 10px;\n"
"border-top-left-radius :0;\n"
"border-top-right-radius : 15px;\n"
"border-bottom-left-radius : 15px; \n"
"border-bottom-right-radius : 0;\n"
"color:rgb(50,50,50);")
        self.text_email_3.setText("")
        self.text_email_3.setObjectName("text_email_3")
        self.label_logged_10 = QtWidgets.QLabel(self.input_frame_5)
        self.label_logged_10.setGeometry(QtCore.QRect(90, 130, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_logged_10.setFont(font)
        self.label_logged_10.setStyleSheet("color: rgb(171, 8, 61);\n"
"background-color: rgba(0, 0, 0,0.0);")
        self.label_logged_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logged_10.setObjectName("label_logged_10")
        self.error_label_3 = QtWidgets.QLabel(self.input_frame_5)
        self.error_label_3.setGeometry(QtCore.QRect(100, 290, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.error_label_3.setFont(font)
        self.error_label_3.setStyleSheet("color: rgb(50, 50, 50);\n"
"background-color: rgba(0, 0, 0,0.0);")
        self.error_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label_3.setObjectName("error_label_3")
        self.return_btn_3 = QtWidgets.QPushButton(self.input_frame_5)
        self.return_btn_3.setGeometry(QtCore.QRect(570, 20, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.return_btn_3.setFont(font)
        self.return_btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.return_btn_3.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(155, 33, 78);\n"
"border-radius:3px;\n"
"color: rgb(155, 33, 78);\n"

"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155, 33, 78);\n"
"color:rgb(255,255,255);\n"
"}")
        self.return_btn_3.setObjectName("return_btn_3")
        self.upload_btn_2 = QtWidgets.QPushButton(self.input_frame_5)
        self.upload_btn_2.setGeometry(QtCore.QRect(400, 281, 141, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.upload_btn_2.setFont(font)
        self.upload_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.upload_btn_2.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(155, 33, 78);\n"
"border-radius:3px;\n"
"color: rgb(155, 33, 78);\n"

"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155, 33, 78);\n"
"color:rgb(255,255,255);\n"
"}")
        self.upload_btn_2.setObjectName("upload_btn_2")
        self.label_image_preview = QtWidgets.QLabel(self.input_frame_5)
        self.label_image_preview.setGeometry(QtCore.QRect(400, 121, 141, 141))
        self.label_image_preview.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image_preview.setObjectName("label_image_preview")
        self.label_foramt = QtWidgets.QLabel(self.input_frame_5)
        self.label_foramt.setGeometry(QtCore.QRect(80, 160, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_foramt.setFont(font)
        self.label_foramt.setStyleSheet("color: rgb(171, 8, 61);\n"
"background-color: rgba(0, 0, 0,0.0);")
        self.label_foramt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_foramt.setObjectName("label_foramt")
        self.stackedWidget.addWidget(self.upload_data_panel)
        self.edit_data_panel = QtWidgets.QWidget()
        self.edit_data_panel.setObjectName("edit_data_panel")
        self.label_6 = QtWidgets.QLabel(self.edit_data_panel)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 901, 551))
        self.label_6.setMinimumSize(QtCore.QSize(901, 551))
        self.label_6.setMaximumSize(QtCore.QSize(901, 551))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("./old-V/images/svg/svg.svg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.tableWidget = QtWidgets.QTableWidget(self.edit_data_panel)
        self.tableWidget.setGeometry(QtCore.QRect(120, 210, 661, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.data_id_input = QtWidgets.QLineEdit(self.edit_data_panel)
        self.data_id_input.setGeometry(QtCore.QRect(190, 140, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.data_id_input.setFont(font)
        self.data_id_input.setStyleSheet("border-bottom:1px solid rgb(149,1,60);\n"
"background-color: rgb(255, 244, 248);\n"
"padding:5px 10px;\n"
"border-top-left-radius :0;\n"
"border-top-right-radius : 15px;\n"
"border-bottom-left-radius : 15px; \n"
"border-bottom-right-radius : 0;\n"
"color:rgb(50,50,50);")
        self.data_id_input.setText("")
        self.data_id_input.setObjectName("data_id_input")
        self.delete_data_btn = QtWidgets.QPushButton(self.edit_data_panel)
        self.delete_data_btn.setGeometry(QtCore.QRect(550, 140, 141, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.delete_data_btn.setFont(font)
        self.delete_data_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_data_btn.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(155, 33, 78);\n"
"border-radius:3px;\n"
"color: rgb(155, 33, 78);\n"

"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155, 33, 78);\n"
"color:rgb(255,255,255);\n"
"}")
        self.delete_data_btn.setObjectName("delete_data_btn")
        self.label_logged_11 = QtWidgets.QLabel(self.edit_data_panel)
        self.label_logged_11.setGeometry(QtCore.QRect(230, 40, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_logged_11.setFont(font)
        self.label_logged_11.setStyleSheet("color: rgb(171, 8, 61);\n"
"background-color: rgba(0, 0, 0,0.0);")
        self.label_logged_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logged_11.setObjectName("label_logged_11")
        self.return_btn_4 = QtWidgets.QPushButton(self.edit_data_panel)
        self.return_btn_4.setGeometry(QtCore.QRect(700, 50, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.return_btn_4.setFont(font)
        self.return_btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.return_btn_4.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(155, 33, 78);\n"
"border-radius:3px;\n"
"color: rgb(155, 33, 78);\n"

"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155, 33, 78);\n"
"color:rgb(255,255,255);\n"
"}")
        self.return_btn_4.setObjectName("return_btn_2")
        self.stackedWidget.addWidget(self.edit_data_panel)
        self.use_app = QtWidgets.QWidget()
        self.use_app.setObjectName("use_app")
        self.frame = QtWidgets.QFrame(self.use_app)
        self.frame.setGeometry(QtCore.QRect(0, 0, 900, 550))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("./old-V/images/svg/svg.svg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(90, 240, 71, 31))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(90, 280, 71, 31))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(60, 120, 141, 111))
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_5.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.use_app)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.user_add.clicked.connect(lambda : self.open_Add_New_User(MainWindow))
        self.user_delete.clicked.connect(lambda : self.open_Delete_User(MainWindow))
        self.data_upload.clicked.connect(lambda : self.open_Add_Data(MainWindow))
        self.data_edit.clicked.connect(lambda : self.open_Delete_Data(MainWindow))
        self.start_btn.clicked.connect(lambda : self.openNewUser(MainWindow))

        #-----Return Button-----#
        self.return_btn.clicked.connect(lambda : self.returnAdminPanel(MainWindow))
        self.return_btn_2.clicked.connect(lambda : self.returnAdminPanel(MainWindow))
        self.return_btn_3.clicked.connect(lambda : self.returnAdminPanel(MainWindow))
        self.return_btn_4.clicked.connect(lambda : self.returnAdminPanel(MainWindow))
        self.pushButton_3.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.login_panel))
        #-----------------------#
        #-----------------------#
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def returnAdminPanel(self,MainWindow):
        self.stackedWidget.setCurrentWidget(self.admin_panel)
    def open_Add_New_User(self,MainWindow):
        self.stackedWidget.setCurrentWidget(self.add_user_panel)
    def open_Delete_User(self,MainWindow):
        self.stackedWidget.setCurrentWidget(self.delete_user_panel)
    def open_Add_Data(self,MainWindow):
        self.stackedWidget.setCurrentWidget(self.upload_data_panel)
    def open_Delete_Data(self,MainWindow):
        self.stackedWidget.setCurrentWidget(self.edit_data_panel)
    def openNewUser(self, MainWindow):
        #MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        #MainWindow.setWindowFlags(self.defaultWindowFlags)
        MainWindow.setMaximumSize(QtCore.QSize(99900, 55099))
        self.centralwidget.setMaximumSize(QtCore.QSize(99900, 55099))
        self.frame.setGeometry(0,0,self.centralwidget.height(),self.centralwidget.width())
        self.frame.setMaximumSize(QtCore.QSize(99900, 55099))
        MainWindow.setWindowFlags(QtCore.Qt.WindowType.CustomizeWindowHint | QtCore.Qt.WindowType.WindowCloseButtonHint | QtCore.Qt.WindowType.WindowMinimizeButtonHint |QtCore.Qt.WindowType.WindowMaximizeButtonHint) 
        # MainWindow.setMinimumSize(QtCore.QSize(300, 250))
        # MainWindow.setMaximumSize(QtCore.QSize(10000, 10550))
        # self.centralwidget.setMinimumSize(QtCore.QSize(900, 550))
        # self.centralwidget.setMaximumSize(QtCore.QSize(99900, 55099))

        # self.centralwidget.setStyleSheet("background-color: rgba(149, 1, 60,0.5);")
        
        # self.frame.setMinimumSize(QtCore.QSize(self.centralwidget.height(),self.centralwidget.width()))
        #MainWindow.stackedWidget.setCurrentWidget(MainWindow.stackedWidget.use_app)
        self.stackedWidget.setCurrentWidget(self.use_app)
        MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.username_input.setPlaceholderText(_translate("MainWindow", "@Username"))
        self.password_input.setPlaceholderText(_translate("MainWindow", "*****"))
        self.username_lbl.setText(_translate("MainWindow", "Username"))
        self.password_lbl.setText(_translate("MainWindow", "Password"))
        self.label_logged.setText(_translate("MainWindow", "Logged in as :"))
        self.user_add.setText(_translate("MainWindow", "Add User"))
        self.start_btn.setText(_translate("MainWindow", "Use App"))
        self.user_delete.setText(_translate("MainWindow", "Delete User"))
        self.data_upload.setText(_translate("MainWindow", "Upload Data"))
        self.data_edit.setText(_translate("MainWindow", "Edit Data"))
        self.current_user.setText(_translate("MainWindow", "Youcef Rida"))
        self.user_rank.setText(_translate("MainWindow", "Lieutenant"))
        self.pushButton_3.setText(_translate("MainWindow", "Logout"))
        self.label_logged_2.setText(_translate("MainWindow", "Please fill in\n"
"the informations"))
        self.user_add_2.setText(_translate("MainWindow", "Add User"))
        self.label_logged_3.setText(_translate("MainWindow", "Full Name :"))
        self.label_logged_4.setText(_translate("MainWindow", "Email :"))
        self.label_logged_5.setText(_translate("MainWindow", "Password :"))
        self.label_logged_6.setText(_translate("MainWindow", "Confirm Password :"))
        self.error_label.setText(_translate("MainWindow", "User Added"))
        self.return_btn.setText(_translate("MainWindow", "⮑"))
        self.label_logged_7.setText(_translate("MainWindow", "You\'re about to\n"
"delete an account !"))
        self.user_delete_2.setText(_translate("MainWindow", "Delete"))
        self.label_logged_8.setText(_translate("MainWindow", "Enter Email"))
        self.error_label_2.setText(_translate("MainWindow", "User Deleted"))
        self.return_btn_2.setText(_translate("MainWindow", "⮑"))
        self.label_logged_9.setText(_translate("MainWindow", "You\'re adding Data to the DB"))
        self.upload_btn.setText(_translate("MainWindow", "Upload"))
        self.label_logged_10.setText(_translate("MainWindow", "Enter informations"))
        self.error_label_3.setText(_translate("MainWindow", "Added"))
        self.return_btn_3.setText(_translate("MainWindow", "⮑"))
        self.upload_btn_2.setText(_translate("MainWindow", "Add Image"))
        self.label_image_preview.setText(_translate("MainWindow", "Image Preview"))
        self.label_foramt.setText(_translate("MainWindow", "format : fname_lname_rank"))
        self.delete_data_btn.setText(_translate("MainWindow", "Delete Data"))
        self.label_logged_11.setText(_translate("MainWindow", "Insert Data UID to Delete"))
        self.return_btn_4.setText(_translate("MainWindow", "⮑"))
        self.label_15.setText(_translate("MainWindow", "Name"))
        self.label_16.setText(_translate("MainWindow", "Name"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        
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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec_())
