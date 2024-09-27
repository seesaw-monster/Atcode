N = int(input())

la = 0
ra = 0

left = True
right = True

weight = 0

for _ in range(N):
    a, s = input().split()
    a = int(a)

    if s == 'L' and left:
        left = False
        la = a
    elif s == 'R' and right:
        right = False
        ra = a
    elif s == 'L':
        weight += abs(la-a)
        la = a
    else:
        weight += abs(ra-a)
        ra = a

print(weight)
