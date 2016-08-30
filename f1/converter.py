import os
from subprocess import call

for root, dirs, files in os.walk(".", topdown=False):
	for name in files:
		if(name[-6:] == '.ipynb'):
			# print(name)
			# print(root)
			# print(os.path.join(root, name))
			call(["sh", "converter.sh", root, name[:-6]])
	for name in dirs:
		pass
		#print(os.path.join(root, name))
