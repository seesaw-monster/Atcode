# import sys
# sys.setrecursionlimit(10**6)
N = int(input())

def cost(a, b, c, d):
    return ((a-c)**2 + (b-d)**2)**(1/2)

all_cost = 0
X = [0]; Y = [0]
for _ in range(N):
    x, y = map(int, input().split())
    all_cost += cost(X[-1], Y[-1], x, y)
    X.append(x)
    Y.append(y)

print(all_cost+cost(X[-1], Y[-1], 0, 0))
