from matplotlib import pyplot as plt
import numpy as np
from pyparsing import line

xr = yr = np.linspace(0, 2*np.pi, 10)
x, y = np.meshgrid(xr, yr)

fx, fy = np.sin(x), np.cos(y)

plt.figure(figsize=(8, 8))
plt.quiver(x, y, fx, fy)
# plt.show()

plt.streamplot(x, y, fx, fy, density=2, linewidth=np.sin(x)/np.cos(y))

plt.axis("scaled")
plt.show()