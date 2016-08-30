
#
import math
import numpy as np
import matplotlib.pyplot as plt
from lfd_utils import *

a, b = np.matrix((1, -2)), 3
x = range(10)
y = find_y(a, b, x)
n_random = 20
pts_random = generate_random_points(n_random, x, y)
ixs_pos, ixs_neg = partition_points_line(a, b, pts_random)

# which ones to flip?
ixs_flip = np.random.random_integers(0, n_random-1, math.ceil(n_random/10))
aa = np.ones(n_random, dtype = bool)
aa[ixs_neg] = [False] * ixs_neg.shape[1]
aa[ixs_flip] = ~aa[ixs_flip]
ixs_pos, ixs_neg = np.where(aa)[0], np.where(~aa)[0]

# plt.scatter(pts_random[0, ixs_pos], pts_random[1, ixs_pos], c=['0'] * ixs_pos.shape[0])
# plt.scatter(pts_random[0, ixs_neg], pts_random[1, ixs_neg], c=['1'] * ixs_neg.shape[0])

min_p, max_p = min_max(pts_random)
x = range(min_p-1, max_p+1)
# plt.plot(x, find_y(a, b, x))

T = 100
w = np.matrix((1, 1, -11))
# signs_pts = np.sign(vals_pts)
w, errors, errors_best = perceptron_m(pts_random, aa, w, T)
# plt.plot(x, find_y(w[0, 1:], w[0,0], x), color='m')
plt.plot(errors, color='b')
plt.plot(errors_best, color='r')
plt.show()



