# import sys
# sys.setrecursionlimit(10**6)
N = int(input())

isprime = [True for _ in range(10**6+1)]
isprime[0] = False
isprime[1] = False

for i in range(10**6+1):
    if not isprime[i]:
        continue

    for j in range(i*2, 10**6+1, i):
        isprime[j] = False

def is_liked_250(k):
    for p in range(k):
        if not isprime[p]:
            continue

        if p**4 > k:
            break

        for q in range(p+1, k):
            if not isprime[q]:
                continue

            if k == p*q**3:
                return True

    return False

c = [0]
for i in range(54, 10**6+1):
    c.append(c[-1] + (1 if is_liked_250(i) else 0))

print(c[N])
