# import sys
# sys.setrecursionlimit(10**6)
import itertools
N, S, T = map(int, input().split())

ABCD = []

def cal_diff(x0, y0, x1, y1):
    return (x1-x0)**2+(y1-y0)**2

for _ in range(N):
    a, b, c, d = map(int, input().split())
    ABCD.append([a, b, c, d])

time = float('inf')
for L in list(itertools.permutations([i for i in range(N)], N)):
    # print(L)
    before_xy=[(0,0)]
    Time = [0]
    for i in range(len(L)):
        a, b, c, d = ABCD[L[i]]
        diff_abcd = cal_diff(a, b, c, d)
        tmp_xy=[]
        tmp_time=[]
        for j in range(len(Time)):
            before_x, before_y = before_xy[j]
            diff_ab = cal_diff(before_x, before_y, a, b)
            diff_cd = cal_diff(before_x, before_y, c, d)

            time_ab = Time[j]+diff_ab**(1/2)*S+diff_abcd**(1/2)*T
            tmp_xy.append((c, d))
            tmp_time.append(time_ab)

            time_cd = Time[j]+diff_cd**(1/2)*S+diff_abcd**(1/2)*T
            tmp_xy.append((a, b))
            tmp_time.append(time_cd)

        before_xy=tmp_xy
        Time=tmp_time

    if min(Time)<time:
        time = min(Time)

print(time)
