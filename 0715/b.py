N,M=map(int,input().split())

p_list=[]
for i in range(N):
    p_list.append(list(map(int,input().split())))

p_list = sorted(p_list)

is_up=False
for i in range(N):
    m_list=[0]*(M+1)
    for k in range(1,len(p_list[i])):
        m_list[p_list[i][k]]=1

    for j in range(i+1,N):
        if len(p_list[i][1:]) < len(p_list[j][1:]):
            continue
        elif len(p_list[i][1:])==len(p_list[j][1:]) and p_list[i][0]==p_list[j][0]:
            continue

        is_up=True
        for k in range(1,len(p_list[j])):
            if m_list[p_list[j][k]]==0:
                is_up=False
                break

        if is_up:
            print('Yes')
            break

    if is_up:
        break

if not is_up:
    print('No')
