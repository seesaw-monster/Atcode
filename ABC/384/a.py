# import sys
# sys.setrecursionlimit(10**6)
N, c1, c2 = input().split()
S = list(input())

for i in range(int(N)):
    if S[i]!=c1:
        S[i]=c2

s = ''
for si in S:
    s+=si

print(s)
