import random


buf_len = 10

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





a = 2
q = 997
num = lambda x: ord(x) - ord('A')

def hash_func(s):
    global a, q
    m = len(s)
    h = 0
    for i in range(m):
        h += binpow(a, m - (i + 1)) * num(s[i])
    
    return h % q

def hash_next(m, last_h, for_del, for_add):
    global a, q
    return (a * (last_h - binpow(a, m - 1) * num(for_del)) + num(for_add)) % q



def rabin_karp(s, p):
    ans = []
    n = len(s)
    m = len(p)
    hash_p = hash_func(p)
    for i in range(n-m+1):
        if i == 0:
            hash_s = hash_func(s[:m])
        else:
            hash_s = hash_next(len(p), hash_s, s[i - 1], s[i + m - 1])
        
        if hash_s == hash_p:
            if s[i:i+m] == p:
                ans.append(i)
    if ans:
        return ans
    return [-1]


p, s = input(), input()

print(* rabin_karp(s, p))