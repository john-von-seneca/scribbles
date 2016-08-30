# perceptron learning


import numpy as np
import matplotlib.pyplot as plt

a = np.matrix((1, -2))
b = 3

x = range(10)
# <a,pt> = b
# => a_0*x + a_1*y = b
# => y = (b - a_0*x) / a_1
y = (-b - x * a[0, 0]) * 1.0 / a[0, 1]
plt.plot(x, y, marker='o')

# generate random points
val_min = min(min(x), min(y))
val_max = max(max(x), max(y))
val = max(abs(val_min), abs(val_max))
n_random = 20
pts_random = np.random.rand(2, n_random) * (2 * val) - val
vals_pts = a * pts_random + b

ixs_pos = np.where(vals_pts >= 0)[1]
ixs_neg = np.where(vals_pts < 0)[1]

# perceptron learning algo
signs_pts = np.sign(vals_pts)
T = 20
w = np.matrix((1, 1, -11))
max_p = int(np.max(pts_random))
min_p = int(np.min(pts_random))
# add 1's as the first entry of each point
pts = np.vstack([np.ones(n_random), pts_random])

for t in range(T):
	# show the dudes
	plt.scatter(pts_random[0, ixs_pos], pts_random[1, ixs_pos], c=['0'] * ixs_pos.shape[1])
	plt.scatter(pts_random[0, ixs_neg], pts_random[1, ixs_neg], c=['1'] * ixs_neg.shape[1])

	# show w
	x = range(min_p-1, max_p+1)
	y = (-w[0,0] - x * w[0,1]) * 1.0 / w[0,2]
	plt.plot(x, y, color = str(t*1.0/T))

	# find the vals
	vals_t = w * pts
	ixs_discrepancies = np.where(signs_pts != np.sign(vals_t))[1]
	print(ixs_discrepancies)
	# if there are no discrepencies, the get the fuck lost
	if (ixs_discrepancies.shape[1] == 0):
		break
	ix_pt = ixs_discrepancies[0, 0]

	# update w
	w = w + signs_pts[0, ix_pt] * pts[:, ix_pt]

plt.plot(x, y, color='r')
plt.show()

offset = 1
# plt.axis((val_min-offset,val_max+offset,val_min-offset,val_max+offset))

# ax = plt.axes()

# ax.xaxis.set_major_locator(plt.MultipleLocator(5.0))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
# ax.yaxis.set_major_locator(plt.MultipleLocator(5.0))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(0.5))
# ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
# ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
# ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
# ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
