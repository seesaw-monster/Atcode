N, K, X = map(int, input().split())
A = list(map(int, input().split()))

B = []
if K == len(A):
    A.append(X)
    print(*A)
else:
    for i in range(len(A)):
        if i == K:
            B.append(X)
        B.append(A[i])
    print(*B)
