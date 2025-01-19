# import sys
# sys.setrecursionlimit(10**6)
Q = int(input())
hebi = []
idx = -1
minus = 0

for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0]==1:
        hebi.append(q[1] + hebi[-1] if len(hebi)>0 else q[1])
    elif q[0]==2:
        idx+=1
        minus=hebi[idx]
    else:
        if idx==-1 and q[1]==1:
            print(0)
        else:
            print(hebi[idx+q[1]-1]-minus)

