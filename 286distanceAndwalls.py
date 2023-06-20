# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 09:44:44 2019

@author: liuga
"""
#BFS 此法为主
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        q = deque()
        m = len(rooms)
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append([i,j,0])
                
        while q:
            x,y,d = q.popleft()
            for dx, dy in directions:
                newx = x + dx
                newy = y + dy
                if newx >=0 and newx < m and newy >= 0 and newy <n:
                    if rooms[newx][newy] == 2147483647:
                        rooms[newx][newy] = d + 1
                        q.append([newx, newy, d+1])
        
        
from collections import deque
#本题BFS更好，一层层的修改
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        q = deque([(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r]) #rooms[i][j] == 0
        while q:
            (i, j) = q.popleft()
            for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= I < len(rooms) and 0 <= J < len(rooms[0]) and rooms[I][J] == INF: # 应该不需要(rooms[I][J] > rooms[i][j] + 1?)，先被更新，距离值肯定更小
                   rooms[I][J] = rooms[i][j] + 1
                   q.append((I, J))　

#dfs找到离门更近的距离
    if not rooms:
            return []
        row = len(rooms)
        col = len(rooms[0])
        
        def dfs(x,y,dis):
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < row and 0 <= ny < col and rooms[nx][ny] > rooms[x][y]: 
                    rooms[nx][ny] = dis+1
                    dfs(nx,ny,dis+1)
        
        for x in range(row):
            for y in range(col):
                if rooms[x][y] == 0:
                    dfs(x,y,0)
