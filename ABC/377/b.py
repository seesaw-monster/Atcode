# import sys
# sys.setrecursionlimit(10**6)
S = []
for _ in range(8):
    S.append(list(input()))

empty = [[True for _ in range(8)] for _ in range(8)]

for i in range(8):
    for j in range(8):
        if S[i][j] == '#':
            for k in range(8):
                empty[i][k] = False
                empty[k][j] = False

s = 0
for k in range(8):
    s+=sum(empty[k])

print(s)
