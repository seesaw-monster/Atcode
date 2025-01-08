# import sys
# sys.setrecursionlimit(10**6)
isprime = [True for _ in range(10**5+1)]
isprime[0] = False
isprime[1] = False
is_liked_2017 = [False for _ in range(10**5+1)]

def like_2017(N):
    return True if (isprime[N] and isprime[(N+1)//2]) else False

for i in range(2, 10**5+1):
    if not isprime[i]:
        continue

    if i%2==1 and like_2017(i):
        is_liked_2017[i] = True

    for j in range(i*2, 10**5+1, i):
        isprime[j] = False

sum_c = [0]
for i in range(1, 10**5+1):
    sum_c.append(sum_c[-1]+(1 if is_liked_2017[i] else 0))

Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())
    print(sum_c[r]-sum_c[l-1])
