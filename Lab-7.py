import numpy
import matplotlib.pyplot as plt

x = numpy.linspace(0,5,20)
y = numpy.cos(x**2)/x
plt.plot(x, y, "ro-")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

plt.savefig("1.png", dpi=200)