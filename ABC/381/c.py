# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
S = input()
max_n = 0
l_count = 0
b = False
r_count = 0

for i in range(N):
    if S[i]=='1':
        if b:
            l_count = 0
            b = False
            if 2*r_count+1>max_n:
                max_n = 2*r_count+1
            r_count = 0
        l_count+=1
    elif S[i]=='/':
        if b:
            l_count = 0
            if 2*r_count+1>max_n:
                max_n = 2*r_count+1
            r_count = 0
        b = True
    else:
        if b:
            if l_count>r_count:
                r_count+=1
        else:
            l_count=0

if b and 2*r_count+1>max_n:
    max_n = 2*r_count+1

print(max_n)
