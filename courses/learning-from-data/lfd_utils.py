import numpy as np
import matplotlib.pyplot as plt

def fuck_you():
	print('fuck you')

def find_y(w, b, x):
	return (-b - x * w[0, 0]) * 1.0 / w[0, 1]

def eval_line(w, b, x):
	return w * x + b

def partition_points_line(w, b, x):
	vals_pts = eval_line(w, b, x)
	ixs_pos = np.where(vals_pts >= 0)[1]
	ixs_neg = np.where(vals_pts < 0)[1]
	return (ixs_pos, ixs_neg)

def min_max(pts):
	return (int(np.min(pts)), int(np.max(pts)))

def generate_random_points(n_random, x, y):
	val_min = min(min(x), min(y))
	val_max = max(max(x), max(y))
	val = max(abs(val_min), abs(val_max))
	return np.random.rand(2, n_random) * (2 * val) - val

# pts: (2, N)
# returns w_best, errors, errors_best
def perceptron_m(pts, gt, w, T):

	ixs_pos, ixs_neg = np.where(gt)[0], np.where(~gt)[0]
	in_pos, in_neg = ixs_pos.shape[0], ixs_neg.shape[0]
	in_pts = in_pos + in_neg
	min_p, max_p = min_max(pts)
	if type(gt[0]) == np.bool_:
		gt = np.ones(in_pts)
		gt[ixs_pos] = [+1] * in_pos
		gt[ixs_neg] = [-1] * in_neg

	pts = np.vstack([np.ones(in_pos+in_neg), pts])

	w_star, err_best= w, in_pos + in_neg
	errors, errors_best = [], []
	for t in range(T):
		# show the dudes
		#plt.scatter(pts[1, ixs_pos], pts[2, ixs_pos], c=['0'] * in_pos)
		#plt.scatter(pts[1, ixs_neg], pts[2, ixs_neg], c=['1'] * in_neg)

		# show w
		x = range(min_p-1, max_p+1)
		y = (-w[0,0] - x * w[0,1]) * 1.0 / w[0,2]
		#plt.plot(x, y, color = str(t*1.0/T))

		# find the vals
		vals_t = w * pts
		ixs_discrepancies = np.where(gt != np.sign(vals_t))[1]
		# print(ixs_discrepancies.shape)
		# print(ixs_discrepancies.shape[1])

		in_discrepancies = ixs_discrepancies.shape[1]
		err_current = in_discrepancies
		errors.append(err_current)
		errors_best.append(err_best)
		#print('error: {0} w_current: {1}'.format(err_current, np.str(w)))
		if err_current <= err_best:
			w_star, err_best = w, err_current
		
		# if there are no discrepencies, the get the fuck lost
		if (in_discrepancies == 0):
			break
			
		ix_pt = ixs_discrepancies[0, np.random.randint(in_discrepancies)]
		#print('ix_pt: {2} gt: {0}, pt: {1}'.format(gt[ix_pt], np.str(pts[:, ix_pt]), ix_pt))
		
		# update w
		w = w + gt[ix_pt] * pts[:, ix_pt]

	print(w_star)
	return (w_star, errors, errors_best)


