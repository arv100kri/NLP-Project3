'''
Created on Feb 14, 2013

@author: koolkid
'''
import matplotlib.pyplot as plt
import subprocess
import sys

X_values = [7,8,9,10,11 ]
Y_values1 = [801, 814, 44539, 88473, 273415]
plt.xlabel("Deliverable")
plt.ylabel("Number of Features")
plt.xlim(6, 12)
plt.plot(X_values, Y_values1, color = 'g', marker = 'o')

plt.show()
