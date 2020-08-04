# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:22:34 2019

@author: Viraj Suri
"""

g=0
f=1
sum=0

for i in range (0,100):
    f=f+g
    g=f-g
    
    if(f%2==0):
        sum=sum+f
    if(f>4000000):
        break
    
    

print (sum)