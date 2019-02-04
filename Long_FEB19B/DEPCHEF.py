T=int(input())

for t in range(T):

    #taking inputs
    N=int(input())
    attack=list(map(int,input().split()))
    defence=list(map(int,input().split()))

    survived=[]
    for i in range(N):
        if defence[i]>attack[(i+1)%N]+attack[i-1]:
            survived.append(defence[i])

    if len(survived)==0:
        print(-1)
    else:
        print(max(survived))
