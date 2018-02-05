# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xss.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import introduction

def xssui(abc):
    
    f7 = QtWidgets.QFrame(abc)
    f7.setGeometry(QtCore.QRect(0, 0, 791, 581))
    f7.setStyleSheet("background-color: rgb(255, 255, 255);")
    f7.setFrameShape(QtWidgets.QFrame.StyledPanel)
    f7.setFrameShadow(QtWidgets.QFrame.Raised)
    f7.setObjectName("f7")
    back = QtWidgets.QPushButton(f7)
    back.setGeometry(QtCore.QRect(10, 10, 75, 23))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    back.setFont(font)
    back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("back1600.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    back.setIcon(icon)
    back.setObjectName("back")
    label = QtWidgets.QLabel(f7)
    label.setGeometry(QtCore.QRect(120, 20, 631, 51))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(24)
    font.setBold(True)
    font.setItalic(True)
    font.setWeight(75)
    label.setFont(font)
    label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
    label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142, 192, 52, 255), stop:1 rgba(255, 255, 255, 255));")
    label.setObjectName("label")
    label_2 = QtWidgets.QLabel(f7)
    label_2.setGeometry(QtCore.QRect(20, 80, 761, 371))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(11)
    label_2.setFont(font)
    label_2.setObjectName("label_2")
    
   
    back.setText( "Back")
    label.setText( "      4. Cross-Site Scripting (XSS) ")
    label_2.setText( "     In an SQL injection attack, an attacker goes after a vulnerable website to target its stored data, such\n"
" as user credentials or sensitive financial data. But if the attacker would rather directly target a website\'s\n"
"users, they may opt for a cross-site scripting attack. Similar to an SQL injection attack, this attack also\n"
"involves injecting malicious code into a website, but in this case the website itself is not being attacked.\n"
"Instead, the malicious code the attacker has injected only runs in the user\'s browser when they visit the \n"
"attacked website, and it goes after the visitor directly, not the website.\n"
"\n"
"      One of the most common ways an attacker can deploy a cross-site scripting attack is by injecting\n"
"malicious code into a comment or a script that could automatically run. For example, they could embed \n"
"a link to a malicious JavaScript in a comment on a blog. \n"
"\n"
"       Cross-site scripting attacks can significantly damage a website’s reputation by placing the users\' \n"
"information at risk without any indication that anything malicious even occurred. Any sensitive information \n"
"a user sends to the site—such as their credentials, credit card information, or other private data—can be \n"
"hijacked via cross-site scripting without the website owners realizing there was even a \n"
"problem in the first place.")

    f7.show()
    back.show()
    label.show()
    label_2.show()

    def back1():
        f7.hide()
        back.hide()
        label.hide()
        label_2.hide()
        introduction.introui(abc)

    back.clicked.connect(back1)



