# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
A = list(map(int, input().split()))

B = {}

C = []

for i in range(len(A)):
    if A[i] in B.keys():
        C.append(B[A[i]])
    else:
        C.append(-1)
    B[A[i]] = i+1

print(*C)
