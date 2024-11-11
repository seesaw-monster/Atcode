# import sys
# sys.setrecursionlimit(10**6)
N, K = map(int, input().split())
S = list(input())

# O, X
count = 0

ox = 0
for i in range(N):
    if S[i]=='O':
        ox+=1
        if ox == K:
            count+=1
            ox=0
    else:
        ox=0

print(count)
