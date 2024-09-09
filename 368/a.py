N, K = map(int, input().split())
A = list(map(int, input().split()))

B = []
B.extend(A[-K:])
B.extend(A[:-K])
print(*B)
