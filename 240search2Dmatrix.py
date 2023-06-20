# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:41:04 2020

@author: liuga
"""

class Solution(object):
    def search2dmatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        while 0 =< row < rows and 0 =< col < cols:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target: #排除一行，一列
                    row += 1
                else:
                    col -= 1
            else:
                return False
            
                
#从矩阵右上角开始搜索 时间复杂度O(m+n)
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n-1
        while i < m and j >=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target: # 排除一行
                i += 1
            elif matrix[i][j] > target: # 排除一列
                j -= 1
        return False
        
