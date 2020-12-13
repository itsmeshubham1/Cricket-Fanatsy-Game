# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
db=sqlite3.connect("Cricket_Fandatabase.db")    #connecting the database
cur=db.cursor()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color: rgb(234, 228, 221);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 50, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.open_cb = QtWidgets.QComboBox(Dialog)
        self.open_cb.setGeometry(QtCore.QRect(100, 120, 161, 31))
        self.open_cb.setObjectName("open_cb")
        self.open_btn = QtWidgets.QPushButton(Dialog)
        self.open_btn.setGeometry(QtCore.QRect(130, 190, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.open_btn.setFont(font)
        self.open_btn.setObjectName("open_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        player=cur.execute("SELECT DISTINCT Name FROM teams;")    #fetching the information from teams table
        data=player.fetchall()
        for i in data:
            self.open_cb.addItem(i[0])

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select  Team"))
        self.open_btn.setText(_translate("Dialog", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
