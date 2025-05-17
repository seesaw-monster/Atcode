H, W, N = map(int, input().split())

dH = [set() for _ in range(H)]
dW = [set() for _ in range(W)]

for i in range(N):
    x, y = map(int, input().split())
    x-=1
    y-=1

    dH[x].add(y)
    dW[y].add(x)

Q = int(input())

for _ in range(Q):
    q, z = map(int, input().split())
    z-=1
    if q==1:
        print(len(dH[z]))
        for k in dH[z]:
            dW[k].remove(z)
        dH[z] = set()
    else:
        print(len(dW[z]))
        for k in dW[z]:
            dH[k].remove(z)
        dW[z] = set()
