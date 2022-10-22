#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:15:58 2022

@author: gess
"""

def solution(A):
    sumA2 = sum(A[1:len(A)])
    sumA = A[0]
    minVal = abs(sumA - sumA2)
    j = 0
    for i in range(1,len(A)-1):
       sumA = sumA + A[i]
       sumA2 = sumA2 - A[i]
       # val = abs(sumA+A[i] - sum(A[i+1:len(A)]))
       val = abs(sumA - sumA2) 
       if val < minVal:
            minVal = val
            j = i
            
    return(minVal)

print(solution([-1000,1000] ))
