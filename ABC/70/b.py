A, B, C, D = map(int, input().split())

x = max(A, C)
y = min(B, D)

print(max(0, y-x))
