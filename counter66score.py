#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:33:58 2022

@author: gess
"""

def increase(x,Nvec):
    Nvec[x-1] += 1
    return(Nvec)


def maxCounter(Nvec,N):
    Nvec = [max(Nvec)]*N
    return(Nvec)
    
def solution(N,A):
    Nvec = [0]*N
    for k in range(len(A)):
        if A[k] <= N:
            if A[k] > 0:

                Nvec = increase(A[k], Nvec)

        elif A[k] == N+1:
            Nvec = maxCounter(Nvec, N)
    return(Nvec)


print(solution(5,[3,4,4,6,1,4,4]))
