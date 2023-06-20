# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:52:23 2019

@author: liuga
"""
#BFS 的重点在于队列，而 DFS 的重点在于递归。这是它们的本质区别
#DFS 从起点出发，把一个方向的点遍历完才改变方向，BFS 常用于找单一的最短路线，它的特点是 "搜到就是最优解"，而 DFS 用于找所有解的问题

#寻找和边界不连通的O,或者连通的O(运用DFS,BFS)
#BFS
from collections import deque
class Solution(object):
    def surroundRegion(self, board):
        if not board:
            return
        row, col = len(board), len(board[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        q = deque()
        
         # get the index of all O on the boarder
        for r in range(row):
            for c in range(col):
                if r in [0 , row-1] or c in [0, col-1] and board[r][c] == 'O':
                    q.append(r, c)
                    board[x][y] = 'A'
                
        # bfs, make the adjacent O into A
        while q:
            x, y = q.popleft()
            for d in directions:
                newx, newy = x + d[0], y + d[1]
                if newx < 0  and newx >= row and newy < 0 and newy >= col or board[x][y] != 'O':
                    continue
                    q.append((newx, newy))
                    board[newx][newy] = 'A'
                
            
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'A':
                    board[r][c] = 'O'


#DFS 时间复杂度O(m*n) 空间复杂度O(m*n)
class Solution(object):
    def solve(self, board):
        if not board:
            return
        n, m = len(board), len(board[0])

        def dfs(x, y):
            if not 0<= x < n or not 0 <= y < m or board[x][y] != 'O':
                return

            board[x][y] = "A"  
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            
        #遍历每一个矩阵边上的点, 把所有的O改成 A
        for i in range(n):
            for j in range(m):
                if i * j == 0 or i == m - 1 or j == n - 1:
                    dfs(i, j)
        '''
        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)

        for i in range(m):
            dfs(0, i)
            dfs(n-1, i)
        '''

        #把标记的，没有被包围的O从A改回O, 被包围的O改成X
        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] == "X"
                
        
