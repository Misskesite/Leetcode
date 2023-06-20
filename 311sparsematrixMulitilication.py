# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:04:08 2020

@author: liuga
"""

class Solution(object):
    def multiply(self, A, B):
        if len(A) == 0 or len(B)==0:
            return [[]]
        a, c, b = len(A), len(B), len(B[0])
        AB =[[0 for _ in range(b)] for _ in range(a)]
        for i in range(a):
            for j in range(c):
                if A[i][j] != 0:
                    for k in range(b):
                        if B[j][k] !=0:
                            AB[i][k] += A[i][j]*B[j][k]
        return AB
        


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        n = len(mat2) #对应k
        l = len(mat2[0])
        ans = [[0] * l for _ in range(m)]

        for i in range(m):
            for k in range(n):
                if mat1[i][k] != 0:
                    for j in range(l):
                        if mat2[k][j] != 0:
                            ans[i][j] += mat1[i][k] * mat2[k][j]

        return ans
