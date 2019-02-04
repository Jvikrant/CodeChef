t=int(input())

for T in range(t):
    N=int(input())
    
    #list of sets
    dishes=[]
    for i in range(N):
        dish=input()
        dishes.append(set(dish))
    
    count=0

    for i in dishes[0]:
        si=True
        for j in range(1,N):
            if i not in dishes[j]:
                si=False
                break
        
        if si:
            count+=1
    
    print(count)
