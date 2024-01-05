def input_graph(): 
    n = int(input()) 
    m = int(input()) 
    A = {k: set() for k in range(n)} 
    G = {k:set() for k in range(n)} 
    G_transposed = {k:set() for k in range(n)} 
    for i in range(m): 
        a, b = map(int, input().split()) 
        G[a].add(b) 
        G_transposed[b].add(a) 
        A[a].add(b) 
        A[b].add(a) 
    return G, G_transposed, A 
 
 
def dfs(v, G, gray, order): 
    gray.add(v) 
    for u in G[v]: 
        if u not in gray: 
            dfs(u, G, gray, order) 
    order.append(v) 
 
G, G_transposed, A = input_graph() 
white = set(G.keys()) 
used = set() 
k = 0 
 
while white: 
    v = white.pop() 
    dfs(v, A, used, []) 
    white -= used 
    k += 1 
white = set(G) 
black = set() 
order = [] 
used = set() 
 
while white: 
    v = white.pop() 
    #print('dfs', v, G_transposed, used, order) 
    dfs(v, G_transposed, used, order) 
    white -= used 
#print(' '.join(map(str, order[::-1]))) 
 
used = set() 
c = 0 
while len(used) != len(G): 
    v = order.pop() 
    while v in used: 
        v = order.pop() 
    dfs(v, G, used, []) 
    c += 1 
print(k, c)