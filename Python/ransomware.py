# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ransomware.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import main


def ranui(abc):
    frame = QtWidgets.QFrame(abc)
    frame.setGeometry(QtCore.QRect(0, 0, 801, 571))
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
    label.setGeometry(QtCore.QRect(210, 10, 491, 41))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(24)
    font.setBold(True)
    font.setItalic(True)
    font.setWeight(75)
    label.setFont(font)
    label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 252, 156, 255), stop:1 rgba(255, 255, 255, 255));")
    label.setObjectName("label")
    label_2 = QtWidgets.QLabel(frame)
    label_2.setGeometry(QtCore.QRect(10, 60, 751, 351))
    font = QtGui.QFont()
    font.setFamily("Rockwell")
    font.setPointSize(11)
    label_2.setFont(font)
    label_2.setObjectName("label_2")
    label_3 = QtWidgets.QLabel(frame)
    label_3.setGeometry(QtCore.QRect(20, 430, 341, 21))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(20)
    font.setBold(True)
    font.setItalic(True)
    font.setWeight(75)
    label_3.setFont(font)
    label_3.setObjectName("label_3")
    rattack = QtWidgets.QPushButton(frame)
    rattack.setGeometry(QtCore.QRect(20, 470, 161, 31))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    rattack.setFont(font)
    rattack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    rattack.setStyleSheet("background-color: rgb(223, 255, 14);")
    rattack.setObjectName("rattack")
    industry = QtWidgets.QPushButton(frame)
    industry.setGeometry(QtCore.QRect(20, 510, 211, 31))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    industry.setFont(font)
    industry.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    industry.setStyleSheet("background-color: rgb(223, 255, 14);")
    industry.setObjectName("industry")

    back.setText("Back")
    label.setText("          Ransomware")
    label_2.setText("       Ransomware is a type of malicious software from cryptovirology that threatens to publish the victim\'s data or\n"
" perpetually block access to it unless a ransom is paid. While some simple ransomware may lock the system \n"
"in a way which is not difficult for a knowledgeable person to reverse, more advanced malware uses a \n"
"technique called cryptoviral extortion,in which it encrypts the victim\'s files, making them inaccessible,\n"
" and demands a ransom payment to decrypt them In a properly implemented cryptoviral extortion attack,\n"
"recovering the files without the decryption key is an intractable problem – and difficult to trace digital \n"
"currencies such as Ukash and Bitcoin are used for the ransoms, making tracing and prosecuting the\n"
" perpetrators difficult.\n"
"\n"
"       Ransomware attacks are typically carried out using a Trojan that is disguised as a legitimate file that \n"
"the user is tricked into downloading or opening when it arrives as an email attachment. However, one \n"
"high-profile example, the \"WannaCry worm\", traveled automatically between computers without user \n"
"interaction.\n"
"\n"
"         Starting from around 2012 the use of ransomware scams has grown internationally. in June 2013, \n"
"vendor McAfee released data showing that it had collected more than double the number of samples\n"
" of ransomware that quarter than it had in the same quarter of the previous year. CryptoLocker was\n"
"particularly successful, procuring an estimated US $3 million before it was taken down by authorities,\n"
"and CryptoWall was estimated by the US Federal Bureau of Investigation (FBI) to have accrued over\n"
" US $18m by June 2015.")
    label_3.setText("Ransomware Statistics 2016")
    rattack.setText("Monthly Attacks")
    industry.setText("Industries Area Affected")

    frame.show()
    label.show()
    label_2.show()
    label_3.show()
    rattack.show()
    industry.show()
    back.show()


    def back1():
        frame.hide()
        label.hide()
        label_2.hide()
        label_3.hide()
        rattack.hide()
        industry.hide()
        back.hide()
        main.mainui(abc)

    back.clicked.connect(back1)
        
    def monthly():
        import matplotlib.pyplot as plt
        plt.rcdefaults()
        import matplotlib.pyplot as plt
        import csv
        import numpy as np

        y = []
        x = []
    
        with open('ransomeware.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in plots:
                x.append(row[0])
                a=float(row[1])
                y.append(a)
             
        y_pos=np.arange(len(x))

        plt.barh(y_pos, y, align='center', alpha=0.5)
        plt.yticks(y_pos, x)
        plt.xlabel('Number of attacks(in thousand')
        plt.title('Ransomeware attacks in 2016 monthly report')
        plt.show()

    rattack.clicked.connect(monthly)
    
    def indus():
        import matplotlib.pyplot as plt
        plt.rcdefaults()
        import matplotlib.pyplot as plt
        import csv
        import numpy as np
        
        y = []
        x = []

        with open('categories.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in plots:
                x.append(row[0])
                a=float(row[1])
                y.append(a)
             
        y_pos=np.arange(len(x))

        plt.barh(y_pos, y, align='center', alpha=0.5)
        plt.yticks(y_pos, x)
        plt.xlabel('Number of attacks(in %)')
        plt.title('Ransomeware Stats by Industry')
        plt.show()
        
    industry.clicked.connect(indus)
