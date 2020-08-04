# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 11:36:29 2020

@author: Viraj Suri
"""


base=1
sum =0
sum10=0
squaresum=0

for i in range(0,100):
    square=base**2
    sum=sum+square
    base+=1
print('The sum of the squares',sum)


base=1
for i in range(0,100):
    sum10+=base
    squaresum=sum10**2
    base+=1
print('The square of the sum of the squares',squaresum)

print('Difference between the two',squaresum-sum)