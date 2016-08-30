
# to show the fraction of volume of a sphere concentrated
# in the periphery

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('text', usetex = True)

n_e = 100
dims = [1,2,5,20]
for d in dims:
	e = np.linspace(0,1,n_e)
	y = [1 - (1 - ee)**d for ee in e]
	plt.plot(e, y, label = 'line 1')


plt.legend(['D = {d}'.format(d=d) for d in dims], loc='center right')
plt.xlabel('\epsilon', fontsize=24)
plt.ylabel('fraction of volume', fontsize=16)
plt.show()
