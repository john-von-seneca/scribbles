import numpy as np
import matplotlib.pyplot as plt
import math

def distance_pts(pt1, pt2):
	return np.sqrt(np.sum(np.square(pt1 - pt2)))

def distance_pt_line(pt1, pt2, pt0):
	num_1 = np.sum(np.square(pt1-pt0)) * np.sum(np.square(pt2-pt1))
	num_2 = (np.sum((pt1-pt0)*(pt2-pt1)))**2
	den_1 = np.sum(np.square(pt2-pt1))
	return math.sqrt((num_1 - num_2)/den_1)

def compute_cost(points, memo, j, k, verbose=False, force=False):
	if(not(force) and not(np.isnan(memo[j,k]))):
		return memo[j, k]
	if verbose:
		print("compute cost {0},{1}".format(j,k))
	
	p_start = points[j, :]
	p_end = points[k, :]
	memo[j, k] = 2*distance_pts(points[j, :], points[k, :])
	for i in range(j+1, k):
		memo[j, k] += distance_pt_line(p_start, p_end, points[i,:])

	return memo[j, k]

def flatten(list1):
	return [item for sublist in list1 for item in sublist]

def compute_best(points, memo_cost, memo_splits, j, k, verbose=False):
	if verbose:
		print('compute_best: {0},{1}'.format(j, k))
	if(not(np.isnan(memo_cost[j, k])) and (memo_splits[j][k] is not None)):
		return (memo_cost[j, k], memo_splits[j][k])
	
	min_cost = compute_cost(points, memo_cost, j, k, verbose)	 
	best_splits = [j,k]

	if((k-j)==1):
		if verbose:
			print('k-j==1')
		memo_cost[j,k] = min_cost
		memo_splits[j][k] = best_splits
		return (memo_cost[j,k], memo_splits[j][k])
	if(k==j):
		if verbose:
			print('k==j')
		return (0, [])
	if(k<j):
		1/0
	
	for i in range(j+1,k):
		if verbose:
			print('compute-best::split::{0}'.format(i))
		val1, splits1 = compute_best(points, memo_cost, memo_splits, j, i, verbose)
		if val1 > min_cost:
			continue
		val2, splits2 = compute_best(points, memo_cost, memo_splits, i, k, verbose)
		current_cost = val1 + val2
		if(current_cost < min_cost):
			min_cost = current_cost
			best_splits = flatten([splits1, splits2[1:]])
	memo_cost[j,k] = min_cost
	memo_splits[j][k] = best_splits

	return (memo_cost[j,k], memo_splits[j][k])

lines = open("points_file3.txt").readlines()
points = np.array([list(map(float, line[:-1].split()[1:])) for line in lines])
print(points.shape)
n = points.shape[0]

memo_cost = np.full((n,n), np.nan)
print(np.isnan(memo_cost[1,3]))
memo_splits = [[None for ix in range(n)] for jx in range(n)]
print(compute_best(points, memo_cost, memo_splits, 0, n-1, verbose=False))
