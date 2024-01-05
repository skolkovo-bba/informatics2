a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = set(map(int, input().split()))

print(*sorted(list((b & c) - a)))