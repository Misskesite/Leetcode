# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:56:04 2020

@author: liuga
"""

class Solution(object):
    def islandParemeter(self, grid):
        m = len(grid)
        n = len(grid[0])
        counts = 0
        neighbors  = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    counts += 1
                    if i < m-1:
                        if grid[i+1][j]==1:
                            neighbors +=1
                        
                    if j < n-1:
                        if grid[i][j+1] ==1:
                            neighbors +=1
                            
        return 4*counts - 2*neighbors
                            
