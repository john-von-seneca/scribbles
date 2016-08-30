import math
import numpy as np
from matplotlib import pyplot as plt

from scipy import optimize as sp_optimize
from scipy.spatial.distance import pdist as sp_pdist
from scipy.spatial.distance import squareform as sp_squareform

# from ipywidgets import interact, interactive, fixed
# import ipywidgets as widgets


def plot_sin():
	thetas = np.linspace(0,2*math.pi,100)
	plt.plot(thetas, np.sin(thetas), 'g')

def draw_samples(in_pts, betai=1.0, uniform=False):
	if uniform:
		x = np.linspace(0,2*math.pi, in_pts).reshape(-1,1)
	else:
		x = np.random.rand(in_pts).reshape(-1,1)*2*math.pi
	if betai==0.0:
		y_noise = np.zeros_like(x)
	else:
		y_noise = np.random.normal(0, betai, size=(in_pts,1))
	y = np.sin(x) + y_noise
	return (x, y)

def f(x, *args):
	if len(x)==1:
		gamma, sigma = x[0]
	else:
		gamma, sigma = x
	A, B, t, N = args
	C = (gamma**2) * (A**(1./(sigma**2))) + np.eye(N)*1e-2
	#eigen_vals = np.linalg.eigvals(C)
	Ci = np.linalg.inv(C)
	Cd = np.linalg.det(C)
	if Cd < 1e-200:
		minC, maxC = np.min(C.ravel()), np.max(C.ravel())
		print('det is two low: ', Cd, ' [',minC,',',maxC,']')
	term1 = -0.5 * math.log(Cd)
	term2 = -0.5 * t.T @ Ci @ t 
	term3 = -N/2. * math.log(2*math.pi)
	return -(term1 + term2 + term3)

def find_sigma_min(x, t, N):
	B = np.square(x - x.T)
	A = np.exp( - B/2.)
	res1 = sp_optimize.fmin_cg(f, (1.0,1.0), args=(A, B, t, N))
	#print('sigma optimal = ', res1[0])
	return abs(res1[0]), abs(res1[1])

def my_cholesky(cn):
	u, s, v = np.linalg.svd(cn)
	#print(s.shape)
	if isinstance(s[0], complex):
		print('complex machie')
	else:
		print('not complex')
	if(np.all(s > 0)):
		print('positive definite')
	else:
		print('not positive definite')
	L = u @ np.diag(np.sqrt(s))
	return L

def kernel_1(x1, y1, gamma, sigma):
	exponent = -np.square(x1-y1)/(2.0*sigma**2)
	return (gamma**2) * np.exp(exponent)

def get_gp_covar(xgt, tgt, betai, gamma, sigma):
	n = xgt.shape[0]
	pairwise_dists = sp_squareform(sp_pdist(xgt, 'euclidean'))
	K = (gamma**2) * np.exp(-pairwise_dists ** 2 / sigma ** 2) + 1e-6*np.eye(n)
	return K

def get_predictions(xt, tt, cni, betai, gamma, sigma, x):
	n = cni.shape[0]
	k = np.array([kernel_1(xt[ix], x, gamma, sigma) for ix in range(n)])
	k = k.reshape(-1,1)
	mean1 = k.T @ cni @ tt
	c = kernel_1(x, x, gamma, sigma) + betai
	covar1 = c - k.T @ cni @ k
	return [mean1, covar1]

def get_predictions2(xt, tt, cni, betai, x, gamma, sigma):
	n = cni.shape[0]
	k_star = kernel_1(xt, x.T, gamma, sigma)
	#k = np.array([kernel_1(xt[ix], x, sigma) for ix in range(n)])
	#k = k.reshape(-1,1)
	mean1 = k_star.T @ cni @ tt
	c = get_gp_covar(x, None, None, gamma, sigma) + betai
	covar1 = c - k_star.T @ cni @ k_star
	return [mean1, covar1]

def plot_samples_posterior(xgt, tgt,
						   betai, x_test, gamma, sigma,
						   plot_posteriors, plot_mean):
	#arr_mean, arr_covar = get_predictions2(xgt, tgt, cni, betai, x_test, sigma)
	cn = get_gp_covar(xgt, tgt, betai, gamma, sigma)
	cni = np.linalg.inv(cn)
	result = np.array([get_predictions(xgt, tgt, cni, betai, gamma, sigma, xx) for xx in x_test]).reshape(-1,2)
	arr_mean, arr_covar = result[:,0], result[:,1]
	if not(plot_posteriors):
		return
	
	n_curves, n = 10, x_test.shape[0]
	arr_mean = np.array(arr_mean)
	# tmp = np.random.multivariate_normal(arr_mean.ravel(),
	# 									 cov=arr_covar,
	# 									size=(10)).T
	# L = my_cholesky(arr_covar)
	# f_posterior = np.dot(L, np.random.normal(size=(n,n_curves)))
	# plt.plot(x_test, f_posterior)
	plt.plot(x_test, arr_mean, linewidth=2, label='my:'+str(sigma))


in_pts = 100
betai=1e-1
test_max= 2*math.pi
uniform=False
plot_posteriors=True
plot_mean=True

xgt, tgt = draw_samples(in_pts, betai, uniform)
np.save('xgt-uniform.npy', xgt)
np.save('tgt-uniform.npy', tgt)
# str_uniform = 'nonuniform'
# xgt, tgt = np.load('xgt-'+str_uniform+'.npy'), np.load('tgt-'+str_uniform+'.npy')
plt.plot(xgt, tgt, '.b')
x_test = np.linspace(0,test_max,100).reshape(-1,1)

gamma, sigma = find_sigma_min(xgt, tgt, in_pts) 
print('sigma-min: ', sigma, ' ', type(sigma))
print('gamma-min: ', gamma, ' ', type(gamma))

plot_samples_posterior(xgt, tgt, betai, x_test, gamma, sigma,          plot_posteriors, plot_mean)
plot_samples_posterior(xgt, tgt, betai, x_test, gamma, math.sqrt(1.0), plot_posteriors, plot_mean)
plot_samples_posterior(xgt, tgt, betai, x_test, gamma, math.sqrt(0.5), plot_posteriors, plot_mean)
plot_samples_posterior(xgt, tgt, betai, x_test, gamma, math.sqrt(0.25), plot_posteriors, plot_mean)
plot_samples_posterior(xgt, tgt, betai, x_test, gamma, math.sqrt(0.1), plot_posteriors, plot_mean)
plot_samples_posterior(xgt, tgt, betai, x_test, gamma, math.sqrt(0.01), plot_posteriors, plot_mean)


# from sklearn import gaussian_process
# gp = gaussian_process.GaussianProcess(theta0=1e-2, thetaL=1e-4, thetaU=1e-1)
# print(gp.get_params())
# gp.fit(xgt, tgt)  
# y_pred, sigma2_pred = gp.predict(x_test, eval_MSE=True)
# plt.plot(x_test, y_pred, 'g', label='gp')

#plt.legend(loc='upper right')
plt.legend(loc=(1,0.5))
plt.legend(loc='lower center')

plt.show()
plt.savefig('name.png')
