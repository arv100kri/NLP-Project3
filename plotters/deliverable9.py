'''
Created on Mar 4, 2013

@author: koolkid
'''

import math
import matplotlib.pyplot as plt

X_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Got the values by manually reading the output from the scorer script
Y_values1 = [68.05, 74.61, 77.65, 79.70, 81.38, 82.88, 83.90, 84.76, 85.57, 85.98]    #Develop1
Y_values2 = [69.91, 71.76, 72.19, 74.15, 75.06, 75.21, 73.30, 75.32, 75.21, 75.23]    #Develop1
#plt.xscale(0.1)
plt.xlabel('Number of iterations')
plt.ylabel("Accuracy")
plt.xlim(0,11)
plt.ylim(0,100)
plt.plot(X_values, Y_values1, color = 'r', marker = 'o', label='Training (after Deliverable 9)')
plt.plot(X_values, Y_values2, color = 'g', marker = 'o', label='Development (after Deliverable 9)')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
       ncol=2, mode="expand", borderaxespad=0.)
plt.show()