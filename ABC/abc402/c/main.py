# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
N, M = map(int, input().split())
K = []
A = []

for _ in range(M):
    tmp = list(map(int, input().split()))
    K.append(tmp[0])
    A.append(tmp[1:])

B = list(map(int, input().split()))

dic = {}
for i in range(len(B)):
    dic[B[i]]=i

count = [0 for _ in range(N)]
for i in range(M):
    index = -1
    for a in A[i]:
        if dic[a]>index:
            index=dic[a]
    count[index]+=1

for i in range(N-1):
    count[i+1]+=count[i]

for i in range(N):
    print(count[i])
