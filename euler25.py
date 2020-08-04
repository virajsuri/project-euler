# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:48:19 2020

@author: Viraj Suri
"""

f = 1
g = 0

for i in range(2, 1000000):
    f=f+g
    g=f-g
    if(f%1==0):
        length = len(str(f))
        if(length==1000):
            print(i)
            break