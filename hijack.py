# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hijack.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import introduction

def hijackui(abc):
    
    f8 = QtWidgets.QFrame(abc)
    f8.setGeometry(QtCore.QRect(0, 0, 801, 581))
    f8.setStyleSheet("background-color: rgb(255, 255, 255);")
    f8.setFrameShape(QtWidgets.QFrame.StyledPanel)
    f8.setFrameShadow(QtWidgets.QFrame.Raised)
    f8.setObjectName("f8")
    back = QtWidgets.QPushButton(f8)
    back.setGeometry(QtCore.QRect(10, 10, 75, 23))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    back.setFont(font)
    back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("back1600.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    back.setIcon(icon)
    back.setObjectName("back")
    label = QtWidgets.QLabel(f8)
    label.setGeometry(QtCore.QRect(110, 10, 661, 51))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(20)
    font.setBold(True)
    font.setItalic(True)
    font.setWeight(75)
    label.setFont(font)
    label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142, 192, 52, 255), stop:1 rgba(255, 255, 255, 255));")
    label.setObjectName("label")
    label_2 = QtWidgets.QLabel(f8)
    label_2.setGeometry(QtCore.QRect(20, 80, 771, 401))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(11)
    label_2.setFont(font)
    label_2.setObjectName("label_2")
    

    
    back.setText( "Back")
    label.setText( "     6.Session Hijacking and Man-in-the-Middle Attacks")
    label_2.setText( "      When you\'re on the internet, your computer has a lot of small back-and-forth transactions with servers\n"
"around the world letting them know who you are and requesting specific websites or serv\n"
"ices. In return, if everything goes  as it should, the web servers should respond to your request by giving\n"
" you the information you\'re accessing. This process, or session, happens whether you are simply\n"
" browsing or when you are logging into a website with your username and password.\n"
"\n"
"      The session between your computer and the remote web server is given a unique session ID, which\n"
" should  stay private between the two parties; however, an attacker can hijack the session by capturing the\n"
" session ID and posing as the computer making a request, allowing them to log in as an unsuspecting user \n"
"and gain access to unauthorized information on the web server. There are a number of methods an attacker\n"
" can use to steal the session ID, such as a cross-site scripting attack used to hijack session IDs.\n"
"\n"
"      An attacker can also opt to hijack the session to insert themselves between the requesting computer \n"
"and the remote server, pretending to be the other party in the session. This allows them to intercept\n"
"information in both directions and is commonly called a man-in-the-middle attack. \n"
"\n"
"       ")

    f8.show()
    back.show()
    label.show()
    label_2.show()

    def back1():
        f8.hide()
        back.hide()
        label.hide()
        label_2.hide()
        introduction.introui(abc)

    back.clicked.connect(back1)



