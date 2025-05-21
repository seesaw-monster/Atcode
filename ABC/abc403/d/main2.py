# import sys
# sys.setrecursionlimit(10**6)
from collections import deque, defaultdict
N, D = map(int, input().split())
A = list(map(int, input().split()))

ng_list = set()
count = defaultdict(int)

exist = set(A)

for a in A:
    count[a]+=1
    if a-D in exist:
        ng_list.add(a-D)

    if a+D in exist:
        ng_list.add(D+a)

    if a-D in exist or a+D in exist:
        ng_list.add(a)

if ng_list:
    q = deque([(ng, 0, ng_list.copy()) for ng in ng_list])
else:
    print(0)
    exit()

min_count = float('inf')

while q:
    ng, c, l = q.popleft()
    # print(ng, c, l)
    l.remove(ng)
    flag = True

    if ng-D in l or ng+D in l:
        c += count[ng]

        if ng-D in l and ng+D in l:
            if not ng-2*D in l and not ng+2*D in l:
                l.remove(ng-D)
                l.remove(ng+D)
            elif not ng-2*D in l:
                flag = False
                l.remove(ng-D)
                q.append((ng+D, c, l.copy()))
                q.append((ng+2*D, c, l.copy()))
            elif not ng+2*D in l:
                flag = False
                l.remove(ng+D)
                q.append((ng-D, c, l.copy()))
                q.append((ng-2*D, c, l.copy()))
            else:
                flag = False
                q.append((ng+D, c, l.copy()))
                q.append((ng+2*D, c, l.copy()))
                q.append((ng-D, c, l.copy()))
                q.append((ng-2*D, c, l.copy()))
        elif ng-D in l:
            if not ng-2*D in l:
                l.remove(ng-D)
            else:
                flag = False
                q.append((ng-D, c, l.copy()))
                q.append((ng-2*D, c, l.copy()))
        elif ng+D in l:
            if not ng+2*D in l:
                l.remove(ng+D)
            else:
                flag = False
                q.append((ng+D, c, l.copy()))
                q.append((ng+2*D, c, l.copy()))

    # print(ng, flag, l, c)

    if flag:
        if len(l) <= 1:
            if c < min_count:
                min_count = c
        else:
            nex_l = l.copy()
            q.append((l.pop(), c, nex_l))

print(min_count)


