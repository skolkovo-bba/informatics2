from collections import deque

N, M = map(int, input().split())

Graph = {x: [] for x in range(N)}

in_sides = [0] * N # Список с количеством входящих рёбер для каждой вершины
for i in range(M):
    a, b = map(int, input().split())
    Graph[a].append(b)
    in_sides[b] += 1
    
queue = deque()
for i in range(N):
    if in_sides[i] == 0:
        queue.append(i)
        
result = []

while queue:
    current = queue.popleft()
    result.append(current)
    for next_v in Graph[current]:
        in_sides[next_v] -= 1
        if in_sides[next_v] == 0:
            queue.append(next_v)
            
if len(result) != N:
    print('NO')
else:
    print(*result)