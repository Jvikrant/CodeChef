# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 11:53:55 2019

@author: Vikrant
"""

def whoWins():
    t=int(input())
    
    while t>0:
        n,a,b=map(int,input().split())

        arr=map(int,input().split())
        abcount,acount,bcount=0,0,0
        for i in arr:
            if i%a==0 and i%b==0:
                abcount+=1
            elif i%a==0 and i%b!=0:
                acount+=1
            elif i%a!=0 and i%b==0:
                bcount+=1
 

                
        
        if acount+abcount%2>bcount:
            print("BOB")
        else:
            print("ALICE")
        t-=1

whoWins()
