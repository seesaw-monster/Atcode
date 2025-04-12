# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
N, K = map(int, input().split())
S = list(input())

co = 0
cq = 0
for i in range(N):
    if S[i]=='o':
        co+=1
        if i>0:
            S[i-1]='.'

        if i<N-1:
            S[i+1]='.'

for i in range(N):
    if S[i]=='?':
        cq+=1

if (K-co)==cq:
    for i in range(N):
        if S[i]=='?':
            S[i]='o'
if (K-co)==0:
    for i in range(N):
        if S[i]=='?':
            S[i]='.'

if cq-(K-co)==1 and cq%2==1:
    for i in range(N):
        if S[i]!='?':
            continue

        if i>0 and S[i-1]=='o':
            S[i]='.'
            continue

        if i<N-1 and S[i+1]=='o':
            S[i]='.'
            continue

        S[i] = 'o'
        if i<N-1:
            S[i+1]='.'

s = ''
for x in S:
    s+=x
print(s)
