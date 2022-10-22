#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:53:29 2022

@author: gess
"""

def solution(A):
    B = A.copy()
    evenList = [0]*len(A)
    i = 0
    while len(B) > 0:
        
        a = B[0]
        B.pop(0)
        indx = A.index(a)
        evenList[indx] = (evenList[indx]+1)%2
        
    k = evenList.index(1)
    
    return(A[k])


def solution2(A):

    evenList = [0]*len(A)
    i = 0
    while i < len(A):
        a = A[i]
        indx = A.index(a)
        evenList[indx] = (evenList[indx]+1)%2
        i += 1
    k = evenList.index(1)
    
    return(A[k])



print(solution2([9,3,9,3,9,1,9]))
