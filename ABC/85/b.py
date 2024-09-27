N = int(input())
d = []

for _ in range(N):
    d.append(int(input()))

d.sort(reverse=True)

count = 1
before_d = d[0]

for i in range(1, N):
    if before_d > d[i]:
        before_d = d[i]
        count+=1

print(count)
