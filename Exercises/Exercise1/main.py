import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

print("Hello World!")

a = np.array([1,2,3,4,5,6,7,8,9])
b = a.reshape([3,3])

print(a)
print(b)

x = np.linspace(0,10,20)
y = x**2

plt.plot(x,y)
plt.title("plot 1D")
plt.xlabel("X label")
plt.ylabel("y label")
plt.show()
print("plotted")