# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import os

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup


class Ui_MainWindow(object):
    def __init__(self):
        self.lwidth = 130
        self.lheight = 25
        self.iwidth = 350
        self.iheigth = 25

        self.label_x = 50
        self.input_x = 200

        self.name = ''
        self.author = ''
        self.reader = ''
        self.genre = ''
        self.duration = ''
        self.desc = ''
        self.add_desc = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Labels
        font = QtGui.QFont()
        font.setPointSize(9)

        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(self.label_x, 30, self.lwidth, self.lheight))
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")

        self.authorLabel = QtWidgets.QLabel(self.centralwidget)
        self.authorLabel.setGeometry(QtCore.QRect(self.label_x, 80, self.lwidth, self.lheight))
        self.authorLabel.setFont(font)
        self.authorLabel.setObjectName("authorLabel")

        self.readlabel = QtWidgets.QLabel(self.centralwidget)
        self.readlabel.setGeometry(QtCore.QRect(self.label_x, 130, self.lwidth, self.lheight))
        self.readlabel.setFont(font)
        self.readlabel.setObjectName("readlabel")

        self.genreLabel = QtWidgets.QLabel(self.centralwidget)
        self.genreLabel.setGeometry(QtCore.QRect(self.label_x, 180, self.lwidth, self.lheight))
        self.genreLabel.setFont(font)
        self.genreLabel.setObjectName("genreLabel")

        self.durationLabel = QtWidgets.QLabel(self.centralwidget)
        self.durationLabel.setGeometry(QtCore.QRect(self.label_x, 230, self.lwidth, self.lheight))
        self.durationLabel.setFont(font)
        self.durationLabel.setObjectName("durationLabel")

        self.descLabel = QtWidgets.QLabel(self.centralwidget)
        self.descLabel.setGeometry(QtCore.QRect(self.label_x, 280, self.lwidth, self.lheight))
        self.descLabel.setFont(font)
        self.descLabel.setObjectName("descLabel")

        self.addDessLabel = QtWidgets.QLabel(self.centralwidget)
        self.addDessLabel.setGeometry(QtCore.QRect(self.label_x, 370, self.lwidth, self.lheight))
        self.addDessLabel.setFont(font)
        self.addDessLabel.setObjectName("addDessLabel")

        self.trackerLabel = QtWidgets.QLabel(self.centralwidget)
        self.trackerLabel.setGeometry(QtCore.QRect(self.label_x, 500, self.lwidth, self.lheight))
        self.trackerLabel.setFont(font)
        self.trackerLabel.setObjectName("trackerLabel")

        # Inputs
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(self.input_x, 30, self.iwidth, self.iheigth))
        self.nameEdit.setObjectName("nameEdit")

        self.authorEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.authorEdit.setGeometry(QtCore.QRect(self.input_x, 80, self.iwidth, self.iheigth))
        self.authorEdit.setObjectName("authorEdit")

        self.readEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.readEdit.setGeometry(QtCore.QRect(self.input_x, 130, self.iwidth, self.iheigth))
        self.readEdit.setObjectName("readEdit")

        self.genreEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.genreEdit.setGeometry(QtCore.QRect(self.input_x, 180, self.iwidth, self.iheigth))
        self.genreEdit.setObjectName("genreEdit")

        self.durationEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.durationEdit.setGeometry(QtCore.QRect(self.input_x, 230, self.iwidth, self.iheigth))
        self.durationEdit.setObjectName("durationEdit")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(self.input_x, 280, self.iwidth, 70))
        self.textEdit.setObjectName("textEdit")

        self.addDessEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addDessEdit.setGeometry(QtCore.QRect(self.input_x, 370, self.iwidth, self.iheigth))
        self.addDessEdit.setObjectName("addDessEdit")

        self.trackerEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.trackerEdit.setGeometry(QtCore.QRect(self.input_x, 500, self.iwidth, self.iheigth))
        self.trackerEdit.setObjectName("trackerEdit")

        # Buttons
        self.pushBtn = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn.setGeometry(QtCore.QRect(195, 420, 100, 30))
        self.pushBtn.setObjectName("pushBtn")
        self.pushBtn.setStyleSheet("QPushButton {background-color: #bddef6; color: #0e0e0e; font-size: 13px}"
                                   "QPushButton:hover{background-color: #b3d3ea;}")
        self.pushBtn.clicked.connect(self.convert)

        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn.setGeometry(QtCore.QRect(305, 420, 100, 30))
        self.clearBtn.setObjectName("clearBtn")
        self.clearBtn.setStyleSheet("QPushButton {background-color: #e6edf2; color: #0e0e0e; font-size: 13px}"
                                    "QPushButton:hover{background-color: #cee4f4}")
        self.clearBtn.clicked.connect(self.clear)

        self.trackerBtn = QtWidgets.QPushButton(self.centralwidget)
        self.trackerBtn.setGeometry(QtCore.QRect(305, 550, 100, 30))
        self.trackerBtn.setObjectName("clearBtn")
        self.trackerBtn.setStyleSheet("QPushButton {background-color: #e6edf2; color: #0e0e0e; font-size: 13px}"
                                      "QPushButton:hover{background-color: #cee4f4}")
        self.trackerBtn.clicked.connect(self.parse_data)

        # Addition
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(50, 450, self.lwidth, self.lheight))
        self.statusLabel.setStyleSheet("QLabel {color: #6c757d; font-size: 10px}")
        self.statusLabel.setObjectName("statusLabel")

        # MenuBar, statusBar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
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
        self.nameLabel.setText(_translate("MainWindow", "Название:"))
        self.authorLabel.setText(_translate("MainWindow", "Автор:"))
        self.readlabel.setText(_translate("MainWindow", "Исполняет:"))
        self.genreLabel.setText(_translate("MainWindow", "Жанр:"))
        self.durationLabel.setText(_translate("MainWindow", "Продолжительность:"))
        self.descLabel.setText(_translate("MainWindow", "Описание:"))
        self.addDessLabel.setText(_translate("MainWindow", "Доп описание:"))
        self.pushBtn.setText(_translate("MainWindow", "Подготовить"))
        self.clearBtn.setText(_translate("MainWindow", "Очистить"))
        self.trackerBtn.setText(_translate("MainWindow", "Спарсить"))
        self.trackerLabel.setText(_translate("MainWindow", "Трекер"))

    def convert(self):

        self.name = self.nameEdit.text()
        self.author = self.authorEdit.text()
        self.reader = self.readEdit.text()
        self.genre = self.genreEdit.text()
        self.duration = self.durationEdit.text()
        self.desc = self.textEdit.toPlainText()
        self.add_desc = self.addDessEdit.text()

        self.saveToFile()

    # Write text to file.
    def saveToFile(self):
        file_name = 'audiobook.txt'

        username = os.getlogin()
        if username:
            folder = f'C:\\Users\\{username}\\Desktop\\'
            path = folder + file_name
        else:
            path = file_name

        text_file = open(path, 'w', encoding="UTF_8")

        if self.name:
            name_input = "__%s__\n\n" % self.name
            text_file.write(name_input)
        if self.author:
            author_input = "**Автор**: %s\n" % self.author
            text_file.write(author_input)
        if self.reader:
            reader_input = "**Исполняет**: %s\n" % self.reader
            text_file.write(reader_input)
        if self.genre:
            genre_input = "**Жанр**: %s\n" % self.genre
            text_file.write(genre_input)
        if self.duration:
            duration = "**Продолжительность**: %s\n" % self.duration
            text_file.write(duration)
        if self.desc:
            desc_input = "\n**Описание**:\n%s\n" % self.desc
            text_file.write(desc_input)
        if self.add_desc:
            add_desc_input = "\n%s" % self.add_desc
            text_file.write(add_desc_input)

        self.status('Файл создан')
        text_file.close()

    # Clear inputs
    def clear(self):
        self.nameEdit.clear()
        self.authorEdit.clear()
        self.readEdit.clear()
        self.genreEdit.clear()
        self.durationEdit.clear()
        self.textEdit.clear()
        self.addDessEdit.clear()

        self.status('Очищено')

    # Set status
    def status(self, text):
        self.statusLabel.setText(text)

    # Get soup (html) from url.
    def get_soup(self, url):
        try:
            r = requests.get(url)
            if r:
                return BeautifulSoup(r.content, 'html.parser')
            else:
                self.status('Not found')

        except Exception as msg:
            self.status(f'Not found:\n {str(msg)}')

    # Get input text
    def parse_input(self, body, text=''):
        # find text
        if not text:
            return refined(body.span.get_text(strip=True))
        return refined(body.find('span', text=text).next_sibling)


# Remove symbols
def refined(text):
    # : First name : Last name
    return text.replace(':', '').strip()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
