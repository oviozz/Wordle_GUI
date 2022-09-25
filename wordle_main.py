from PyQt5 import QtCore, QtGui, QtWidgets
import random
import requests


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 1300)
        MainWindow.setStyleSheet("background-color: #f1f2f6 ; font: 20pt \"Arial\";\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(79, 237, 801, 791))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_21.setStyleSheet("")
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 4, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 3, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 4, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 3, 2, 1, 1)
        self.first_two = QtWidgets.QLabel(self.gridLayoutWidget)
        self.first_two.setObjectName("first_two")
        self.gridLayout.addWidget(self.first_two, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.first_five = QtWidgets.QLabel(self.gridLayoutWidget)
        self.first_five.setObjectName("first_five")
        self.gridLayout.addWidget(self.first_five, 0, 4, 1, 1)
        self.first_four = QtWidgets.QLabel(self.gridLayoutWidget)
        self.first_four.setObjectName("first_four")
        self.gridLayout.addWidget(self.first_four, 0, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 4, 4, 1, 1)
        self.first_three = QtWidgets.QLabel(self.gridLayoutWidget)
        self.first_three.setObjectName("first_three")
        self.gridLayout.addWidget(self.first_three, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 4, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 3, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 4, 2, 1, 1)
        self.first_one = QtWidgets.QLabel(self.gridLayoutWidget)
        self.first_one.setObjectName("first_one")
        self.gridLayout.addWidget(self.first_one, 0, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 4, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 120, 391, 61))
        self.lineEdit.setStyleSheet("border: 3px solid lightblue; border-radius:10%\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 130, 181, 41))
        self.pushButton.setStyleSheet("""QPushButton {
    background-color: rgb(106, 168, 79);
    color: White;
    padding: 2px;
    font: bold 20px;
    border-width: 6px;
    border-radius: 5px;
    border-color: rgb(96, 166, 235);
}
QPushButton:hover {
    background-color: rgb(96, 166, 235);
}""")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 190, 441, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(248, 120, 120);")
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 101, 91))
        self.label_2.setStyleSheet("font: 50pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(106, 168, 79);\n"
"border-radius: 20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 10, 101, 91))
        self.label_3.setStyleSheet("font: 50pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(106, 168, 79);\n"
"border-radius: 20px;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 10, 101, 91))
        self.label_4.setStyleSheet("font: 50pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(106, 168, 79);\n"
"border-radius: 20px;\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 10, 101, 91))
        self.label_5.setStyleSheet("font: 50pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(106, 168, 79);\n"
"border-radius: 20px;\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(640, 10, 101, 91))
        self.label_0.setStyleSheet("font: 50pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(106, 168, 79);\n"
                                   "border-radius: 20px;\n"
                                   "")
        self.label_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_0.setObjectName("label_0")

        self.hint = QtWidgets.QPushButton(self.centralwidget)
        self.hint.setGeometry(QtCore.QRect(10, 10, 61, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.hint.setFont(font)
        self.hint.setStyleSheet("background-color: white; font: 10pt \"MS Shell Dlg 2\";")
        self.hint.setObjectName("hint")
        self.answer = QtWidgets.QLabel(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(10, 30, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.answer.setFont(font)
        self.answer.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.answer.setText("")
        self.answer.setObjectName("answer")
        self.first_arrow = QtWidgets.QLabel(self.centralwidget)
        self.first_arrow.setGeometry(QtCore.QRect(20, 270, 51, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.first_arrow.setFont(font)
        self.first_arrow.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"")
        self.first_arrow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.first_arrow.setObjectName("first_arrow")
        self.second_arrow = QtWidgets.QLabel(self.centralwidget)
        self.second_arrow.setGeometry(QtCore.QRect(20, 430, 51, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.second_arrow.setFont(font)
        self.second_arrow.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"")
        self.second_arrow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.second_arrow.setObjectName("second_arrow")
        self.third_arrow = QtWidgets.QLabel(self.centralwidget)
        self.third_arrow.setGeometry(QtCore.QRect(20, 570, 51, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.third_arrow.setFont(font)
        self.third_arrow.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"")
        self.third_arrow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.third_arrow.setObjectName("third_arrow")
        self.fourth_arrow = QtWidgets.QLabel(self.centralwidget)
        self.fourth_arrow.setGeometry(QtCore.QRect(20, 740, 51, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.fourth_arrow.setFont(font)
        self.fourth_arrow.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"")
        self.fourth_arrow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fourth_arrow.setObjectName("fourth_arrow")
        self.fifth_arrow = QtWidgets.QLabel(self.centralwidget)
        self.fifth_arrow.setGeometry(QtCore.QRect(20, 890, 51, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.fifth_arrow.setFont(font)
        self.fifth_arrow.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"")
        self.fifth_arrow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fifth_arrow.setObjectName("fifth_arrow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1131, 38))
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
        self.label_12.setText(_translate("MainWindow", ""))
        self.label_21.setText(_translate("MainWindow", ""))
        self.label_20.setText(_translate("MainWindow", ""))
        self.label_6.setText(_translate("MainWindow", ""))
        self.label_13.setText(_translate("MainWindow", ""))
        self.label_7.setText(_translate("MainWindow", ""))
        self.label_10.setText(_translate("MainWindow", ""))
        self.label_18.setText(_translate("MainWindow", ""))
        self.first_two.setText(_translate("MainWindow", ""))
        self.label_16.setText(_translate("MainWindow", ""))
        self.label_8.setText(_translate("MainWindow", ""))
        self.first_five.setText(_translate("MainWindow", ""))
        self.first_four.setText(_translate("MainWindow", ""))
        self.label_22.setText(_translate("MainWindow", ""))
        self.label_11.setText(_translate("MainWindow", ""))
        self.label_25.setText(_translate("MainWindow", ""))
        self.first_three.setText(_translate("MainWindow", ""))
        self.label_15.setText(_translate("MainWindow", ""))
        self.label_17.setText(_translate("MainWindow", ""))
        self.label_9.setText(_translate("MainWindow", ""))
        self.label_23.setText(_translate("MainWindow", ""))
        self.first_one.setText(_translate("MainWindow", ""))
        self.label_19.setText(_translate("MainWindow", ""))
        self.label_24.setText(_translate("MainWindow", ""))
        self.label_14.setText(_translate("MainWindow", ""))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Type a word"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "Enter a five letter word"))
        self.label_2.setText(_translate("MainWindow", "W"))
        self.label_3.setText(_translate("MainWindow", "O"))
        self.label_4.setText(_translate("MainWindow", "R"))
        self.label_5.setText(_translate("MainWindow", "D"))
        self.label_0.setText(_translate("MainWindow", "Y"))
        self.hint.setText(_translate("MainWindow", "Answer?"))
        self.first_arrow.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.second_arrow.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.third_arrow.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.fourth_arrow.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.fifth_arrow.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))

        self.pushButton.clicked.connect(self.input_submitted)
        self.hint.clicked.connect(self.reveal)

        # ----------------------------------------------------
        self.count = 0
        self.word = self.get_words()

    def get_words(self):
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

        response = requests.get(word_site)
        word = response.content.splitlines()

        random_num = random.randint(0, 10000)

        word_list = str(word[random_num].decode())

        while len(word_list) != 5:
            random_num = random.randint(0, 10000)
            word_list = str(word[random_num].decode())

        return word_list


    def input_submitted(self):

        self.input_word = self.lineEdit.displayText()

        if len(self.input_word) != 5 or True in (i.isdigit() for i in self.input_word):
            self.label.setText('Enter a five letter word')
        else:
            self.label.setText(f'You typed: {self.input_word.capitalize()}')

            if self.count == 0:
                self.first_arrow.setText('➤')
                self.first_arrow.setStyleSheet("color: rgb(102,178,255);")

                self.first_place_word()
                for i in range(len(self.input_word)):
                    self.index = i
                    self.place_color_first()

                self.count += 1
                self.correct_answer()
                self.lineEdit.setText('')


            elif self.count == 1:

                self.second_arrow.setText('➤')
                self.second_arrow.setStyleSheet("color: rgb(102,178,255);")
                self.first_arrow.setText('')

                self.second_place_word()
                for i in range(len(self.input_word)):
                    self.index = i
                    self.place_color_second()

                self.count += 1
                self.correct_answer()
                self.lineEdit.setText('')

            elif self.count == 2:

                self.third_arrow.setText('➤')
                self.third_arrow.setStyleSheet("color: rgb(102,178,255);")
                self.second_arrow.setText('')

                self.third_place_word()
                for i in range(len(self.input_word)):
                    self.index = i
                    self.place_color_third()


                self.count += 1
                self.correct_answer()
                self.lineEdit.setText('')

            elif self.count == 3:
                self.fourth_arrow.setText('➤')
                self.fourth_arrow.setStyleSheet("color: rgb(102,178,255);")
                self.third_arrow.setText('')

                self.fourth_place_word()
                for i in range(len(self.input_word)):
                    self.index = i
                    self.place_color_fourth()

                self.count += 1
                self.correct_answer()
                self.lineEdit.setText('')

            elif self.count == 4:
                self.fifth_arrow.setText('➤')
                self.fifth_arrow.setStyleSheet("color: rgb(102,178,255);")
                self.fourth_arrow.setText('')

                self.fifth_place_word()
                for i in range(len(self.input_word)):
                    self.index = i
                    self.place_color_fifth()

                self.count += 1
                self.tries_over()
                self.correct_answer()
                self.lineEdit.setText('')



    def place_color_first(self):
        if self.input_word[self.index] == self.word[self.index]:
            if self.index == 0:
                self.first_one.setStyleSheet('background-color: rgb(1,154,1);')
                self.first_one.setMargin(60)

            if self.index == 1:
                self.first_two.setStyleSheet('background-color: rgb(1,154,1);')
                self.first_two.setMargin(60)

            if self.index == 2:
                self.first_three.setStyleSheet('background-color: rgb(1,154,1);')
                self.first_three.setMargin(60)

            if self.index == 3:
                self.first_four.setStyleSheet('background-color: rgb(1,154,1);')
                self.first_four.setMargin(60)

            if self.index == 4:
                self.first_five.setStyleSheet('background-color: rgb(1,154,1);')
                self.first_five.setMargin(60)

        if self.input_word[self.index] != self.word[self.index] and self.input_word[self.index] in self.word:
            if self.index == 0:
                self.first_one.setStyleSheet('background-color: rgb(200,182,83);')
                self.first_one.setMargin(60)

            if self.index == 1:
                self.first_two.setStyleSheet('background-color: rgb(200,182,83);')
                self.first_two.setMargin(60)

            if self.index == 2:
                self.first_three.setStyleSheet('background-color: rgb(200,182,83);')
                self.first_three.setMargin(60)

            if self.index == 3:
                self.first_four.setStyleSheet('background-color: rgb(200,182,83);')
                self.first_four.setMargin(60)

            if self.index == 4:
                self.first_five.setStyleSheet('background-color: rgb(200,182,83);')
                self.first_five.setMargin(60)

        if self.input_word[self.index] not in self.word:
            if self.index == 0:
                self.first_one.setStyleSheet('background-color: rgb(120,124,127);')
                self.first_one.setMargin(60)

            if self.index == 1:
                self.first_two.setStyleSheet('background-color: rgb(120,124,127);')
                self.first_two.setMargin(60)

            if self.index == 2:
                self.first_three.setStyleSheet('background-color: rgb(120,124,127);')
                self.first_three.setMargin(60)

            if self.index == 3:
                self.first_four.setStyleSheet('background-color: rgb(120,124,127);')
                self.first_four.setMargin(60)

            if self.index == 4:
                self.first_five.setStyleSheet('background-color: rgb(120,124,127);')
                self.first_five.setMargin(60)


    def place_color_second(self):
        if self.input_word[self.index] == self.word[self.index]:
            if self.index == 0:
                self.label_6.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_6.setMargin(60)

            if self.index == 1:
                self.label_7.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_7.setMargin(60)

            if self.index == 2:
                self.label_8.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_8.setMargin(60)

            if self.index == 3:
                self.label_9.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_9.setMargin(60)

            if self.index == 4:
                self.label_10.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_10.setMargin(60)

        if self.input_word[self.index] != self.word[self.index] and self.input_word[self.index] in self.word:
            if self.index == 0:
                self.label_6.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_6.setMargin(60)

            if self.index == 1:
                self.label_7.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_7.setMargin(60)

            if self.index == 2:
                self.label_8.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_8.setMargin(60)

            if self.index == 3:
                self.label_9.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_9.setMargin(60)

            if self.index == 4:
                self.label_10.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_10.setMargin(60)

        if self.input_word[self.index] not in self.word:
            if self.index == 0:
                self.label_6.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_6.setMargin(60)

            if self.index == 1:
                self.label_7.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_7.setMargin(60)

            if self.index == 2:
                self.label_8.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_8.setMargin(60)

            if self.index == 3:
                self.label_9.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_9.setMargin(60)

            if self.index == 4:
                self.label_10.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_10.setMargin(60)

    def place_color_third(self):
        if self.input_word[self.index] == self.word[self.index]:
            if self.index == 0:
                self.label_11.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_11.setMargin(60)

            if self.index == 1:
                self.label_12.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_12.setMargin(60)

            if self.index == 2:
                self.label_13.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_13.setMargin(60)

            if self.index == 3:
                self.label_14.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_14.setMargin(60)

            if self.index == 4:
                self.label_15.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_15.setMargin(60)

        if self.input_word[self.index] != self.word[self.index] and self.input_word[self.index] in self.word:
            if self.index == 0:
                self.label_11.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_11.setMargin(60)

            if self.index == 1:
                self.label_12.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_12.setMargin(60)

            if self.index == 2:
                self.label_13.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_13.setMargin(60)

            if self.index == 3:
                self.label_14.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_14.setMargin(60)

            if self.index == 4:
                self.label_15.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_15.setMargin(60)

        if self.input_word[self.index] not in self.word:
            if self.index == 0:
                self.label_11.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_11.setMargin(60)

            if self.index == 1:
                self.label_12.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_12.setMargin(60)

            if self.index == 2:
                self.label_13.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_13.setMargin(60)

            if self.index == 3:
                self.label_14.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_14.setMargin(60)

            if self.index == 4:
                self.label_15.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_15.setMargin(60)

    def place_color_fourth(self):
        if self.input_word[self.index] == self.word[self.index]:
            if self.index == 0:
                self.label_16.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_16.setMargin(60)

            if self.index == 1:
                self.label_17.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_17.setMargin(60)

            if self.index == 2:
                self.label_18.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_18.setMargin(60)

            if self.index == 3:
                self.label_19.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_19.setMargin(60)

            if self.index == 4:
                self.label_20.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_20.setMargin(60)

        if self.input_word[self.index] != self.word[self.index] and self.input_word[self.index] in self.word:
            if self.index == 0:
                self.label_16.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_16.setMargin(60)

            if self.index == 1:
                self.label_17.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_17.setMargin(60)

            if self.index == 2:
                self.label_18.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_18.setMargin(60)

            if self.index == 3:
                self.label_19.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_19.setMargin(60)

            if self.index == 4:
                self.label_20.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_20.setMargin(60)

        if self.input_word[self.index] not in self.word:
            if self.index == 0:
                self.label_16.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_16.setMargin(60)

            if self.index == 1:
                self.label_17.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_17.setMargin(60)

            if self.index == 2:
                self.label_18.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_18.setMargin(60)

            if self.index == 3:
                self.label_19.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_19.setMargin(60)

            if self.index == 4:
                self.label_20.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_20.setMargin(60)

    def place_color_fifth(self):
        if self.input_word[self.index] == self.word[self.index]:
            if self.index == 0:
                self.label_21.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_21.setMargin(60)

            if self.index == 1:
                self.label_22.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_22.setMargin(60)

            if self.index == 2:
                self.label_23.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_23.setMargin(60)

            if self.index == 3:
                self.label_24.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_24.setMargin(60)

            if self.index == 4:
                self.label_25.setStyleSheet('background-color: rgb(1,154,1);')
                self.label_25.setMargin(60)

        if self.input_word[self.index] != self.word[self.index] and self.input_word[self.index] in self.word:
            if self.index == 0:
                self.label_21.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_21.setMargin(60)

            if self.index == 1:
                self.label_22.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_22.setMargin(60)

            if self.index == 2:
                self.label_23.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_23.setMargin(60)

            if self.index == 3:
                self.label_24.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_24.setMargin(60)

            if self.index == 4:
                self.label_25.setStyleSheet('background-color: rgb(200,182,83);')
                self.label_25.setMargin(60)

        if self.input_word[self.index] not in self.word:
            if self.index == 0:
                self.label_21.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_21.setMargin(60)

            if self.index == 1:
                self.label_22.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_22.setMargin(60)

            if self.index == 2:
                self.label_23.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_23.setMargin(60)

            if self.index == 3:
                self.label_24.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_24.setMargin(60)

            if self.index == 4:
                self.label_25.setStyleSheet('background-color: rgb(120,124,127);')
                self.label_25.setMargin(60)


# -------------------------------------------------------------------------
    # Placing index word for each line ( 0 - 4 )

    def first_place_word(self):
        self.first_one.setText(self.input_word[0].upper())
        self.first_two.setText(self.input_word[1].upper())
        self.first_three.setText(self.input_word[2].upper())
        self.first_four.setText(self.input_word[3].upper())
        self.first_five.setText(self.input_word[4].upper())

    def second_place_word(self):
        self.label_6.setText(self.input_word[0].upper())
        self.label_7.setText(self.input_word[1].upper())
        self.label_8.setText(self.input_word[2].upper())
        self.label_9.setText(self.input_word[3].upper())
        self.label_10.setText(self.input_word[4].upper())

    def third_place_word(self):
        self.label_11.setText(self.input_word[0].upper())
        self.label_12.setText(self.input_word[1].upper())
        self.label_13.setText(self.input_word[2].upper())
        self.label_14.setText(self.input_word[3].upper())
        self.label_15.setText(self.input_word[4].upper())

    def fourth_place_word(self):
        self.label_16.setText(self.input_word[0].upper())
        self.label_17.setText(self.input_word[1].upper())
        self.label_18.setText(self.input_word[2].upper())
        self.label_19.setText(self.input_word[3].upper())
        self.label_20.setText(self.input_word[4].upper())

    def fifth_place_word(self):
        self.label_21.setText(self.input_word[0].upper())
        self.label_22.setText(self.input_word[1].upper())
        self.label_23.setText(self.input_word[2].upper())
        self.label_24.setText(self.input_word[3].upper())
        self.label_25.setText(self.input_word[4].upper())


# -------------------------------------------------------------------------

    def reveal(self):
        self.answer.setText(f'The word is {self.word}')


    def correct_answer(self):
        if self.input_word == self.word:
            msg = QtWidgets.QMessageBox()

            msg.setIcon(msg.Information)
            msg.setWindowTitle("Congratulation")
            msg.setText("Good Job, You got it Right ")

            x = msg.exec_()
            self.reboot()

    def tries_over(self):
        if self.input_word != self.word:
            msg = QtWidgets.QMessageBox()

            msg.setIcon(msg.Information)
            msg.setWindowTitle("You are out of tries")
            msg.setText(f"ehh out of luck \nCorrect word: {self.word}")

            x = msg.exec_()
            self.reboot()

    def reboot(self):
        Ui_MainWindow.setupUi(self,MainWindow)
        self.count = 0





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
