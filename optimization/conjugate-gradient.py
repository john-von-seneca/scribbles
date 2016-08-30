import numpy as np
import scipy as sp

from matplotlib import pyplot as plt
from matplotlib import cm as mp_cm
from mpl_toolkits.mplot3d import Axes3D

A = np.array([[3,2],[2,6]])
b = np.array([[2],[-8]]).reshape(-1,1)
c = 0
print('shapes: A,b,c ::', A.shape, b.shape)

x_star = np.linalg.inv(A) @ b
print(x_star)

num_pts = 2e2
x,y = np.meshgrid(np.linspace(-6,4,num_pts), np.linspace(-4,6,num_pts))
X = np.vstack([x.ravel(), y.ravel()])

z = X * (A @ X) - b.T @ X - c
z = np.sum(z, axis=0).reshape((x.shape[0],y.shape[0]))
print('shapes: x,y,X,z ::', x.shape, y.shape, X.shape, z.shape)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, z, linewidth=0, cmap=mp_cm.coolwarm)
fig.colorbar(surf)

plt.show()
