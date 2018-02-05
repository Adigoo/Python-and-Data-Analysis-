# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dos.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import introduction


def dosui(abc):
    f7 = QtWidgets.QFrame(abc)
    f7.setGeometry(QtCore.QRect(0, 0, 801, 571))
    f7.setStyleSheet("background-color: rgb(255, 255, 255);")
    f7.setFrameShape(QtWidgets.QFrame.StyledPanel)
    f7.setFrameShadow(QtWidgets.QFrame.Raised)
    f7.setObjectName("f7")
    back = QtWidgets.QPushButton(f7)
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
    label = QtWidgets.QLabel(f7)
    label.setGeometry(QtCore.QRect(110, 20, 661, 61))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(24)
    font.setBold(True)
    font.setItalic(True)
    font.setWeight(75)
    label.setFont(font)
    label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142, 192, 52, 255), stop:1 rgba(255, 255, 255, 255));")
    label.setObjectName("label")
    label_2 = QtWidgets.QLabel(f7)
    label_2.setGeometry(QtCore.QRect(10, 100, 771, 431))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(11)
    label_2.setFont(font)
    label_2.setObjectName("label_2")
    

   

   
    back.setText( "Back")
    label.setText( "        5.Denial of Service (DoS) ")
    label_2.setText( "     Imagine you\'re sitting in traffic on a one-lane country road, with cars backed up as far as the eye can see.\n"
"Normally this road never sees more than a car or two, but a county fair and a major sporting event have ended \n"
"around the same time, and this road is the only way for visitors to leave town. The road can\'t handle\n"
"the massive amount of traffic, and as a result it gets so backed up that pretty much no one can leave.\n"
"\n"
"     That\'s essentially what happens to a website during a denial of service (DoS) attack. If you flood\n"
"a website with more traffic than it was built to handle, you\'ll overload the website\'s server and it\'ll be nigh-\n"
"impossible for the website to serve up its content to visitors who are trying to access it. \n"
"\n"
"       This can happen for innocuous reasons of course, say if a massive news story breaks and a newspaper\'s\n"
"website gets overloaded with traffic from people trying to find out more. But often, this kind of traffic overload \n"
"is malicious, as an attacker floods a website with an overwhelming amount of traffic to essentially shut it\n"
" down for all users.\n"
"\n"
"         In some instances, these DoS attacks are performed by many computers at the same time. This \n"
"scenario of attack is known as a Distributed Denial of Service Attack (DDoS). This type of attack can be \n"
"even more difficult to overcome due to the attacker appearing from many different IP addresses\n"
" around the world simultaneously,making determining the source of the attack even more difficult for\n"
" network administrators. ")

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
        




