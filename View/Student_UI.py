# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Student_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fenetre(object):
    def setupUi(self, fenetre):
        fenetre.setObjectName("fenetre")
        fenetre.resize(1306, 658)
        fenetre.setMinimumSize(QtCore.QSize(1306, 658))
        fenetre.setMaximumSize(QtCore.QSize(1306, 658))
        fenetre.setBaseSize(QtCore.QSize(1306, 658))
        fenetre.setStyleSheet("#clear_button\n"
                              "{\n"
                              "  color: white;\n"
                              "font-size:17px;\n"
                              "font-style:Italic;\n"
                              "  background-color: green;\n"
                              "  border-width: 5px;\n"
                              "  border-radius: 5px;\n"
                              "  height: 40px;\n"
                              "}\n"
                              "\n"
                              "#clear_button:hover\n"
                              "{\n"
                              "  color: white;\n"
                              "font-size:17px;\n"
                              "font-style:Italic;\n"
                              "  background-color: lightgreen;\n"
                              "  border-width: 5px;\n"
                              "  border-radius: 5px;\n"
                              "  height: 40px;\n"
                              "}\n"
                              "\n"
                              "#add_button\n"
                              "{\n"
                              "  color: white;\n"
                              "font-size:17px;\n"
                              "font-style:Italic;\n"
                              "  background-color: #27a9e3;\n"
                              "  border-width: 5px;\n"
                              "  border-radius: 5px;\n"
                              "  height: 40px;\n"
                              "}\n"
                              "\n"
                              "#add_button:hover\n"
                              "{\n"
                              "  color: white;\n"
                              "font-size:17px;\n"
                              "font-style:Italic;\n"
                              "  background-color: lightblue;\n"
                              "  border-width: 5px;\n"
                              "  border-radius: 5px;\n"
                              "  height: 35px;\n"
                              "}\n"
                              "#create_button:hover \n"
                              "{\n"
                              "   background-color: #66c011;\n"
                              " }\n"
                              "\n"
                              "QLineEdit\n"
                              "{\n"
                              "color: black;\n"
                              "font-size:20px;\n"
                              "font-style: Italic Bold;\n"
                              "border-radius: 5px;\n"
                              "border-bottom: 5px solid lightblue;\n"
                              "text-align:center;\n"
                              "height: 30px;\n"
                              "padding-left:10px;\n"
                              "}\n"
                              "/*#Form\n"
                              "{\n"
                              " background-color:\n"
                              "  qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0, y2:0, \n"
                              "  stop:0 rgba(91, 204, 233, 100), stop:1 rgba(32, 80, 96, \n"
                              "  100));\n"
                              "}*/\n"
                              "\n"
                              "/*QLabel{\n"
                              "color:white;\n"
                              "font-size:17px;\n"
                              "font-style:Italic;}*/\n"
                              "\n"
                              "QMainWindow{\n"
                              " background-color:\n"
                              "  qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0, y2:0, \n"
                              "  stop:0 rgba(91, 204, 233, 100), stop:1 rgba(32, 80, 96, \n"
                              "  100));\n"
                              "}")
        self.centralwidget = QtWidgets.QWidget(fenetre)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 1261, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
                                      "color:white;\n"
                                      "font-size:17px;\n"
                                      "font-style:Italic;\n"
                                      "border:2px solid white;\n"
                                      "border-radius: 15%;\n"
                                      "position: relative;\n"
                                      "box-shadow: 0px 2px 4px rgba(0, 0, 0, .10);\n"
                                      "/*padding: 10px;*/\n"
                                      " /* background: white;*/\n"
                                      "}\n"
                                      "")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 50, 651, 531))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableau = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.tableau.setStyleSheet("QTableWidget{\n"
                                   "\n"
                                   "border:2px solid white;\n"
                                   "border-radius:5px;\n"
                                   "box-shadow:10px 10px white;\n"
                                   "}")
        self.tableau.setFrameShape(QtWidgets.QFrame.Box)
        self.tableau.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableau.setObjectName("tableau")
        self.tableau.setColumnCount(0)
        self.tableau.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableau)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.delete_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.delete_button.setStyleSheet("#delete_button\n"
                                         "{\n"
                                         "  color: white;\n"
                                         "  font-size:17px;\n"
                                         "  font-style:Italic;\n"
                                         "  background-color: red;\n"
                                         "  border-width: 5px;\n"
                                         "  border-radius: 5px;\n"
                                         "  height: 40px;\n"
                                         "  width: 140px;\n"
                                         "}\n"
                                         "\n"
                                         "#delete_button:hover\n"
                                         "{\n"
                                         "  color: white;\n"
                                         "  font-size:15px;\n"
                                         "  font-style:Italic;\n"
                                         "  background-color: pink;\n"
                                         "  border-width: 5px;\n"
                                         "  border-radius: 5px;\n"
                                         "  height: 35px;\n"
                                         "  width: 130px;\n"
                                         "}\n"
                                         "\n"
                                         "#delete_button:pressed\n"
                                         "{\n"
                                         "  color: white;\n"
                                         "  font-size:15px;\n"
                                         "  font-style:Italic;\n"
                                         "  background-color: red;\n"
                                         "  border-width: 5px;\n"
                                         "  border-radius: 5px;\n"
                                         "  height: 30px;\n"
                                         "  width: 120px;\n"
                                         "cursor: pointer;\n"
                                         "}")
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_2.addWidget(self.delete_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.student_list = QtWidgets.QLabel(self.groupBox_2)
        self.student_list.setGeometry(QtCore.QRect(14, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.student_list.setFont(font)
        self.student_list.setAutoFillBackground(False)
        self.student_list.setStyleSheet("QLabel{\n"
                                        "color:white;\n"
                                        "font-style:italic;\n"
                                        "font-size:25px;\n"
                                        "font-weight:10px;\n"
                                        "box-shadow: 7px 2px 4px rgba(0, 0, 0, .10);\n"
                                        "margin: 2px;\n"
                                        "border:0px;\n"
                                        "}")
        self.student_list.setFrameShape(QtWidgets.QFrame.Box)
        self.student_list.setFrameShadow(QtWidgets.QFrame.Plain)
        self.student_list.setScaledContents(True)
        self.student_list.setWordWrap(False)
        self.student_list.setIndent(5)
        self.student_list.setObjectName("student_list")
        self.horizontalLayout_7.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("QGroupBox{\n"
                                    "color:white;\n"
                                    "font-size:17px;\n"
                                    "font-style:Italic;\n"
                                    "border:2px solid white;\n"
                                    "border-radius: 15%;\n"
                                    "position: relative;\n"
                                    "box-shadow: 0px 2px 4px rgba(0, 0, 0, .10);\n"
                                    "/*padding: 10px;*/\n"
                                    " /* background: white;*/\n"
                                    "}")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(1, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.register_new_student = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.register_new_student.setFont(font)
        self.register_new_student.setStyleSheet("QLabel{\n"
                                                "color:white;\n"
                                                "font-style:italic;\n"
                                                "font-size:25px;\n"
                                                "font-weight:10px;\n"
                                                "box-shadow: 7px 2px 4px rgba(0, 0, 0, .10);\n"
                                                "margin: 2px;\n"
                                                "border:0px;\n"
                                                "}\n"
                                                "\n"
                                                "")
        self.register_new_student.setFrameShape(QtWidgets.QFrame.Box)
        self.register_new_student.setFrameShadow(QtWidgets.QFrame.Raised)
        self.register_new_student.setScaledContents(True)
        self.register_new_student.setWordWrap(False)
        self.register_new_student.setIndent(5)
        self.register_new_student.setObjectName("register_new_student")
        self.verticalLayout.addWidget(self.register_new_student)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setObjectName("formLayout")
        self.name = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setStyleSheet("QLabel{\n"
                                "color:white;\n"
                                "font-style:italic bold;\n"
                                "font-size:20px;\n"
                                "font-weight:20px;\n"
                                "margin: 2px;\n"
                                "border:0px;\n"
                                "}")
        self.name.setObjectName("name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name)
        self.name_input = QtWidgets.QLineEdit(self.groupBox)
        self.name_input.setObjectName("name_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_input)
        self.surname = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.surname.setFont(font)
        self.surname.setStyleSheet("QLabel{\n"
                                   "color:white;\n"
                                   "font-style:italic bold;\n"
                                   "font-size:20px;\n"
                                   "font-weight:20px;\n"
                                   "margin: 2px;\n"
                                   "border:0px;\n"
                                   "}")
        self.surname.setObjectName("surname")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.surname)
        self.surname_input = QtWidgets.QLineEdit(self.groupBox)
        self.surname_input.setObjectName("surname_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.surname_input)
        self.email = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setStyleSheet("QLabel{\n"
                                 "color:white;\n"
                                 "font-style:italic bold;\n"
                                 "font-size:20px;\n"
                                 "font-weight:20px;\n"
                                 "margin: 2px;\n"
                                 "border:0px;\n"
                                 "}")
        self.email.setObjectName("email")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.email)
        self.email_input = QtWidgets.QLineEdit(self.groupBox)
        self.email_input.setObjectName("email_input")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.email_input)
        self.calendar = QtWidgets.QCalendarWidget(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.calendar.setFont(font)
        self.calendar.setAutoFillBackground(False)
        self.calendar.setStyleSheet("QCalendarWidget{\n"
                                    "border-radius:10px;\n"
                                    "}")
        self.calendar.setGridVisible(False)
        self.calendar.setObjectName("calendar")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.calendar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clear_button = QtWidgets.QPushButton(self.groupBox)
        self.clear_button.setStyleSheet("#clear_button\n"
                                        "{\n"
                                        "  color: white;\n"
                                        "font-size:17px;\n"
                                        "font-style:Italic;\n"
                                        "  background-color: #27a9e3;\n"
                                        "  border-width: 5px;\n"
                                        "  border-radius: 5px;\n"
                                        "  height: 40px;\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "#clear_button:hover\n"
                                        "{\n"
                                        "  color: white;\n"
                                        "font-size:15px;\n"
                                        "font-style:Italic;\n"
                                        "  background-color:lightblue;\n"
                                        "  border-width: 5px;\n"
                                        "  border-radius: 5px;\n"
                                        "  height: 35px;\n"
                                        "}\n"
                                        "\n"
                                        "#clear_button:pressed\n"
                                        "{\n"
                                        "  color: white;\n"
                                        "  font-size:15px;\n"
                                        "  font-style:Italic;\n"
                                        "  background-color: #27a9e3;\n"
                                        "  border-width: 5px;\n"
                                        "  border-radius: 5px;\n"
                                        "  height: 30px;\n"
                                        "  width: 120px;\n"
                                        "cursor: pointer;\n"
                                        "}")
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout.addWidget(self.clear_button)
        self.add_button = QtWidgets.QPushButton(self.groupBox)
        self.add_button.setStyleSheet("#add_button\n"
                                      "{\n"
                                      "  color: white;\n"
                                      "font-size:17px;\n"
                                      "font-style:Italic;\n"
                                      "  background-color: #27a9e3;\n"
                                      "  border-width: 5px;\n"
                                      "  border-radius: 5px;\n"
                                      "  height: 40px;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "#add_button:hover\n"
                                      "{\n"
                                      "  color: white;\n"
                                      "font-size:15px;\n"
                                      "font-style:Italic;\n"
                                      "  background-color: lightgreen;\n"
                                      "  border-width: 5px;\n"
                                      "  border-radius: 5px;\n"
                                      "  height: 35px;\n"
                                      "}\n"
                                      "\n"
                                      "#add_button:pressed\n"
                                      "{\n"
                                      "  color: white;\n"
                                      "  font-size:15px;\n"
                                      "  font-style:Italic;\n"
                                      "  background-color: green;\n"
                                      "  border-width: 5px;\n"
                                      "  border-radius: 5px;\n"
                                      "  height: 30px;\n"
                                      "  width: 120px;\n"
                                      "cursor: pointer;\n"
                                      "}")
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.birthday = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.birthday.setFont(font)
        self.birthday.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.birthday.setStyleSheet("QLabel{\n"
                                    "color:white;\n"
                                    "font-style:italic bold;\n"
                                    "font-size:20px;\n"
                                    "font-weight:20px;\n"
                                    "margin: 2px;\n"
                                    "border:0px;\n"
                                    "}")
        self.birthday.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.birthday.setTextFormat(QtCore.Qt.AutoText)
        self.birthday.setScaledContents(False)
        self.birthday.setAlignment(QtCore.Qt.AlignCenter)
        self.birthday.setObjectName("birthday")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.birthday)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_7.addWidget(self.groupBox, 0, QtCore.Qt.AlignRight)
        fenetre.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(fenetre)
        self.statusBar.setObjectName("statusBar")
        fenetre.setStatusBar(self.statusBar)

        self.retranslateUi(fenetre)
        QtCore.QMetaObject.connectSlotsByName(fenetre)

    def retranslateUi(self, fenetre):
        _translate = QtCore.QCoreApplication.translate
        fenetre.setWindowTitle(_translate("fenetre", "MainWindow"))
        self.delete_button.setText(_translate("fenetre", "Delete"))
        self.student_list.setText(_translate("fenetre", "Student List"))
        self.register_new_student.setText(_translate("fenetre", "Register new Student"))
        self.name.setText(_translate("fenetre", "Name:"))
        self.surname.setText(_translate("fenetre", "Surname:"))
        self.email.setText(_translate("fenetre", "Email:"))
        self.clear_button.setText(_translate("fenetre", "Clear"))
        self.add_button.setText(_translate("fenetre", "Add"))
        self.birthday.setText(_translate("fenetre", "Date of Birth:"))
