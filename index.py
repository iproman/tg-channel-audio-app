# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Labels
        font = QtGui.QFont()
        font.setPointSize(9)

        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(70, 30, 90, 25))
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")

        self.authorLabel = QtWidgets.QLabel(self.centralwidget)
        self.authorLabel.setGeometry(QtCore.QRect(70, 80, 90, 25))
        self.authorLabel.setFont(font)
        self.authorLabel.setObjectName("authorLabel")

        self.readlabel = QtWidgets.QLabel(self.centralwidget)
        self.readlabel.setGeometry(QtCore.QRect(70, 130, 90, 25))
        self.readlabel.setFont(font)
        self.readlabel.setObjectName("readlabel")

        self.genreLabel = QtWidgets.QLabel(self.centralwidget)
        self.genreLabel.setGeometry(QtCore.QRect(70, 180, 90, 25))
        self.genreLabel.setFont(font)
        self.genreLabel.setObjectName("genreLabel")

        self.descLabel = QtWidgets.QLabel(self.centralwidget)
        self.descLabel.setGeometry(QtCore.QRect(70, 230, 90, 25))
        self.descLabel.setFont(font)
        self.descLabel.setObjectName("descLabel")

        self.addDessLabel = QtWidgets.QLabel(self.centralwidget)
        self.addDessLabel.setGeometry(QtCore.QRect(70, 320, 90, 25))
        self.addDessLabel.setFont(font)
        self.addDessLabel.setObjectName("addDessLabel")

        # Buttons
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 390, 100, 30))
        self.pushButton.setObjectName("pushButton")

        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(170, 30, 350, 25))
        self.nameEdit.setObjectName("nameEdit")

        self.authorEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.authorEdit.setGeometry(QtCore.QRect(170, 80, 350, 25))
        self.authorEdit.setObjectName("authorEdit")

        self.readEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.readEdit.setGeometry(QtCore.QRect(170, 130, 350, 25))
        self.readEdit.setObjectName("readEdit")

        self.genreEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.genreEdit.setGeometry(QtCore.QRect(170, 180, 350, 25))
        self.genreEdit.setObjectName("genreEdit")

        self.addDessEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addDessEdit.setGeometry(QtCore.QRect(170, 320, 350, 25))
        self.addDessEdit.setObjectName("addDessEdit")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 230, 350, 70))
        self.textEdit.setObjectName("textEdit")

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
        self.nameLabel.setText(_translate("MainWindow", "Имя:"))
        self.authorLabel.setText(_translate("MainWindow", "Автор:"))
        self.readlabel.setText(_translate("MainWindow", "Исполняет:"))
        self.genreLabel.setText(_translate("MainWindow", "Жанр:"))
        self.descLabel.setText(_translate("MainWindow", "Описание:"))
        self.addDessLabel.setText(_translate("MainWindow", "Доп описание:"))
        self.pushButton.setText(_translate("MainWindow", "Подготовить"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
