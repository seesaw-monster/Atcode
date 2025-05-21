# import sys
# sys.setrecursionlimit(10**6)
from collections import deque, defaultdict
N, D = map(int, input().split())
A = list(map(int, input().split()))

ng_list = set()
count = defaultdict(int)

for a in A:
    count[a]+=1

# index, count, ng_list
q = deque([(0, 0, ng_list)])
min_c = float('inf')

while q:
    index, count, nl = q.popleft()

    # print(index, count, nl)

    if index==N:
        if min_c>count:
            min_c = count
    elif A[index] in nl:
        count+=1
        index+=1
        q.append((index, count, nl))
    else:
        nex_nl = []
        if A[index]-D > 0:
            nex_nl.append(A[index]-D)
        if A[index]+D > 0:
            nex_nl.append(A[index]+D)

        q.append((index+1, count, nl.union(nex_nl)))

        q.append((index+1, count+1, nl.union([A[index]])))

print(min_c)

