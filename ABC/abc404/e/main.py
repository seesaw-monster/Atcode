# import sys
# sys.setrecursionlimit(10**6)
from collections import deque, defaultdict
N = int(input())
C = [0]
A = [0]
C.extend(list(map(int, input().split())))
A.extend(list(map(int, input().split())))

# dp = [[] for _ in range(N)]

i = N-1
c = 0
while True:
    print(A)
    input()
    if i==0:
        print(c)
        break
    if A[i]!=0:
        c+=1
        is_moved = False
        max_c = C[i-1]
        max_idx = i-1
        for j in range(1, C[i]+1):
            if A[i-j]:
                is_moved = True
                A[i-j]+=A[i]
                break
            else:
                if C[i-j]>max_c:
                    max_c = C[i-j]
                    max_idx = i-j
        if not is_moved:
            A[max_idx]+=A[i]

    i-=1
