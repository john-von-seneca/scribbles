
import sys
import math

def get_strings():
	s1 = sys.argv[1] if len(sys.argv) > 1 else input('str1: ')
	s2 = sys.argv[2] if len(sys.argv) > 2 else input('str2: ')
	return (s1, s2)


def normalize(s1, s2):
	n1, n2 = len(s1), len(s2)
	if n1>n2:
		s2 = '0'*(n1-n2)+s2
	elif n1<n2:
		s1 = '0'*(n2-n1)+s1
	n = max(n1, n2)
	sz_group = 3
	num_groups = n//sz_group + 1
	s1 = '0'*(sz_group*num_groups-n) + s1
	s2 = '0'*(sz_group*num_groups-n) + s2
	return (s1, s2, n, sz_group, num_groups)

def multiply(i1, s2, s, num_groups):
	carryforward=0
	s_out_1 = ''
	for ix in range(num_groups):
		ix1, ix2 = -(ix+1)*s, -ix*s-1
		i2 = int(s2[ix1:ix2]+s2[ix2])

		result_tmp = i1 * i2 + carryforward

		# prepend last "s" digits
		s_out_1 = str(result_tmp % (10**s)) + s_out_1
		# carryforward whatever remains 
		carryforward = result_tmp//(10**s)

		# print('i1', i1, 'i2', i2, 'product', i1*i2, result_tmp,
		# 	  'stub', str(result_tmp % (10**s)),
		# 	  'sout', s_out_1, 'carryforward', carryforward)

	#print(s_out_1, i1*int(s2), int(s_out_1)==i1*int(s2))
	return s_out_1

def add(str1, str2):
	if len(str1) < len(str2):
		str1, str2 = str2, str1
	str2 = '0'*(len(str1)-len(str2)) + str2
	str_out = ''
	carryforward = 0
	s = 1
	for ix in range(len(str2)):
		ix1 = -ix-1
		result_tmp = int(str1[ix1]) + int(str2[ix1]) + carryforward
		str_out = str(result_tmp % (10**s)) + str_out
		carryforward = result_tmp//(10**s)
	str_out = str(carryforward) + str_out
	# print('add', str1, str2, str_out, (int(str1)+int(str2))==int(str_out))
	return str_out


s1, s2 = get_strings()
s1, s2, n, sz_group, num_groups = normalize(s1, s2)
s_out = '0' * (n*2)
num_groups_s = (n*2)//sz_group+1

s=sz_group
for ix1 in range(num_groups):
	ix11, ix12 = -(ix1+1)*s, -ix1*s-1
	i1 = int(s1[ix11:ix12]+s1[ix12])
	#print(ix11, ix12, i1)

	s_out_1 = multiply(i1, s2, s, num_groups)
	s_out_1 = s_out_1 + '0'*(ix1*s)
	s_out = add(s_out, s_out_1)

print(s_out, int(s1)*int(s2), int(s1)*int(s2)==int(s_out))
