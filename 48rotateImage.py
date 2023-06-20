# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:54:57 2019

@author: liuga
"""

class Solution(object):
    def rotate(self, matrix):
        if matrix:
            rows = len(matrix)
            cols = len(matrix[0])
            
        for i in range(rows//2):
            for j in range(cols):
                matrix[i][j],matrix[rows-i-1][j] = matrix[rows-i-1][j],matrix[i][j]
                
        for i in range(rows):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        if not matrix:
            return

        
    def rotate(self, matrix):    
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i]  = matrix[j][i],matrix[i][j]

        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
        
        
        return matrix
