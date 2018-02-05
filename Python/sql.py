# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sql.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import introduction

def sqlui(abc):
    
    f6 = QtWidgets.QFrame(abc)
    f6.setGeometry(QtCore.QRect(0, 0, 801, 581))
    f6.setStyleSheet("background-color: rgb(255, 255, 255);")
    f6.setFrameShape(QtWidgets.QFrame.StyledPanel)
    f6.setFrameShadow(QtWidgets.QFrame.Raised)
    f6.setObjectName("f6")
    back = QtWidgets.QPushButton(f6)
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
    label = QtWidgets.QLabel(f6)
    label.setGeometry(QtCore.QRect(120, 20, 611, 61))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(24)
    font.setBold(True)
    font.setItalic(True)
    font.setWeight(75)
    label.setFont(font)
    label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142, 192, 52, 255), stop:1 rgba(255, 255, 255, 255));")
    label.setObjectName("label")
    label_2 = QtWidgets.QLabel(f6)
    label_2.setGeometry(QtCore.QRect(10, 100, 771, 331))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(11)
    label_2.setFont(font)
    label_2.setObjectName("label_2")
    

    
    back.setText( "Back")
    label.setText( "        3. SQL Injection Attack")
    label_2.setText( "        SQL (pronounced “sequel”) stands for structured query language; it’s a programming language used\n"
"to communicate with databases. Many of the servers that store critical data for websites and services \n"
"use SQL to manage the data in their databases. A SQL injection attack specifically targets this kind of \n"
"server,  using malicious code to get the server to divulge information it normally wouldn’t. This is especially\n"
"problematic if the server stores private customer information from the website, such as credit card numbers, usernames and\n"
"passwords (credentials), or other personally identifiable information, which are tempting and lucrative \n"
"targets for an attacker.\n"
"\n"
"       An SQL injection attack works by exploiting any one of the known SQL vulnerabilities that allow \n"
"the SQL server to run malicious code. For example, if a SQL server is vulnerable to an injection attack, it may be \n"
"possible for an attacker to go to a website\'s search box and type in code that  of its stored usernames and passwords for the site. would force the site\'s SQL \n"
"server to dump all")

    f6.show()
    label.show()
    back.show()
    label_2.show()

    def back1():
        f6.hide()
        label.hide()
        back.hide()
        label_2.hide()
        introduction.introui(abc)

    back.clicked.connect(back1)


