N, M = map(int, input().split())
D = [{} for _ in range(N)]
bD = [False for _ in range(N)]
W = [0 for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1

    D[u].update({str(v):w})
    D[v].update({str(u):-w})

start_i = -1
for i in range(N):
    if bD[i]:
        continue
    st = [i]
    bD[i] = True
    while st:
        u = st.pop()

        for k, v in D[u].items():
            if not bD[int(k)]:
                bD[int(k)] = True
                W[int(k)] = W[u] + v
                st.append(int(k))

print(*W)
