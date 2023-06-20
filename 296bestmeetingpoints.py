# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:19:49 2020

@author: liuga
"""
#曼哈顿距离, 只要给位置排好序，然后用最后一个坐标减去第一个坐标，即CD距离，倒数第二个坐标减去第二个坐标，即AB距离
#二维是2个一维相加
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        row = []
        col = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    row.append(i)
                    col.append(j)
        col.sort()
        row.sort()
        res = 0 
        i = 0
        j = len(row)-1
        while i < j :
            res += row[j]- row[i] 
            j -= 1
            i += 1
        
        i = 0
        j = len(col)-1
        while i < j :
            res += col[j] - col[i]
            j -= 1
            i += 1
        return res
            
        
