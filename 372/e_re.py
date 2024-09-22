import sys
sys.setrecursionlimit(1000000)
N, Q = map(int, input().split())

G = [[i] for i in range(N)]

def search(G, v, H):
    for i in range(len(G[v])):
        if not G[v][i] in H:
            H.add(G[v][i])
            search(G, G[v][i], H)

    return H

for _ in range(Q):
    t, *s = map(int, input().split())

    # print(t, *s)

    if t == 1:
        u = s[0]-1
        v = s[1]-1
        G[u].append(v)
        G[v].append(u)
        # print(G)
    else:
        v = s[0]-1
        k = s[1]-1

        H = set()
        H = search(G, v, H)
        if len(H)<k+1:
            print(-1)
        else:
            print(sorted(H, reverse=True)[k]+1)
