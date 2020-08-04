# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:18:07 2019

@author: Viraj Suri
"""

sum =0
for i in range (0,1000):
    if (i%3==0) or (i%5==0):
        print (i)
        sum+=i
    
    print(sum)