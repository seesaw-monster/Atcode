# import sys
# sys.setrecursionlimit(10**6)
# MON - FRI AM. - PM.
# 店舗数
N = int(input())
# 営業時間
F = []
# 両方営業していると得られる利益
P = []

for _ in range(N):
    F.append(list(map(int, input().split())))
for _ in range(N):
    P.append(list(map(int, input().split())))

max_value = -float('inf')
for i in range(1, 2**10):
    tmp = 0
    # for j in range(10):
    #     if i >> j & 1:
    for n in range(N):
        count = 0
        for j in range(10):
            if F[n][j] == 1 and i>>j & 1:
                count += 1
        tmp += P[n][count]
    if tmp > max_value:
        max_value = tmp

print(max_value)
