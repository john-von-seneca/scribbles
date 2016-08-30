# basic neural net

import numpy as np
import math

# data point
x, y = 2, 1

w = []
w.append(np.matrix(((0.1, 0.2), (0.3, 0.4))))
w.append(np.matrix(((0.2),      (1),      (-3))).transpose())
w.append(np.matrix(((1),        (2))).transpose())
print(w)

# forward propagation
def forward(w, x):
	x_current = np.matrix([x]) # need to do vert concat
	x_all, s_all = [], []
	for ww in w:
		xx = np.hstack((np.matrix([1]), x_current)).transpose()
		x_all.append(xx)
		# print('')
		# print(ww)
		# print(xx)
		ss = ww.transpose() * xx
		s_all.append(ss)
		# print(ss)
		x_current = np.matrix([math.tanh(ss) for ss in ss])

	x_all.append(np.matrix(math.tanh(ss)))
	return (x_all, s_all)


def comp_mul(x, y):
	rows, cols = x.shape
	z = np.zeros(x.shape)
	for row in range(rows):
		for col in range(cols):
			z[row][col] = x[row][col] * y[row][col]
	return z
	
def backward(y, w, x_all, s_all):
	L = len(w)
	delta = [0] * (L+1)
	x_L = x_all[L][0]
	theta_dx = 1 - x_L**2
	delta[L] = 2 * (x_L - y) * theta_dx
	# print(delta[L])
	for l in range(L-1, 0, -1):
		# print('')
		d_l = w[l].shape[1]
		# print('l: {0} :: d_l: {1}'.format(l, d_l))
		ones = np.matrix(np.ones((d_l, 1)))
		x_l_sqrd = comp_mul(x_all[l], x_all[l])
		theta_dx = ones - x_l_sqrd[1:]
		# print(theta_dx)
		delta[l] = comp_mul(theta_dx, ( w[l] * delta[l+1] )[1:])
		# print(delta[l])

	return(delta)

	

x_all, s_all = forward(w, x)
print('s: ')
print(s_all)
delta = backward(y, w, x_all, s_all)
print('delta: ')
print(delta)
