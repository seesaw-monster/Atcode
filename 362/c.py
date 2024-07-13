N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

min_s = 0
max_s = 0
sum_l = 0

for l, r in LR:
    sum_l += l
    min_s += l
    max_s += r

if max_s >= 0 and min_s <= 0:
    print("Yes")

    lr = []
    for l, r in LR:
        if sum_l < 0:
            if abs(sum_l) > (r-l):
                lr.append(r)
                sum_l += (r-l)
            else:
                lr.append(l+abs(sum_l))
                sum_l = 0
        else:
            lr.append(l)

    print(*lr)

else:
    print("No")
