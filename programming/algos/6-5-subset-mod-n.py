
import random
import sys

n = 10
n = int(sys.argv[1]) if len(sys.argv)>1 else n

a = [random.randint(1,n**3) for _ in range(n)]
print(a)

subsets=[[] for _ in range(n)]

for aa in a:
	subsets_aa = [[] for _ in range(n)]
	subsets_aa[aa % n].append([aa])
	for mod_val, ix_subsets in enumerate(subsets):
		if len(ix_subsets)==0:
			continue
		for ixix_subset in ix_subsets:
			mod_val_new = (mod_val + aa) % n
			subsets_aa[mod_val_new].append(ixix_subset + [aa])
	print(aa, len(subsets_aa[0]), subsets_aa[0])
	subsets = [subsets[ix]+subsets_aa[ix] for ix in range(n)]

#print(subsets[0])
