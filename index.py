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
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # Labels
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.authorLabel = QtWidgets.QLabel(self.centralwidget)
        self.readlabel = QtWidgets.QLabel(self.centralwidget)
        self.genreLabel = QtWidgets.QLabel(self.centralwidget)
        self.durationLabel = QtWidgets.QLabel(self.centralwidget)
        self.descriptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.addDessLabel = QtWidgets.QLabel(self.centralwidget)
        self.trackerLabel = QtWidgets.QLabel(self.centralwidget)

        # Inputs
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.authorEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.readEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.genreEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.durationEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.descriptionEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.additionDescripionEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.trackerEdit = QtWidgets.QLineEdit(self.centralwidget)

        # Buttons
        self.pushBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.trackerBtn = QtWidgets.QPushButton(self.centralwidget)

        # Addition
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.lengthLabel = QtWidgets.QLabel(self.centralwidget)

        # MenuBar, statusBar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

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

    # Set object properties
    def set_object_properties(self):
        # Labels
        self.nameLabel.setGeometry(QtCore.QRect(self.label_x, 30, self.lwidth, self.lheight))
        self.authorLabel.setGeometry(QtCore.QRect(self.label_x, 80, self.lwidth, self.lheight))
        self.readlabel.setGeometry(QtCore.QRect(self.label_x, 130, self.lwidth, self.lheight))
        self.genreLabel.setGeometry(QtCore.QRect(self.label_x, 180, self.lwidth, self.lheight))
        self.durationLabel.setGeometry(QtCore.QRect(self.label_x, 230, self.lwidth, self.lheight))
        self.descriptionLabel.setGeometry(QtCore.QRect(self.label_x, 280, self.lwidth, self.lheight))
        self.addDessLabel.setGeometry(QtCore.QRect(self.label_x, 370, self.lwidth, self.lheight))
        self.trackerLabel.setGeometry(QtCore.QRect(self.label_x, 550, self.lwidth, self.lheight))

        # Inputs
        self.nameEdit.setGeometry(QtCore.QRect(self.input_x, 30, self.iwidth, self.iheigth))
        self.authorEdit.setGeometry(QtCore.QRect(self.input_x, 80, self.iwidth, self.iheigth))
        self.readEdit.setGeometry(QtCore.QRect(self.input_x, 130, self.iwidth, self.iheigth))
        self.genreEdit.setGeometry(QtCore.QRect(self.input_x, 180, self.iwidth, self.iheigth))
        self.durationEdit.setGeometry(QtCore.QRect(self.input_x, 230, self.iwidth, self.iheigth))
        self.descriptionEdit.setGeometry(QtCore.QRect(self.input_x, 280, self.iwidth, 70))
        self.additionDescripionEdit.setGeometry(QtCore.QRect(self.input_x, 370, self.iwidth, self.iheigth))
        self.trackerEdit.setGeometry(QtCore.QRect(self.input_x, 550, self.iwidth, self.iheigth))

        # Buttons
        self.pushBtn.setGeometry(QtCore.QRect(195, 470, 100, 30))
        self.clearBtn.setGeometry(QtCore.QRect(305, 470, 100, 30))
        self.trackerBtn.setGeometry(QtCore.QRect(250, 600, 100, 30))

        # Addition
        self.statusLabel.setGeometry(QtCore.QRect(50, 420, self.lwidth, self.lheight))
        self.lengthLabel.setGeometry(QtCore.QRect(450, 420, self.lwidth, self.lheight))

        # MenuBar, statusBar
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))

    # Set object names
    def set_object_names(self):
        # Labels
        self.nameLabel.setObjectName("nameLabel")
        self.authorLabel.setObjectName("authorLabel")
        self.readlabel.setObjectName("readlabel")
        self.genreLabel.setObjectName("genreLabel")
        self.durationLabel.setObjectName("durationLabel")
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.addDessLabel.setObjectName("addDessLabel")
        self.trackerLabel.setObjectName("trackerLabel")

        # Inputs
        self.nameEdit.setObjectName("nameEdit")
        self.authorEdit.setObjectName("authorEdit")
        self.readEdit.setObjectName("readEdit")
        self.genreEdit.setObjectName("genreEdit")
        self.durationEdit.setObjectName("durationEdit")
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.additionDescripionEdit.setObjectName("additionDescripionEdit")
        self.trackerEdit.setObjectName("trackerEdit")

        # Buttons
        self.pushBtn.setObjectName("pushBtn")
        self.clearBtn.setObjectName("clearBtn")
        self.trackerBtn.setObjectName("clearBtn")

        # Addition
        self.statusLabel.setObjectName("statusLabel")
        self.lengthLabel.setObjectName("lengthLabel")

        # MenuBar, statusBar
        self.menubar.setObjectName("menubar")
        self.statusbar.setObjectName("statusbar")

    # Set object styles
    def set_object_styles(self):
        font = QtGui.QFont()
        font.setPointSize(9)

        # Labels
        self.nameLabel.setFont(font)
        self.authorLabel.setFont(font)
        self.readlabel.setFont(font)
        self.genreLabel.setFont(font)
        self.durationLabel.setFont(font)
        self.descriptionLabel.setFont(font)
        self.addDessLabel.setFont(font)
        self.trackerLabel.setFont(font)

        # Buttons
        self.pushBtn.setStyleSheet("QPushButton {background-color: #bddef6; color: #0e0e0e; font-size: 13px}"
                                   "QPushButton:hover{background-color: #b3d3ea;}")
        self.clearBtn.setStyleSheet("QPushButton {background-color: #e6edf2; color: #0e0e0e; font-size: 13px}"
                                    "QPushButton:hover{background-color: #cee4f4}")
        self.trackerBtn.setStyleSheet("QPushButton {background-color: #e6edf2; color: #0e0e0e; font-size: 13px}"
                                      "QPushButton:hover{background-color: #cee4f4}")
        # Addition
        self.statusLabel.setStyleSheet("QLabel {color: #6c757d; font-size: 10px}")
        self.lengthLabel.setStyleSheet("QLabel {color: #6c757d; font-size: 10px}")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        self.centralwidget.setObjectName("centralwidget")

        # Set object properties
        self.set_object_properties()

        # Set object names
        self.set_object_names()

        # Set object styles
        self.set_object_styles()

        # Buttons
        self.pushBtn.clicked.connect(self.convert)
        self.clearBtn.clicked.connect(self.clear)
        self.trackerBtn.clicked.connect(self.parse_data)

        # MenuBar, statusBar
        MainWindow.setCentralWidget(self.centralwidget)

        MainWindow.setMenuBar(self.menubar)
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
        self.descriptionLabel.setText(_translate("MainWindow", "Описание:"))
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
        self.desc = self.descriptionEdit.toPlainText()
        self.add_desc = self.additionDescripionEdit.text()

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
        self.descriptionEdit.clear()
        self.additionDescripionEdit.clear()

        self.status('Очищено')

    # Set status
    def status(self, text):
        self.statusLabel.setText(text)

    # Set total input length
    def input_length(self, length):
        text = 'Total length: '
        self.lengthLabel.setText(text + length)

    # Get soup (html) from url
    def get_soup(self, url):
        try:
            r = requests.get(url)
            if r:
                return BeautifulSoup(r.content, 'html.parser')
            else:
                self.status('Not found')

        except Exception as msg:
            self.status(f'Not found:\n {str(msg)}')

    # Parse and set data
    def parse_data(self):
        # Block input/btn
        self.block_inputs_btn(True)

        # Send url and get soup
        url = self.trackerEdit.text()
        soup = self.get_soup(url)

        # Set body
        body = soup.find('div', {'class': 'post_body'})

        # Text to find
        data = {
            'name': 'Имя автора',
            'last_name': 'Фамилия автора',
            'reader': 'Исполнитель',
            'genre': 'Жанр',
            'time': 'Время звучания',
            'description': 'Описание'
        }

        # Get text from inputs
        p = Parser(body)

        name = p.parse_input()
        author_first_name = p.parse_input(data['name'])
        author_last_name = p.parse_input(data['last_name'])
        reader = p.parse_input(data['reader'])
        genre = p.parse_input(data['genre'])
        time = p.parse_input(data['time'])
        description = p.parse_input(data['description'])

        # Set text to inputs
        self.nameEdit.setText(name)
        self.authorEdit.setText(f'{author_first_name} {author_last_name}')
        self.readEdit.setText(reader)
        self.genreEdit.setText(genre)
        self.durationEdit.setText(time)
        self.descriptionEdit.setText(description)

        self.status('Найдено')

        self.block_inputs_btn(False)

    def block_inputs_btn(self, boolean=False):
        if boolean:
            boolean = False
        else:
            boolean = True

        self.nameEdit.setEnabled(boolean)
        self.authorEdit.setEnabled(boolean)
        self.readEdit.setEnabled(boolean)
        self.genreEdit.setEnabled(boolean)
        self.durationEdit.setEnabled(boolean)
        self.descriptionEdit.setEnabled(boolean)
        self.additionDescripionEdit.setEnabled(boolean)

        # Todo: block buttons


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


class Parser(object):
    def __init__(self, body):
        self.body = body

    # Get input text
    def parse_input(self, text=''):
        # find text
        if not text:
            return self.refined(self.body.span.get_text(strip=True))
        return self.refined(self.body.find('span', text=text).next_sibling)

    # Remove symbols
    def refined(self, text):
        # : First name : Last name
        return text.replace(':', '').strip()
