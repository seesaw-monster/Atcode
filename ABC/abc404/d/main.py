# import sys
# sys.setrecursionlimit(10**6)
from collections import deque, defaultdict
N, M = map(int, input().split())
C = list(map(int, input().split()))

enn = defaultdict(list)
for i in range(M):
    K = list(map(int, input().split()))
    A = K[1:]
    for a in A:
        enn[a-1].append(i)

min_price = float('inf')
q = deque([[i, [0 for _ in range(M)], 0] for i in range(N)])
while q:
    x, before_count, price = q.popleft()
    if len(enn[x])==0:
        continue
    if price > min_price:
        continue

    price += C[x]
    for animal in enn[x]:
        before_count[animal]+=1

    is_finished = True
    key_num = -1
    for i in range(len(before_count)):
        if before_count[i]<2:
            key_num = i
            is_finished=False
            break

    if is_finished:
        if price< min_price:
            min_price=price
        continue
    else:
        for i in range(N):
            if key_num in enn[i]:
                q.append([i, before_count.copy(), price])

print(min_price)
