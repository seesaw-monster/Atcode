N = int(input())
A = list(map(int, input().split()))

idx = list(range(1, N+1))

A = list(zip(A, idx))

A = sorted(A, key=lambda x: x[0])

print(A[-2][1])
