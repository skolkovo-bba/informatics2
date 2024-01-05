a, q = map(int, input().split())

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

def hash_func(s):
    global a, q
    m = len(s)
    h = 0
    for i in range(m):
        h += binpow(a, m - (i + 1)) * num(s[i])
    
    return h % q

print(hash_func(input()))