#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:39:49 2022

@author: gess
"""
D = [-1]

def solA(A):
    A = set(A)
    B = []
    C = []
    for i in A:
        if i>0:
            B.append(i)
       
    if len(B) == 0: 
        return(1)
    else:
        E = list(range(1,len(B)+1))
        F = E.difference(B)
        if F != []:
            return(F[1])
        else:
            return(min(B)+1)
    
print(solA(D))

