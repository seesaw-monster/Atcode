# import sys
# sys.setrecursionlimit(10**6)
from collections import deque, defaultdict
N, D = map(int, input().split())
A = list(map(int, input().split()))

c = 0
ng_list = set()
now_ng = set()
count = defaultdict(int)

for i in range(N):
    count[A[i]]+=1
    if A[i]-D>=0:
        ng_list.add(A[i]-D)
    if A[i]-D<=10**6:
        ng_list.add(A[i]+D)

    if A[i] in ng_list:
        now_ng.add(A[i])
        if count[A[i]-D]>0:
            now_ng.add(A[i]-D)
        if count[A[i]+D]>0:
            now_ng.add(A[i]+D)

print(now_ng)
print(count)
