H, W=map(int,input().split())

l = []
for i in range(H):
    l.append([])
    line = input()
    for j in range(W):
        s = line[j]
        if s == '#':
            l[i].append(True)
        else:
            l[i].append(False)

x = 0
y = 0
c = False
for i in range(H):
    for j in range(W):
        if l[i][j]:
            x=i
            y=j
            c=True
            break
    if c:
        break
   
X = 0
Y = 0
c = False
for i in reversed(range(H)):
    for j in reversed(range(W)):
        if l[i][j]:
            X=i
            Y=j
            c=True
            break
    if c:
        break

c = False
for i in range(x,X+1):
    for j in range(y,Y+1):
        if not l[i][j]:
            c=True
            print(f'{i+1} {j+1}')
            break

if not c:
    print(f'{x+1} {y}')
