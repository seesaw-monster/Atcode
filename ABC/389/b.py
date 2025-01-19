# import sys
# sys.setrecursionlimit(10**6)
X = int(input())

def cal_Kai(N):
    s = 1
    for i in range(1, N+1):
        s*=i

    return s

for n in range(1, X+1):
    if cal_Kai(n)==X:
        print(n)
        exit()
