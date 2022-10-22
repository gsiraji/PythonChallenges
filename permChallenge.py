#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:33:58 2022

@author: gess
"""
def counting(A, m):
    n = len(A)
    count = [0] * (m)
    for k in range(n):
        count[A[k]-1]+=1
    return(count)

def edgeCases(A):
    if max(A) != len(A):
        return(0)
    if min(A) != 1:
        return(0)

def solution(A):
   # edgeCases(A)
    if sum(A) == (len(A)+1)*len(A)/2:
        perm1  = counting(A, max(A))
        print(perm1)
        if all(perm1) == 1:
            return(1)
        else:
            return(0)
    else:
        return(0)



m = [4,1,3,2]

print(solution(m))
