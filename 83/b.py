N, A, B = map(int, input().split())

sum_all = 0
for n in range(1, N+1):
    tmp_n = n
    sum_n = 0
    for i in reversed(range(5)):
        sum_n += tmp_n//(10**i)
        tmp_n -= (10**i)*(tmp_n//(10**i))

    if sum_n >= A and sum_n <= B:
        sum_all+=n

print(sum_all)
