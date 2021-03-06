# 4.11 3D plot

# import necessary libraries
import matplotlib.pyplot as pl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = pl.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)

#Z = np.sin( np.sqrt(X ** 2 + Y ** 2))

Z = np.sin(X ** 2 + Y ** 2)+np.cos(X ** 2 + Y ** 2)



ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=pl.cm.hot)
#ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=pl.cm.hot)
ax.set_zlim(-2, 2)

pl.show()