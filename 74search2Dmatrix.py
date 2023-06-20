# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:05:15 2019

@author: liuga
"""

class Solution(object):
    def search2Dmatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        #如果要搜索的 target 比当前元素大，那么让行增加，如果小，让列减小(从右上角开始搜索)
        while True:
            if row < rows and col >= 0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    row += 1
                else:
                    col -= 1
            else:
                return False

        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n-1
        while i < m and j >=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
