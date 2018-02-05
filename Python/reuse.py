# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reuse.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import introduction
def reuseui(abc):
    
    f9 = QtWidgets.QFrame(abc)
    f9.setGeometry(QtCore.QRect(0, 0, 801, 581))
    f9.setStyleSheet("background-color: rgb(255, 255, 255);")
    f9.setFrameShape(QtWidgets.QFrame.StyledPanel)
    f9.setFrameShadow(QtWidgets.QFrame.Raised)
    f9.setObjectName("f9")
    back = QtWidgets.QPushButton(f9)
    back.setGeometry(QtCore.QRect(10, 10, 75, 23))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    back.setFont(font)
    back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    back.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("back1600.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    back.setIcon(icon)
    back.setObjectName("back")
    label = QtWidgets.QLabel(f9)
    label.setGeometry(QtCore.QRect(180, 10, 511, 41))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(24)
    font.setBold(True)
    font.setItalic(True)
    font.setWeight(75)
    label.setFont(font)
    label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142, 192, 52, 255), stop:1 rgba(255, 255, 255, 255));")
    label.setObjectName("label")
    label_2 = QtWidgets.QLabel(f9)
    label_2.setGeometry(QtCore.QRect(20, 80, 771, 331))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(11)
    label_2.setFont(font)
    label_2.setObjectName("label_2")
    

    
    back.setText( "Back")
    label.setText( "       7.Credential Reuse")
    label_2.setText( "    Users today have so many logins and passwords to remember that it’s tempting to reuse credentials \n"
"here or there to make life a little easier. Even though security best practices universally recommend that you\n"
" have unique passwords for all your applications and websites, many people still reuse\n"
"their passwords —a fact attackers rely on. \n"
"\n"
"       Once attackers have a collection of usernames and passwords from a breached website or service\n"
"(easily acquired on any number of black market websites on the internet), they know that if they use these \n"
"same credentials on other websites there’s a chance they’ll be able to log in. No matter how tempting it may\n"
"be  reuse credentials for your email, bank account, and your favorite sports forum, it’s possible that one day \n"
"the forum will get hacked, giving an attacker easy access to your email and bank account.\n"
" When it comes to credentials, variety is essential. Password managers are available and can be helpful when\n"
"it comes to managing the various credentials you use.\n"
"\n"
"       ")
    f9.show()
    back.show()
    label.show()
    label_2.show()

    def back1():
        f9.hide()
        back.hide()
        label.hide()
        label_2.hide()
        introduction.introui(abc)

    back.clicked.connect(back1)


