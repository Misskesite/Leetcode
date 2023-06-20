# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 20:21:35 2020

@author: liuga
"""

class Solution(object):
    def rangesum(self, matrix, row1, col1, row2, col2):
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        sumM = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                sumM[i+1][j+1] =  sumM[i][j+1] + sumM[i+1][j] - sumM[i][j] + matrix[i][j]
        return sumM[row2 + 1][col2 + 1] - sumM[row2 + 1][col1] - sumM[row1][col2 + 1] + sumM[row1][col1]
