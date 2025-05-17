# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
N = int(input())
P = list(map(int, input().split()))

diff = [P[0]<P[1]]
diff_len = [1]

for i in range(1, N-1):
    if diff[-1]==(P[i]<P[i+1]):
        diff_len[-1]+=1
    else:
        diff_len.append(1)
    diff.append(P[i]<P[i+1])

c = 0

l = 0
for i in range(len(diff_len)-2):
    if diff[l]:
        c+=diff_len[i]*diff_len[i+2]

    l += diff_len[i]

print(c)
