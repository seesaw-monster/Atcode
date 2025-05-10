# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
N = int(input())
S = []
for _ in range(N):
    S.append(list(input()))
T = []
for _ in range(N):
    T.append(list(input()))

# .; white, #; black
def lotate(X):
    Y = []
    for i in range(len(X)):
        tmp = []
        for j in range(len(X)):
            tmp.append(X[len(X)-1-j][i])
        Y.append(tmp)

    return Y

def count_diff(X, Y):
    c = 0
    for i in range(len(X)):
        for j in range(len(Y)):
            if X[i][j]!=Y[i][j]:
                c+=1

    return c

min_c = count_diff(S, T)
for i in range(3):
    S = lotate(S)
    c = count_diff(S, T) + 1 + i
    if c < min_c:
        min_c = c

print(min_c)
