def cal_dist(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

N, S, T = map(int, input().split())
X = []; Y = []; dist = []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    X.append([a, c])
    Y.append([b, d])
    dist.append(cal_dist(a, b, c, d)**(1/2))

print(sum(dist)/T)
