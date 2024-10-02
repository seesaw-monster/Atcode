import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

D = [[] for _ in range(N)]

for i in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    D[u].append({str(v):w})

# print(D)

use = [False for _ in range(N)]
value = [0 for _ in range(N)]

def search(i):
    for d in D[i]:
        for k, v in d.items():
            if use[int(k)]:
                value[i] = value[int(k)] - v
                continue
            value[int(k)] += v
            use[int(k)] = True
            search(int(k))
        
    return

for i in range(N):
    if use[i] or len(D[i])==0:
        continue

    use[i] = True
    search(i)

print(*value)
