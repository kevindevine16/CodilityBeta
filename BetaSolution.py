# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 12:58:43 2021

@author: Kevin.Devine
"""

def solution(A):
    n = len(A)
    B = [0 for ii in range(n)]
    counter = 0 
    for i in range(n):
        B[i] = A[i]+i
        for iii in range(i):
            if B[iii] >= i-A[i]:
                counter += 1
                if counter > 10000000:
                    counter = -1
                    iii = i
                    i = n-1
    return counter