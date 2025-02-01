# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque
A = list(map(int, input().split()))
B = [i for i in range(1, 6)]

flag = [A[i]!=B[i] for i in range(5)]

if sum(flag)!=2:
    print('No')
else:
    l = -1
    r = -1
    for i in range(5):
        if flag[i]:
            if l==-1:
                l = i
            else:
                r = i

    if l+1==r:
        print('Yes')
    else:
        print('No')

