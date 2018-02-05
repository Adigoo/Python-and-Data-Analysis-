# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 19:07:57 2017

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:47:51 2017

@author: aditya
"""

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