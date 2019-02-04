# cook your dish here
def GCD(A,B):
    if B==0:
        return A
    return GCD(B,A%B)
    
t=int(input())

for T in range(t):
    N,A,B,K=tuple(map(int,input().split()))
    
    cm=0
    count=0
    gcd=GCD(A,B)
    
    if gcd:
        cm=N*gcd
        cm=cm//(A*B)
    
    if A<=N:
        count+=N//A
    
    if B<=N:
        count+=N//B
        
    count-=2*cm
    
    if count>=K:
        print("Win")
    else:
        print("Lose")