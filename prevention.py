# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prevention.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import main

def preui(abc):
    frame = QtWidgets.QFrame(abc)
    frame.setGeometry(QtCore.QRect(0, 0, 801, 581))
    frame.setStyleSheet("background-color: rgb(255, 255, 255);")
    frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame.setFrameShadow(QtWidgets.QFrame.Raised)
    frame.setObjectName("frame")
    back = QtWidgets.QPushButton(frame)
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
    label = QtWidgets.QLabel(frame)
    label.setGeometry(QtCore.QRect(230, 10, 401, 41))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(24)
    font.setBold(True)
    font.setItalic(True)
    font.setWeight(75)
    label.setFont(font)
    label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(196, 255, 156, 255), stop:1 rgba(255, 255, 255, 255));")
    label.setObjectName("label")
    label_2 = QtWidgets.QLabel(frame)
    label_2.setGeometry(QtCore.QRect(10, 60, 221, 31))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(14)
    font.setBold(True)
    font.setWeight(75)
    label_2.setFont(font)
    label_2.setObjectName("label_2")
    label_3 = QtWidgets.QLabel(frame)
    label_3.setGeometry(QtCore.QRect(60, 90, 581, 211))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(11)
    label_3.setFont(font)
    label_3.setObjectName("label_3")
    label_4 = QtWidgets.QLabel(frame)
    label_4.setGeometry(QtCore.QRect(10, 300, 331, 31))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(14)
    font.setBold(True)
    font.setWeight(75)
    label_4.setFont(font)
    label_4.setLineWidth(1)
    label_4.setObjectName("label_4")
    label_5 = QtWidgets.QLabel(frame)
    label_5.setGeometry(QtCore.QRect(60, 330, 741, 151))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(11)
    label_5.setFont(font)
    label_5.setObjectName("label_5")

    back.setText("Back")
    label.setText("       Prevention")
    label_2.setText("Tips to avoid cyber attacks:")
    label_3.setText("1. Set up your computer for automatic software and operating system updates\n"
"2. Install protective software.\n"
"3. Choose strong passwords\n"
"4. BACK UP on a regular basis\n"
"5. Control access to your machine.\n"
"6. Use email and the internet safely.\n"
"7. Use secure connections like HTTPS\n"
"8. Protect sensitive data\n"
"9. Use desktop firewalls\n"
"10. Do not store your passwords in browers\n"
"11. Stay current with the latest developments for your operating systems.")
    label_4.setText("Technologies can be use to avoid attacks:")
    label_5.setText("1. Cloud access security brokers\n"
"2. Endpoint detection and response (EDR)\n"
"3. Nonsignature approaches for endpoint prevention\n"
"4. User and entity behavioural analytics\n"
"5. Microsegmentation and flow visibility\n"
"6. Intelligence-driven security operations centre orchestration solutions\n"
"7. Remote browser\n"
"8. Pervasive trust services")

    frame.show()
    label.show()
    label_2.show()
    label_3.show()
    label_4.show()
    label_5.show()
    back.show()

    def back1():
        frame.hide()
        label.hide()
        label_2.hide()
        label_3.hide()
        label_4.hide()
        label_5.hide()
        back.show()
        main.mainui(abc)

    back.clicked.connect(back1)

