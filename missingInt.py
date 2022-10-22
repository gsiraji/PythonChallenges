#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 15:19:38 2022

@author: gess
"""

def solution(A):
    N = len(A)
    B = [0]*(len(A)+1)
    for i in range(len(A)+1):
        B[i] = i+1
    return(sum(B)-sum(A))


B = [0]*(100000)
for i in range(len(B)):
    B[i] = i+1
    
print(sum(B))


print(solution([1,2,4,5]))
