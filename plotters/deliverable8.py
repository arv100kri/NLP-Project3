'''
Created on Mar 4, 2013

@author: koolkid
'''

import math
import matplotlib.pyplot as plt

X_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Got the values by manually reading the output from the scorer script
Y_values1 = [47.74, 48.58, 50.18, 50.33, 50.39, 50.78, 50.97, 50.85, 51.11, 50.97]    #Develop1
Y_values2 = [61.62, 62.50, 63.88, 63.86, 64.63, 63.86, 64.01, 64.16, 63.86, 64.07]    #Develop1
#plt.xscale(0.1)
plt.xlabel('Number of iterations')
plt.ylabel("Accuracy")
plt.xlim(0,11)
plt.ylim(0,70)
plt.plot(X_values, Y_values1, color = 'r', marker = 'o', label='Development (before features)')
plt.plot(X_values, Y_values2, color = 'g', marker = 'o', label='Development (after Deliverable 8)')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
       ncol=2, mode="expand", borderaxespad=0.)
plt.show()