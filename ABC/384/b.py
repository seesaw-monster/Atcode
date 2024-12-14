# import sys
# sys.setrecursionlimit(10**6)
N, R = map(int, input().split())

def next_rate(i, now, this):
    if i==1 and (1600<=now<=2799):
        return now+this
    elif i==2 and (1200<=now<=2399):
        return now+this

    return now

for i in range(N):
    d, a = map(int, input().split())
    R = next_rate(d, R, a)

print(R)
