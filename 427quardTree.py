# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 21:24:55 2020

@author: liuga
"""

class Solution(object):
    def construct(self, grid):
        isleaf = self.isQuardTree(grid)
        n = len(grid)
        if isleaf == None:
            mid = n //2
            topleft = [[grid[i][j]for j in range(mid)] for i in range(mid)]
            topright = [[grid[i][j] for j in range(mid,n) for i in range(mid)]]
            botomleft = [[grid[i][j] for j in range(mid) for i in range(mid,n)]]
            botomright = [[grid[i][j] for j in range(mid,n) for i in range(mid,n)]]
            
            node = Node(True, False, self.construct(topleft), self.construct(topright),self.construct(bottomleft),self.construct(bottomright))
        elif isleaf == False:
            node = Node(False, True, None, None, None, None)
        else:
            node = Node(True, True, None, None, None, None)
        return node
    
    def isQuardTree(self, grid):
        n = len(grid)
        s = 0
        for i in range(n):
            s += sum(grid[i])
        if s == n*n:
            return True
        elif s == 0 :
            return False
        else:
            return None

def construct(self, grid):
	if not grid: return None
	if self.isLeaf(grid):
		return Node(grid[0][0] == 1, True, None, None, None, None)
	n = len(grid)
	return Node('*',
				False,
				self.construct([row[:n/2] for row in grid[:n/2]]),
				self.construct([row[n/2:] for row in grid[:n/2]]),
				self.construct([row[:n/2] for row in grid[n/2:]]),
				self.construct([row[n/2:] for row in grid[n/2:]]))

def isLeaf(self, grid):
    return all(grid[i][j] == grid[0][0] 
        for i in range(len(grid)) for j in range(len(grid[i])))

'''    
#Definition for a QuadTree Node   索引表示 left, (left+right)/2 , right
class Node:
    def _init_(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.lsLeaf = isLEaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
''''

class Solution2(object):
    def construct(self, grid):
        self.grid = grid
        return self.dfs(0 ,0 ,len(grid[0]))

    def dfs(self, row, col, n): #方格内全0或者全1，叶子节点，不会继续递归
        sum_val = sum(sum(e[col: col + n]) for e in self.grid[row: row + n])
        if n == 1 or sum_val in [n*n ,0]: #说明是quad tree?
            return Node(self.grid[row][col], 1, *[None]*4)
        n //= 2
        topLeft = self.dfs(row, col, n)
        topRight = self.dfs(row, col + n , n)
        bottomLeft = self.dfs(row + n, col, n)
        bottomRight = self.dfs(row + n, col + n, n)
        root = Node(1, 0, topLeft, topRight, bottomLeft, bottomRight)
        return root
            
        
