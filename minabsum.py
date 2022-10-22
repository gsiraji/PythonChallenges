#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 08:52:21 2022

@author: gess
"""

#def PowerSet(A,set_size):
    
    
    
     
    # # set_size of power set of a set
    # # with set_size n is (2**n -1)
    # pow_set_size = (int) (2**set_size);
    # counter = 0;
    # j = 0;
    # 
    
    # yield [] # first return the result we’re sure about 
    # for i in range(len(A)):
    #     for x in classical_recursive_one(A[i+1:]): 
    #         # induction part 
    #         yield [A[i]] + x 
    

    # minSum = abs(sum(minList))   
    # return(minList, minSum)
 
# Driver program to test printPowerSet

def PowerSet(A):
    yield [] 
    for i in range(len(A)):
        for x in PowerSet(A[i+1:]): 
            # induction part 
            yield [A[i]] + x 

B = [1,-1,1,-1,1000,20];
lengthB = len(B)
#Bprime = [b * -1 for b in B]
for b in range(lengthB):
    B.append(-1*B[b])
minSum = abs(min(B))
minList = [min(B)]
for x in PowerSet(B):
    if len(x) != 0:
        if abs(sum(x)) < minSum:
            
            minList = x
            minSum = abs(sum(x))
        elif (abs(sum(x)) == minSum & len(x) < len(minList)):
            minList = x
print(minList, minSum);
