N=int(input())
s=set()
for _ in range(N):
    si = input()
    s.add(min(si,si[::-1]))

print(len(s))
