import json
import sys
import difflib

def load_json(filename):
	return json.loads(open(filename).read()) 

# from http://stackoverflow.com/a/845432/5510350
def unidiff_output(expected, actual):
	"""
	Helper function. Returns a string containing the unified diff of two multiline strings.
	"""

	#expected=expected.splitlines(1)
	#actual=actual.splitlines(1)

	diff=difflib.unified_diff(expected, actual)
	return ''.join(diff)


json_bp  = load_json('boilerplate.ipynb')
json_new = load_json(sys.argv[1])

for ix in range(7):
	a = unidiff_output(json_bp['cells'][ix]['source'], json_new['cells'][ix]['source'])
	if len(a)!=0:
		print('{2}cell {0}\n{1}\n{2}'.format(ix+1,a,'='*20+'\n'))


