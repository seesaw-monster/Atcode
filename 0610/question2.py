l = sorted(input().split())
dlist = [3,1,4,1,5,9]
p = l[0]
q = l[1]
ip = 0
iq = 0

def f(i):
    if i=='A':
        return 0
    elif i=='B':
        return 1
    elif i=='C':
        return 2
    elif i=='D':
        return 3
    elif i=='E':
        return 4
    elif i=='F':
        return 5
    elif i=='G':
        return 6

ip = f(p)
iq = f(q)

s = 0

for j in range(ip, iq):
    s+=dlist[j]


print(s)
