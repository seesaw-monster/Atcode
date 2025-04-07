# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
N, M = map(int, input().split())

S = []

for _ in range(N):
    S.append(list(input()))

T = []

for _ in range(M):
    T.append(list(input()))

# . : white # : black

def judge(a, b):
    for i in range(M):
        for j in range(M):
            if S[a+i][b+j]!=T[i][j]:
                return False

    return True

for a in range(N-M+1):
    for b in range(N-M+1):
        if judge(a, b):
            print(a+1, b+1)
            exit()
