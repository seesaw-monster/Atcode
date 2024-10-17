# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
# . = 白, not 黒
A = []
for _ in range(N):
    A.append(list(input()))

B = [list('.'*N) for _ in range(N)]

for i in range(N//2):
    for x in range(N-i):
        for y in range(N-i):
            B[y][N-1-x] = A[x][y]
    A, B = B, A

for i in range(N):
    s = ''
    for j in range(N):
        s += A[i][j]
    print(s)
