# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
N = int(input())
P = list(map(int, input().split()))

r = 0
c = 0

# <> の判定
is_o = [False for _ in range(N)]
for i in range(1, N-1):
    if P[i-1]<P[i]>P[i+1]:
        is_o[i]=True

# print(is_o)

# >< の判定
is_x = [False for _ in range(N)]
for i in range(1, N-1):
    if P[i-1]>P[i]<P[i+1]:
        is_x[i]=True

# print(is_x)

count_o = 0
count_x = 0
before_count = 0
for l in range(N-3):
    if is_o[l]:
        count_o = max(0, count_o-1)
    if is_x[l]:
        count_x = max(0, count_x-1)

    if P[l]>=P[l+1]:
        before_count = 0
        continue
    elif count_o==1 and count_x==1:
        c+=min(before_count, r-l-2)

    if r <= l:
        r = l+1

    # print(l, r, count_o, count_x)
    # print(c)

    before_count = 0

    while r <= N-2:
        r+=1
        if is_o[r-1]:
            if count_o==1:
                r-=1
                break
            count_o+=1

        if is_x[r-1]:
            if count_x==1:
                r-=1
                break
            count_x+=1

        if r-l+1 >= 4 and count_o==1 and count_x==1:
            c+=1
            before_count+=1

    # print(c)

print(c)
