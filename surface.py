import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

def z_func(x,y):                                            # function of 2 variables
    return ((x**2*y)/(x**4+y**2))

x = np.arange(-1.0,1.0,0.1)                                 # populates x and y values with intervals of 0.1
y = np.arange(-1.0,1.0,0.1)                                 # part of numpy, returns an ndarray
X,Y = np.meshgrid(x, y)                                     # grid of each point on the ndarray
Z = z_func(X, Y)                                            # evaulate the function with the grids as input

fig = plt.figure()                                          # container object for all plot elements
#ax = fig.gca(projection='3d')                              # get current axis
ax = fig.add_subplot(111, projection="3d")
cset = ax.contour(X, Y, Z, 10, lw=1, colors="w", 
        linestyles="solid")    # can only contour
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,       # or surface
        cmap=plt.cm.RdBu, lw=5)
#cset = ax.contour(X, Y, Z, zdir='z', offset=-0.5, cmap=plt.cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-1.2, cmap=plt.cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=1, cmap=plt.cm.coolwarm)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
