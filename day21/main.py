s = {}
with open('day21.txt') as f:
	c = f.read().strip().splitlines()
	for l in c:
		sp = l.split()
		if sp[0] == 'root': print(sp)
		if len(sp) == 2:
			s[sp[0][:-1]] = int(sp[1])
		else:
			s[sp[0][:-1]] = sp[1:]
computed = {}
uncomputed = {}
print(s['root'])
for ss, sss in s.items():
	if isinstance(sss, int): computed[ss] = sss
	else: uncomputed[ss] = sss

def compute(key: str) -> int:
	if key in computed: return computed[key]
	k1, op, k2 = uncomputed[key]
	if k1 not in computed:
		computed[k1] = compute(k1)
		v1 = computed[k1]
	else: v1 = computed[k1]
	if k2 not in computed:
		computed[k2] = compute(k2)
		v2 = computed[k2]
	else: v2 = computed[k2]
	if op == '*': res = v1 * v2
	elif op == '+': res = v1 + v2
	elif op == '-': res = v1 - v2
	elif op == '/': res = v1 // v2
	computed[key] = res
	return res

ans = compute('root')
print(ans)
