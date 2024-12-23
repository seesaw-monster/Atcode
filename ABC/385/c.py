# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
H = list(map(int, input().split()))

max_c = 1
for mid in range(N-2):
    for start_l in range(N-mid):
        r = start_l+mid+1
        c = 1
        for l in range(start_l, N-mid, mid+1):
            while r < N and H[l]==H[r]:
                r+=mid+1
                c+=1

            if c>max_c:
                max_c = c

            c-=1

print(max_c)
