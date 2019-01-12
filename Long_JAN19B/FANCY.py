# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 11:41:24 2019

@author: Vikrant
"""

t=int(input())

while t:
    s=input()
    
    isReal=False
    
    s=set(s.split())
    if "not" in s:
        print("Real Fancy")
    else:
        print("regularly fancy")
    t-=1