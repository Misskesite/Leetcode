# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:16:12 2019

@author: liuga
"""
#O(1)空间，两个flag位
class Solution(object):
    def setmatrixZero(self, matrix):
        first_row = False
        first_col = False
        
        m = len(matrix)
        n = len(matrix)
        
        #找第一行是否有0
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
                
        #第一列是否有0       
        for j in range(n):
            if matrix[0][j] == 0:
                first_row = True
                
        #把第一行或者第一列设置为标志位
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        #置0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    
        if first_row:
            for j in range(n):
                matrix[0][j] = 0
                
        if first_col:
            for i in range(m):
                matrix[m][0] = 0
    



                
import collections
   
class Solution2(object):
    def setmatrixZero2(self, matrix):
        m = len(matrix)
        n = len(matrix)
        
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append({i,j})
                    
        while q:
            p = q[-1]
            q.pop()
            
        for j in range(n):
            matrix[p.first][j] = 0
        for i in range(m):
            matrix[i][p.second] = 0
            

#用O(M+N)空间 此法为主
class Solution3(object):
    def setMatrixzero(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        row_zero = set()
        col_zero = set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)

        for i in range(row):
            for j in range(col):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0
                    
        
