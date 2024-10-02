# import sys
# sys.setrecursionlimit(10**6)
S = list(input())

Z = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

before = -1
cost = 0
for i in range(26):
    now = Z[i]
    for j in range(26):
        if S[j]==now:
            if not before == -1:
                cost += abs(j-before)
            before = j

print(cost)
