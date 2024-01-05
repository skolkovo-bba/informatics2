def binpow(a, n):
    res = 1
    while n:
        if n & 1:
            res *= a
        a *= a
        n >>= 1
    
    return res

p = input()
s = input()
s = p + s
i1, i2, size # входные данные

p = 31
p_pow = [0] * len(s)
p_pow[0] = 1
for i in range(1, len(p_pow)):
	p_pow[i] = p_pow[i-1] * p


h = [0] * len(s)
for i in range(len(s)):
	h[i] = (s[i] - 'a' + 1) * p_pow[i]
	if i:
             h[i] += h[i-1]
    h[i] = h[i] % binpow(2, 64)

for i in range(n):
    h1 = h[i1 + size - 1]
    if i1:
        h1 -= h[i1-1]
        
    h2 = h[i2 + size - 1]
    if i2:
        h2 -= h[i2-1]


    if (i1 < i2 and h1 * p_pow[i2 - i1] == h2 or i1 > i2 and h1 == h2 * p_pow[i1 - i2]):
        print("eee")
    else:
        print("neeee")