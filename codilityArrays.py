#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:31:19 2022

@author: gess
"""

def rotateA(A,K):
    B =[0]*len(A)
    for i in range(len(A)):
        j = (i+K)%len(A)
        B[j] = A[i]

        

    return(B)


print(rotateA([3, 8, 9, 7, 6],3))
    
