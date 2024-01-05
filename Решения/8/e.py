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

def remove(table, key):
	ha = hasher(key)
	for i in range(len(table[ha % 10])):
		if table[ha % 10][i][1] == key:
			return table[ha % 10].pop(i)[2]
	else:
		return 'KeyError'