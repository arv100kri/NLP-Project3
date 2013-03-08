'''
Created on Mar 4, 2013

@author: koolkid
'''

import math
import matplotlib.pyplot as plt

X_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Got the values by manually reading the output from the scorer script
Y_values1 = [81.57, 90.94, 93.94, 95.58, 96.71, 97.42, 97.79, 98.07, 98.46, 98.53]    #Develop1
Y_values2 = [85.27, 87.36, 88.16, 88.52, 88.95, 88.76, 88.89, 89.28, 89.32, 89.39]    #Develop1
#plt.xscale(0.1)
plt.xlabel('Number of iterations')
plt.ylabel("Accuracy")
plt.xlim(0,11)
plt.ylim(0,100)
plt.plot(X_values, Y_values1, color = 'r', marker = 'o', label='Training (after Deliverable 11)')
plt.plot(X_values, Y_values2, color = 'g', marker = 'o', label='Development (after Deliverable 11)')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
       ncol=2, mode="expand", borderaxespad=0.)
plt.show()