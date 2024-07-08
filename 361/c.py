N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

i = 0
j = len(A) - 1

min_diff = A[j] - A[i]

for k in range(K+1):
    if A[j-(K-k)] - A[i+k] < min_diff:
        min_diff = A[j-(K-k)] - A[i+k]

print(min_diff)

