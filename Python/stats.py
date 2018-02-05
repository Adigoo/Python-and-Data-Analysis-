# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stats.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import main


def statui(abc):
    f10 = QtWidgets.QFrame(abc)
    f10.setGeometry(QtCore.QRect(0, -10, 801, 581))
    f10.setStyleSheet("background-color: rgb(255, 255, 255);")
    f10.setFrameShape(QtWidgets.QFrame.StyledPanel)
    f10.setFrameShadow(QtWidgets.QFrame.Raised)
    f10.setObjectName("f10")
    back = QtWidgets.QPushButton(f10)
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
    label = QtWidgets.QLabel(f10)
    label.setGeometry(QtCore.QRect(320, 130, 451, 351))
    a=QtGui.QMovie("source.gif")
    label.setMovie(a)
    a.start()
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(24)
    font.setBold(True)
    font.setItalic(True)
    font.setWeight(75)
    label.setFont(font)
    label.setStyleSheet("")
    label.setText("")
    label.setPixmap(QtGui.QPixmap("source.gif"))
    label.setObjectName("label")
    label_2 = QtWidgets.QLabel(f10)
    label_2.setGeometry(QtCore.QRect(30, 60, 331, 31))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(18)
    font.setBold(True)
    font.setWeight(75)
    label_2.setFont(font)
    label_2.setObjectName("label_2")
    label_3 = QtWidgets.QLabel(f10)
    label_3.setGeometry(QtCore.QRect(20, 270, 291, 31))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(18)
    font.setBold(True)
    font.setWeight(75)
    label_3.setFont(font)
    label_3.setObjectName("label_3")
    p2008 = QtWidgets.QPushButton(f10)
    p2008.setGeometry(QtCore.QRect(30, 130, 75, 23))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    p2008.setFont(font)
    p2008.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    p2008.setStyleSheet("background-color: rgb(60, 241, 81);")
    p2008.setObjectName("p2008")
    p2009 = QtWidgets.QPushButton(f10)
    p2009.setGeometry(QtCore.QRect(130, 130, 75, 23))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    p2009.setFont(font)
    p2009.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    p2009.setStyleSheet("background-color: rgb(60, 241, 81);")
    p2009.setObjectName("p2009")
    p2010 = QtWidgets.QPushButton(f10)
    p2010.setGeometry(QtCore.QRect(230, 130, 75, 23))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    p2010.setFont(font)
    p2010.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    p2010.setStyleSheet("background-color: rgb(60, 241, 81);")
    p2010.setObjectName("p2010")
    p2011 = QtWidgets.QPushButton(f10)
    p2011.setGeometry(QtCore.QRect(30, 170, 75, 23))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    p2011.setFont(font)
    p2011.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    p2011.setStyleSheet("background-color: rgb(60, 241, 81);")
    p2011.setObjectName("p2011")
    p2013 = QtWidgets.QPushButton(f10)
    p2013.setGeometry(QtCore.QRect(230, 170, 75, 23))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    p2013.setFont(font)
    p2013.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    p2013.setStyleSheet("background-color: rgb(60, 241, 81);")
    p2013.setObjectName("p2013")
    all = QtWidgets.QPushButton(f10)
    all.setGeometry(QtCore.QRect(130, 210, 75, 23))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    all.setFont(font)
    all.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    all.setStyleSheet("background-color: rgb(60, 241, 81);")
    all.setObjectName("all")
    p2012 = QtWidgets.QPushButton(f10)
    p2012.setGeometry(QtCore.QRect(130, 170, 75, 23))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    p2012.setFont(font)
    p2012.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    p2012.setStyleSheet("background-color: rgb(60, 241, 81);")
    p2012.setObjectName("p2012")
    t2013 = QtWidgets.QPushButton(f10)
    t2013.setGeometry(QtCore.QRect(30, 340, 75, 23))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    t2013.setFont(font)
    t2013.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    t2013.setStyleSheet("background-color: rgb(60, 241, 81);")
    t2013.setObjectName("t2013")
    t2014 = QtWidgets.QPushButton(f10)
    t2014.setGeometry(QtCore.QRect(140, 340, 75, 23))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    t2014.setFont(font)
    t2014.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    t2014.setStyleSheet("background-color: rgb(60, 241, 81);")
    t2014.setObjectName("t2014")
    t2015 = QtWidgets.QPushButton(f10)
    t2015.setGeometry(QtCore.QRect(30, 380, 75, 23))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    t2015.setFont(font)
    t2015.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    t2015.setStyleSheet("background-color: rgb(60, 241, 81);")
    t2015.setObjectName("t2015")
    t2016 = QtWidgets.QPushButton(f10)
    t2016.setGeometry(QtCore.QRect(140, 380, 75, 23))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    t2016.setFont(font)
    t2016.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    t2016.setStyleSheet("background-color: rgb(60, 241, 81);")
    t2016.setObjectName("t2016")
    label_4 = QtWidgets.QLabel(f10)
    label_4.setGeometry(QtCore.QRect(40, 100, 581, 16))
    font = QtGui.QFont()
    font.setPointSize(10)
    label_4.setFont(font)
    label_4.setObjectName("label_4")
    label_5 = QtWidgets.QLabel(f10)
    label_5.setGeometry(QtCore.QRect(30, 300, 261, 16))
    label_5.setObjectName("label_5")
    label_6 = QtWidgets.QLabel(f10)
    label_6.setGeometry(QtCore.QRect(250, 20, 351, 41))
    font = QtGui.QFont()
    font.setFamily("Rockwell Condensed")
    font.setPointSize(24)
    font.setBold(True)
    font.setItalic(True)
    font.setWeight(75)
    label_6.setFont(font)
    label_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 203, 70, 255), stop:1 rgba(255, 255, 255, 255));")
    label_6.setObjectName("label_6")

    back.setText("Back")
    label_2.setText("Persons Arrested in Cyber Crimes")
    label_3.setText("Types of Cyber Attacks")
    p2008.setText("2008")
    p2009.setText("2009")
    p2010.setText("2010")
    p2011.setText("2011")
    p2013.setText("2013")
    all.setText("All years")
    p2012.setText("2012")
    t2013.setText("2013")
    t2014.setText("2014")
    t2015.setText("2015")
    t2016.setText("2016")
    label_4.setText("Click the button of corresponding year to get graph")
    label_5.setText("Click the button of corresponding year to get graph")
    label_6.setText("      Statistics")

    f10.show()
    back.show()
    label_2.show()
    label_3.show()
    p2008.show()
    p2009.show()
    p2010.show()
    p2011.show()
    p2013.show()
    all.show()
    p2012.show()
    t2013.show()
    t2014.show()
    t2015.show()
    t2016.show()
    label_4.show()
    label_5.show()
    label_6.show()

    def back1():
        f10.hide()
        back.hide()
        label_2.hide()
        label_3.hide()
        p2008.hide()
        p2009.hide()
        p2010.hide()
        p2011.hide()
        p2013.hide()
        all.hide()
        p2012.hide()
        t2013.hide()
        t2014.hide()
        t2015.hide()
        t2016.hide()
        label_4.hide()
        label_5.hide()
        label_6.hide()
        main.mainui(abc)

    back.clicked.connect(back1)
    
    def p2800():
        import matplotlib.pyplot as plt
        plt.rcdefaults()
        import matplotlib.pyplot as plt
        import csv
        import numpy as np

        y = []
        x = []

        with open('1person_arrested_2008.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in plots:
                x.append(row[0])
                a=float(row[1])
                y.append(a)
             
        y_pos=np.arange(len(x))

        plt.barh(y_pos, y, align='center', alpha=0.5,color='purple')
        plt.yticks(y_pos, x)
        plt.xlabel('Number of person arrested')
        plt.title('Person arrested in 2008(age-wise)')
        plt.show()
        
    p2008.clicked.connect(p2800)
    
    def p2900():
        import matplotlib.pyplot as plt
        plt.rcdefaults()
        import matplotlib.pyplot as plt
        import csv
        import numpy as np

        y = []
        x = []

        with open('1person_arrested_2009.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in plots:
                x.append(row[0])
                a=float(row[1])
                y.append(a)
             
        y_pos=np.arange(len(x))

        plt.barh(y_pos, y, align='center', alpha=0.5,color='purple')
        plt.yticks(y_pos, x)
        plt.xlabel('Number of person arrested')
        plt.title('Person arrested in 2009(age-wise)')
        plt.show()
    
    p2009.clicked.connect(p2900)

    def p2100():
        import matplotlib.pyplot as plt
        plt.rcdefaults()
        import matplotlib.pyplot as plt
        import csv
        import numpy as np

        y = []
        x = []

        with open('1person_arrested_2010.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in plots:
                x.append(row[0])
                a=float(row[1])
                y.append(a)
             
        y_pos=np.arange(len(x))

        plt.barh(y_pos, y, align='center', alpha=0.5,color='purple')
        plt.yticks(y_pos, x)
        plt.xlabel('Number of person arrested')
        plt.title('Person arrested in 2010(age-wise)')
        plt.show()
        
    p2010.clicked.connect(p2100)
    
    def p2110():
        import matplotlib.pyplot as plt
        plt.rcdefaults()
        import matplotlib.pyplot as plt
        import csv
        import numpy as np

        y = []
        x = []

        with open('1person_arrested_2011.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in plots:
                x.append(row[0])
                a=float(row[1])
                y.append(a)
             
        y_pos=np.arange(len(x))

        plt.barh(y_pos, y, align='center', alpha=0.5,color='purple')
        plt.yticks(y_pos, x)
        plt.xlabel('Number of person arrested')
        plt.title('Person arrested in 2011(age-wise)')
        plt.show()
        
    p2011.clicked.connect(p2110)
    
    def p2120():
        import matplotlib.pyplot as plt
        plt.rcdefaults()
        import matplotlib.pyplot as plt
        import csv
        import numpy as np

        y = []
        x = []

        with open('1person_arrested_2012.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in plots:
                x.append(row[0])
                a=float(row[1])
                y.append(a)
             
        y_pos=np.arange(len(x))

        plt.barh(y_pos, y, align='center', alpha=0.5,color='purple')
        plt.yticks(y_pos, x)
        plt.xlabel('Number of person arrested')
        plt.title('Person arrested in 2012(age-wise)')
        plt.show()
        
    p2012.clicked.connect(p2120)
    
    def p2130():
        import matplotlib.pyplot as plt
        plt.rcdefaults()
        import matplotlib.pyplot as plt
        import csv
        import numpy as np

        y = []
        x = []

        with open('1person_arrested_2013.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in plots:
                x.append(row[0])
                a=float(row[1])
                y.append(a)
             
        y_pos=np.arange(len(x))

        plt.barh(y_pos, y, align='center', alpha=0.5,color='purple')
        plt.yticks(y_pos, x)
        plt.xlabel('Number of person arrested')
        plt.title('Person arrested in 2013(age-wise)')
        plt.show()
                  
    p2013.clicked.connect(p2130)
    
    def al():
        import matplotlib.pyplot as plt
        plt.rcdefaults()
        import matplotlib.pyplot as plt
        import csv
        import numpy as np

        y = []
        x = []

        with open('total.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in plots:
                x.append(row[0])
                a=float(row[1])
                y.append(a)
             
        y_pos=np.arange(len(x))

        plt.barh(y_pos, y, align='center', alpha=0.5,color='purple')
        plt.yticks(y_pos, x)
        plt.xlabel('Number of person arrested')
        plt.title('Person arrested in period 2008-2013')
        plt.show()
        
    all.clicked.connect(al)
    
    def c2130():
        import matplotlib.pyplot as plt
        plt.rcdefaults()
        import matplotlib.pyplot as plt
        import csv
        import numpy as np

        y = []
        x = []

        with open('2013_attacks.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in plots:
                x.append(row[0])
                a=float(row[1])
                y.append(a)
             
        y_pos=np.arange(len(x))

        plt.barh(y_pos, y, align='center', alpha=0.5)
        plt.yticks(y_pos, x)
        plt.xlabel('Number of attacks(in %)')
        plt.title('Top 10 attacks techniques in 2013')
        plt.show()

    t2013.clicked.connect(c2130)
    
    def c2140():
        import matplotlib.pyplot as plt
        plt.rcdefaults()
        import matplotlib.pyplot as plt
        import csv
        import numpy as np

        y = []
        x = []

        with open('2014_attacks.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in plots:
                x.append(row[0])
                a=float(row[1])
                y.append(a)
             
        y_pos=np.arange(len(x))

        plt.barh(y_pos, y, align='center', alpha=0.5)
        plt.yticks(y_pos, x)
        plt.xlabel('Number of attacks(in %)')
        plt.title('Top 10 attacks techniques in 2014')
        plt.show()
        
    t2014.clicked.connect(c2140)
    
    def c2150():
        import matplotlib.pyplot as plt
        plt.rcdefaults()
        import matplotlib.pyplot as plt
        import csv
        import numpy as np

        y = []
        x = []

        with open('2015_attacks.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in plots:
                x.append(row[0])
                a=float(row[1])
                y.append(a)
             
        y_pos=np.arange(len(x))

        plt.barh(y_pos, y, align='center', alpha=0.5)
        plt.yticks(y_pos, x)
        plt.xlabel('Number of attacks(in %)')
        plt.title('Top 10 attacks techniques in 2015')
        plt.show()
        
    t2015.clicked.connect(c2150)
    
    def c2160():
        import matplotlib.pyplot as plt
        plt.rcdefaults()
        import matplotlib.pyplot as plt
        import csv
        import numpy as np

        y = []
        x = []

        with open('2016_attacks.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in plots:
                x.append(row[0])
                a=float(row[1])
                y.append(a)
             
        y_pos=np.arange(len(x))

        plt.barh(y_pos, y, align='center', alpha=0.5)
        plt.yticks(y_pos, x)
        plt.xlabel('Number of attacks(in %)')
        plt.title('Top 10 attacks techniques in 2016')
        plt.show()
        
    t2016.clicked.connect(c2160)