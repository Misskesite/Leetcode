# -*- coding: utf-8 -*-
"""
Created on Mon May 25 19:22:50 2020

@author: liuga
"""
#use template
import collections 
#求最短距离(曼哈顿距离只能沿着横、竖到达另外一个点走的步数)，BFS 找出每个0到1的距离,本题抽象为多个起始点的BFS
class Solution3(object):
    def updateMatrix(self, matrix):
        M, N = len(matrix), len(matrix[0])
        queue = collections.deque()
        visited = [[0] * N for _ in range(M)]
        res = [[0] * N for _ in range(M)]
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = 1
                    
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        step = 0
        while queue:
            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()
                if matrix[x][y] == 1:
                    res[x][y] = step
                    
                for dx, dy in dirs:
                    newx, newy = x + dx, y + dy
                    if newx < 0 or newx >= M or newy < 0 or newy >= N or visited[newx][newy] == 1: #先访问的距离更小
                        continue
                    queue.append((newx, newy))
                    visited[newx][newy] = 1
            step += 1
        return res


#此解法为主    
from collections import deque
class Solution2(object):
    def updateMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        res = matrix[:]
        
        q = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append([[i,j,0])
                    
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        while q:
            x0, y0, distance = q.popleft()
             
            if matrix[x0][y0] == 1:
                res[x0][y0] = distance
            
            for dx, dy in dirs:
                x = x0 + dx
                y = y0 + dy
                
                if 0 <= x < m and 0 <= y < n and visited[x][y] != 1:
                    q.append([[x,y], distance + 1])
                    visited[x][y] = 1
                
        return res
                
                 
#类似于286 比较简洁 省空间
class Solution(object):
    def updateMatrix(self, matrix):
        h = len(matrix)
        w = len(matrix[0])
        queue = deque()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for x in range(h):
            for y in range(w):
                if matrix[x][y] == 0:
                    queue.append((x,y))
                else:
                    matrix[x][y] = -1 #表示未被访问，只更新1的距离
                     
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < h and nx >= 0 and ny >= 0 and ny < w and matrix[nx][ny] == -1:
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append((nx,ny))
        return matrix
    

class Solution:
  def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                q.append((i, j))
            else:
                mat[i][j] = math.inf

    while q:
      i, j = q.popleft()
      for dx, dy in dirs:
        x = i + dx
        y = j + dy
        if x < 0 or x == m or y < 0 or y == n:
          continue
        if mat[x][y] <= mat[i][j] + 1:
          continue
        q.append((x, y))
        mat[x][y] = mat[i][j] + 1

    return mat  
