a = {input() for _ in range(int(input()))}
b = {input() for _ in range(int(input()))}

print(len(a & b), len(b - a), len(a - b))