# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phishing.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import introduction

def phiui(abc):
   
    f5 = QtWidgets.QFrame(abc)
    f5.setGeometry(QtCore.QRect(0, 0, 801, 581))
    f5.setStyleSheet("background-color: rgb(255, 255, 255);")
    f5.setFrameShape(QtWidgets.QFrame.StyledPanel)
    f5.setFrameShadow(QtWidgets.QFrame.Raised)
    f5.setObjectName("f5")
    back = QtWidgets.QPushButton(f5)
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
    label = QtWidgets.QLabel(f5)
    label.setGeometry(QtCore.QRect(200, 10, 461, 51))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(24)
    font.setBold(True)
    font.setItalic(True)
    font.setWeight(75)
    label.setFont(font)
    label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142, 192, 52, 255), stop:1 rgba(255, 255, 255, 255));")
    label.setObjectName("label")
    label_2 = QtWidgets.QLabel(f5)
    label_2.setGeometry(QtCore.QRect(10, 70, 781, 371))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(11)
    label_2.setFont(font)
    label_2.setObjectName("label_2")
    
   
    back.setText( "Back")
    label.setText( "         2. Phishing")
    label_2.setText( "      Of course, chances are you wouldn\'t just open a random attachment or click on a link in any email\n"
" that comes your way—there has to be a compelling reason for you to take action. Attackers know this, too.\n"
" When an attacker wants you to install malware or divulge sensitive information, they often turn to phishing\n"
"tactics, or pretending to be someone or something else to get you to take an action you normally wouldn’t.\n"
"Since they rely on human curiosity and impulses, phishing attacks can be difficult to stop.\n"
"\n"
"       In a phishing attack, an attacker may send you an email that appears to be from someone you \n"
"trust,like your boss or a company you do business with. The email will seem legitimate, and it will have some \n"
"urgency to it(e.g. fraudulent activity has been detected on your account). In the email, there will be an \n"
"attachment to open or a link to click.Upon opening the malicious attachment, you’ll thereby install malware in your computer. \n"
"If you click the link, it may send you to a legitimate-looking website that asks for you to log in \n"
"to access an important file except the website is actually a trap used to capture your credentials when you try \n"
"to log in.")

    f5.show()
    back.show()
    label.show()
    label_2.show()

    def back1():
        f5.hide()
        back.hide()
        label.hide()
        label_2.hide()
        introduction.introui(abc)

    back.clicked.connect(back1)
        


