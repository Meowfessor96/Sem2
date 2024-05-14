import numpy as np
import matplotlib.pyplot as plt

x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
y= np.loadtxt('y_n_output.txt',dtype='double')

plt.subplot(2, 1, 1)
plt.stem(range(0,6),x)
plt.ylabel('$x(n)$')
plt.grid()
plt.savefig("x(n)_vs_n.png")

plt.clf()

plt.subplot(2, 1, 2)
plt.stem(range(0,20),y) #There are 20 values of y in text file
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()

plt.savefig("y(n)_vs_n.png")
