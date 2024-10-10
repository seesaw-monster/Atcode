# import sys
# sys.setrecursionlimit(10**6)
N, S, T = map(int, input().split())

before_x = 0;before_y = 0

ABCD = []
diff = []

def cal_diff(x0, y0, x1, y1):
    return (x1-x0)**2+(y1-y0)**2

for _ in range(N):
    a, b, c, d = map(int, input().split())
    ABCD.append([a, b, c, d])
    diff.append(min(cal_diff(0, 0, a, b), cal_diff(0, 0, c, d)))

time = 0
while len(ABCD) > 0:
    idx = 0
    min_d = float('inf')
    for i in range(len(diff)):
        if diff[i]<min_d:
            idx = i
            min_d = diff[i]

    a, b, c, d = ABCD.pop(idx)
    _ = diff.pop(idx)
    ab_diff = cal_diff(before_x, before_y, a, b)
    cd_diff = cal_diff(before_x, before_y, c, d)
    if ab_diff<=cd_diff:
        before_x = c
        before_y = d
        time += ab_diff**(1/2)/S + cal_diff(a, b, c, d)**(1/2)/T
    else:
        before_x = a
        before_y = b
        time += cd_diff**(1/2)/S + cal_diff(c, d, a, b)**(1/2)/T

    for i in range(len(ABCD)):
        a, b, c, d = ABCD[i]
        diff[i] = min(cal_diff(before_x, before_y, a, b), cal_diff(before_x, before_y, c, d))

print(time)
