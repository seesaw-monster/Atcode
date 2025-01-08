N = int(input())

answer = 0

isprime = [True for _ in range(N+1)]
isprime[0] = False
isprime[1] = False

for i in range(2, N+1):
    if not isprime[i]:
        continue

    for j in range(i*2, N+1, i):
        isprime[j] = False

# print(answer)
for i in range(1, 51):
    print(f'{i} : {"prime" if isprime[i] else "not"}')
