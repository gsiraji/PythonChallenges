#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 07:59:46 2022

@author: gess
"""



def solution1(A):
    A.append(0)
    for i in range(1,max(A)+2):
        if i not in A:
            return(i)
        
        
def solution(A): 
    A = set(A) 
    B = {i for i in range(1,max(A)+2)}
    if len(B) == 0:
        return(1)
    else:
        return(min(B.difference(A)))
        


       

B = [-100000,100000,2]
B = set(B)
C = {-100}
print(solution(B))
