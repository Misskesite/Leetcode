# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:34:54 2019

@author: liuga
"""

class Solution(object):
    def numberIslands(self, grid):
        if not gird:
            return 0
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    res += 1
        return res
        
    def dfs(self, grid, i, j):
        dirs = [[-1,0], [1,0], [0,-1],[0,1]] 
        grid[i][j]= "0"  #深度搜索中删除岛屿
        for dir in dirs:
            nr, nc = i + dir[0], j + dir[1]
            
            if nr < len(grid) and nc < len(grid[0]) and nr >=0 and nc >=0:
                if grid[nr][nc] == "1":
                    self.dfs(grid, nr, nc)
     #以此为准           
    def dfs2(self, grid, i, j):
        if i < 0 or i >= len(grid) or j <0 or j >= len(grid[0]) or grid[i][j] != "1":
            return 
        
        grid[i][j] = 2 # or 0
        self.dfs2(grid, i+1,j)
        self.dfs2(grid, i-1,j)
        self.dfs2(grid, i,j+1)
        self.dfs2(grid, i,j-1)
