import numpy as np
# 頂点，辺，人口
N,M,K=map(int,input().split())

xy_list=[]
for i in range(1,N+1):
    xy_list.append(list(map(int,input().split())))

uvw_list=[]
for i in range(N+1,N+M+1):
    uvw_list.append(list(map(int,input().split())))

ab_list=[]
for i in range(N+M+1,N+M+K+1):
    ab_list.append(list(map(int,input().split())))

def D(xu,yu,xv,yv):
    return round(((xu-xv)**2+(yu-yv)**2)**(1/2))

b_list=np.zeros(N)
p_list=np.zeros(N)
for k in range(K):
    diff_list=[]
    for n in range(N):
        diff_list.append(D(ab_list[k][0],ab_list[k][1],xy_list[n][0],xy_list[n][1]))

    ind=diff_list.index(min(diff_list))
    b_list[ind]=1
    p_list[ind]=diff_list[ind]

b_str=''
p_str=''
for i in range(N-1):
    b_str+=f'{b_list[i]} '
    p_str+=f'{p_list[i]} '

b_str+=f'{b_list[N-1]}'
p_str+=f'{p_list[N-1]}'
print(p_str)
print(b_str)
