# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 11:53:55 2019

@author: Vikrant
"""

def whoWins():
    t=int(input())
    
    while t>0:
        n,a,b=map(int,input().split())
    
 
                
        
        if acount+abcount%2>bcount:
            print("BOB")
        else:
            print("ALICE")
        t-=1

whoWins()