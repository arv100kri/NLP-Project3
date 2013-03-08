'''
Created on Mar 4, 2013

@author: koolkid
'''

import math
import matplotlib.pyplot as plt

X_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Got the values by manually reading the output from the scorer script
Y_values1 = [68.49, 78.02, 82.56, 85.64, 87.34, 89.21, 90.29, 91.00, 91.65, 92.29]    #Develop1
Y_values2 = [70.69, 73.87, 74.52, 75.06, 75.68, 76.11, 76.24, 76.65, 76.68, 76.78]    #Develop1
#plt.xscale(0.1)
plt.xlabel('Number of iterations')
plt.ylabel("Accuracy")
plt.xlim(0,11)
plt.ylim(0,100)
plt.plot(X_values, Y_values1, color = 'r', marker = 'o', label='Training (after Deliverable 10)')
plt.plot(X_values, Y_values2, color = 'g', marker = 'o', label='Development (after Deliverable 10)')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
       ncol=2, mode="expand", borderaxespad=0.)
plt.show()