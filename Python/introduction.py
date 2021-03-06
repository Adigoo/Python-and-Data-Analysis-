# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'introduction.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from malware import malui
from phishing import phiui
from sql import sqlui
from xss import xssui
from dos import dosui
from hijack import hijackui
from reuse import reuseui
import main

def introui(abc):
    f3 = QtWidgets.QFrame(abc)
    f3.setGeometry(QtCore.QRect(0, 0, 801, 581))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    f3.setFont(font)
    f3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
    f3.setAutoFillBackground(False)
    f3.setStyleSheet("background-color: rgb(255, 255, 255);")
    f3.setFrameShape(QtWidgets.QFrame.StyledPanel)
    f3.setFrameShadow(QtWidgets.QFrame.Raised)
    f3.setObjectName("f3")
    back = QtWidgets.QPushButton(f3)
    back.setGeometry(QtCore.QRect(20, 10, 61, 21))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(11)
    font.setBold(True)
    font.setItalic(False)
    font.setWeight(75)
    back.setFont(font)
    back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    back.setStyleSheet("background-color: rgb(255, 255, 255);")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("back1600.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    back.setIcon(icon)
    back.setObjectName("back")
    intro_head = QtWidgets.QLabel(f3)
    intro_head.setGeometry(QtCore.QRect(240, 10, 331, 41))
    font = QtGui.QFont()
    font.setPointSize(18)
    font.setBold(True)
    font.setItalic(True)
    font.setWeight(75)
    intro_head.setFont(font)
    intro_head.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 203, 70, 255), stop:1 rgba(255, 255, 255, 255));")
    intro_head.setFrameShape(QtWidgets.QFrame.NoFrame)
    intro_head.setFrameShadow(QtWidgets.QFrame.Sunken)
    intro_head.setObjectName("intro_head")
    intro = QtWidgets.QLabel(f3)
    intro.setGeometry(QtCore.QRect(10, 60, 771, 251))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(12)
    font.setBold(False)
    font.setWeight(50)
    intro.setFont(font)
    intro.setObjectName("intro")
    type = QtWidgets.QLabel(f3)
    type.setGeometry(QtCore.QRect(20, 330, 311, 41))
    font = QtGui.QFont()
    font.setPointSize(18)
    font.setBold(True)
    font.setItalic(True)
    font.setWeight(75)
    type.setFont(font)
    type.setStyleSheet("")
    type.setObjectName("type")
    malware = QtWidgets.QPushButton(f3)
    malware.setGeometry(QtCore.QRect(20, 390, 101, 31))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    malware.setFont(font)
    malware.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    malware.setStyleSheet("background-color: rgb(167, 255, 142);")
    malware.setObjectName("malware")
    phishing = QtWidgets.QPushButton(f3)
    phishing.setGeometry(QtCore.QRect(20, 430, 111, 31))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    phishing.setFont(font)
    phishing.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    phishing.setStyleSheet("background-color: rgb(167, 255, 142);\n"
"")
    phishing.setObjectName("phishing")
    sql = QtWidgets.QPushButton(f3)
    sql.setGeometry(QtCore.QRect(20, 470, 201, 31))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    sql.setFont(font)
    sql.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    sql.setStyleSheet("background-color: rgb(167, 255, 142);")
    sql.setObjectName("sql")
    script = QtWidgets.QPushButton(f3)
    script.setGeometry(QtCore.QRect(20, 510, 201, 31))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    script.setFont(font)
    script.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    script.setStyleSheet("background-color: rgb(167, 255, 142);")
    script.setObjectName("script")
    dos = QtWidgets.QPushButton(f3)
    dos.setGeometry(QtCore.QRect(370, 390, 221, 31))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    dos.setFont(font)
    dos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    dos.setStyleSheet("background-color: rgb(167, 255, 142);")
    dos.setObjectName("dos")
    hack = QtWidgets.QPushButton(f3)
    hack.setGeometry(QtCore.QRect(370, 430, 401, 31))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    hack.setFont(font)
    hack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    hack.setStyleSheet("background-color: rgb(167, 255, 142);")
    hack.setObjectName("hack")
    reuse = QtWidgets.QPushButton(f3)
    reuse.setGeometry(QtCore.QRect(370, 470, 181, 31))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    reuse.setFont(font)
    reuse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    reuse.setStyleSheet("background-color: rgb(167, 255, 142);")
    reuse.setObjectName("reuse")

    back.setText("Back")
    intro_head.setText("      INTRODUCTION")
    intro.setText("        Computer security, also known as cyber security or IT security,\n"
"is the protection of computer systems from the theft or damage to their hardware,\n"
" software or information, as well as from disruption or misdirection of the services they provide.\n"
"\n"
"         Cyber security includes controlling physical access to the hardware,\n"
" as well as protecting against harm that may come via network access, data and code injection.\n"
" Also, due to malpractice by operators, whether intentional, accidental,\n"
" IT security is susceptible to being tricked into deviating from secure procedures through various methods.\n"
"\n"
"         The field is of growing importance due to the increasing reliance on computer systems and the\n"
"Internet,wireless networks such as Bluetooth and Wi-Fi, and the growth of \"smart\" devices,\n"
" including smartphones, televisions and tiny devices as part of the Internet of Things.")
    type.setText("Types of Cyber Attacks :")
    malware.setText("1. Malware")
    phishing.setText("2. Phishing")
    sql.setText("3. SQL Injection Attack")
    script.setText("4. Cross-Site Scripting")
    dos.setText("5. Denial of Service (DoS)")
    hack.setText("6. Session Hijacking and Man-in-the-Middle Attacks ")
    reuse.setText("7. Credential Reuse")
    
    f3.show()
    back.show()
    intro_head.show()
    intro.show()
    type.show()
    malware.show()
    phishing.show()
    sql.show()
    script.show()
    dos.show()
    hack.show()
    reuse.show()

    def fuct():
        f3.hide()
        back.hide()
        intro_head.hide()
        intro.hide()
        type.hide()
        malware.hide()
        phishing.hide()
        sql.hide()
        script.hide()
        dos.hide()
        hack.hide()
        reuse.hide()
        malui(abc)
        
    malware.clicked.connect(fuct)
        
    def fuct1():
        f3.hide()
        back.hide()
        intro_head.hide()
        intro.hide()
        type.hide()
        malware.hide()
        phishing.hide()
        sql.hide()
        script.hide()
        dos.hide()
        hack.hide()
        reuse.hide()
        phiui(abc)
    phishing.clicked.connect(fuct1)

    def fuct2():
        f3.hide()
        back.hide()
        intro_head.hide()
        intro.hide()
        type.hide()
        malware.hide()
        phishing.hide()
        sql.hide()
        script.hide()
        dos.hide()
        hack.hide()
        reuse.hide()
        sqlui(abc)

    sql.clicked.connect(fuct2)

    def fuct3():
        f3.hide()
        back.hide()
        intro_head.hide()
        intro.hide()
        type.hide()
        malware.hide()
        phishing.hide()
        sql.hide()
        script.hide()
        dos.hide()
        hack.hide()
        reuse.hide()
        xssui(abc)

    script.clicked.connect(fuct3)

    def fuct4():
        f3.hide()
        back.hide()
        intro_head.hide()
        intro.hide()
        type.hide()
        malware.hide()
        phishing.hide()
        sql.hide()
        script.hide()
        dos.hide()
        hack.hide()
        reuse.hide()
        dosui(abc)

    dos.clicked.connect(fuct4)

    def fuct5():
        f3.hide()
        back.hide()
        intro_head.hide()
        intro.hide()
        type.hide()
        malware.hide()
        phishing.hide()
        sql.hide()
        script.hide()
        dos.hide()
        hack.hide()
        reuse.hide()
        hijackui(abc)

    hack.clicked.connect(fuct5)

    def fuct6():
        f3.hide()
        back.hide()
        intro_head.hide()
        intro.hide()
        type.hide()
        malware.hide()
        phishing.hide()
        sql.hide()
        script.hide()
        dos.hide()
        hack.hide()
        reuse.hide()
        reuseui(abc)

    reuse.clicked.connect(fuct6)


    def back1():
        f3.hide()
        back.hide()
        intro_head.hide()
        intro.hide()
        type.hide()
        malware.hide()
        phishing.hide()
        sql.hide()
        script.hide()
        dos.hide()
        hack.hide()
        reuse.hide()
        main.mainui(abc)

    back.clicked.connect(back1)
