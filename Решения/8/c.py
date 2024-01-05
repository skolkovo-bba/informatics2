from pprint import pprint

a, q = 91, 100

buf_len = 10

num = lambda x: ord(x)

def binpow(a, n):
	global buf_len
	res = None

	if not hasattr(binpow, "buf"):
		binpow.buf = [0] * buf_len
		binpow.buf_ans = [0] * buf_len
		binpow.count = 0
	
	if (a, n) in binpow.buf:
		res = binpow.buf_ans[binpow.buf.index((a, n))]
	elif (a, n + 1) in binpow.buf:
		res = binpow.buf_ans[binpow.buf.index((a, n + 1))] / a
	elif (a, n - 1) in binpow.buf:
		res = binpow.buf_ans[binpow.buf.index((a, n - 1))] * a
	else:
		res = 1
		while n:
			if n & 1:
				res *= a
			a *= a
			n >>= 1
	
	binpow.buf[binpow.count % buf_len] = (a, n)
	binpow.buf_ans[binpow.count % buf_len] = res
	binpow.count += 1
	
	return res

def hasher(s):
    global a, q
    m = len(s)
    h = 0
    for i in range(m):
        h += a ** (m - (i + 1)) * num(s[i])
    
    return int(h % q)


hash_table = [[] for _ in range(10)]

for _ in range(int(input())):
	key, value = input().split()
	m = [hasher(key), key, value]
	for i in range(len(hash_table[m[0] % 10])):
		if hash_table[m[0] % 10][i][1] == key:
			hash_table[m[0] % 10][i][2] = value
			break
	else:
	    hash_table[m[0] % 10].append(m)

for i in range(10):
	if len(hash_table[i]) == 0:
		continue
	print(i)
	for line in hash_table[i]:
		print(*line)