from matplotlib import pyplot as plt
import pylab
from pylab import *
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
fig.canvas.set_window_title('timxag')

v = numpy.array([[-5, 0, 0], [0, -5, 0], [-2, 0, 0.3], \
              [0, -2, 0.3], [5, 0, 0], [0, 5, 0], \
              [0, 2, 0.3], [2, 0, 0.3]])

ax.scatter(v[:,0], v[:, 1], v[:, 2])

verts = [[v[0], v[5], v[6], v[2]] , [v[4], v[5], v[6], v[7]],\
        [v[0], v[1], v[3], v[2]] , [v[1], v[4], v[7], v[3]]]

ax.add_collection(Poly3DCollection(verts, \
    facecolors='grey', linewidths=1, edgecolors='black', alpha=.25))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.axis('scaled')
plt.show()
