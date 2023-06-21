# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:13:12 2020

@author: liuga
"""
#DFS
class Solution(object):
    def pacificWater(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        pv = [[False]*n for _ in range(m)]
        av = [[False]*n for _ in range(n)]
        
        for i in range(m):
            self.dfs(pv,m,n,i,0)
            self.dfs(av,m,n,i,n-1)
        for j in range(n):
            self.dfs(pv,m,n,0,j)
            self.dfs(pv,m,n,m-1,j)
        
        res = []
        for i in range(m):
            for j in range(n):
                if pv[i][j] and av[i][j]:
                    res.append([i,j])
        
        return res
    
    def dfs(self, visited, matrix, m, n, i, j):
        visited[i][j] = True
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for dire in directions:
            x, y = i + dire[0], j + dire[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(visited, matrix, m, n, x, y)
            

#BFS, set是一个无序且不重复的元素集合, set和dict一样，只是没有value，相当于dict的key集合
class Solution(object):
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        P = deque()
        A = deque()
        m, n = len(heights), len(heights[0])

        #四条边的点入队列
        for i in range(m):
            P.append((i, 0))
            
        for j in range(n):
            P.append((0, j))
            
        for i in range(m-1, -1, -1):
            A.append((i, n-1))
            
        for j in range(n):
            A.append((m-1, j))
          
        visited = set(P)
        while P:
            N = len(P)
            for _ in range(N):
                i, j = P.popleft()
                for x, y in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]:
                    
                    if 0 <= x < m and 0 <= y < n and (x,y) not in visited and heights[x][y] >= heights[i][j]:
                        visited.add((x,y))
                        P.append((x,y))

                     
        visited2 = set(A)
        res = [list(x) for x in visited2 if x in visited]
        while A:
            N = len(A)
            for _ in range(N):
                i, j = A.popleft()
                for x, y in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]:
                    if 0<= x < m and 0 <= y< n and (x,y) not in visited2 and heights[x][y]>= heights[i][j]:
                        visited2.add((x,y))
                        if (x,y) in visited:
                            res.append([x,y])
                        A.append((x,y))
        return res
    
#BFS改写 此方法为准？
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        P = deque()
        A = deque()
        m, n = len(heights), len(heights[0])
        dirs = [(0, -1),(-1, 0),(0, 1),(1, 0)]

        for i in range(m):
            P.append((i, 0))
            A.append((i, n-1))

        for j in range(n):
            P.append((0, j))
            A.append((m-1,j))

        visitP = set(P)
        visitA = set(A)

        def bfs(q, visit):
            while q:
                for _ in range(len(q)): #可以省略？
                    i, j = q.popleft()
                    for dir in dirs:
                        x = i + dir[0]
                        y = j + dir[1]
                        if 0 <= x < m and 0 <= y < n and (x,y) not in visited and heights[x][y] >= heights[i][j]:
                            visit.add((x,y))
                            q.append((x,y))
        bfs(P, visitP)
        bfs(A, visitA)
        return [[i, j] for i in range(m) for j in range(n) if (i, j) in visitP and (i, j) in visitA]
                    
            
            
    
#DFS
#从太平洋和大西洋边界位置出发遍历，同时被它们两遍历到的(重合的点) 按照高度找下一个大于此时遍历的点
#从四个边像中间找，找到重合的点
class Solution2(object):
    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]: 
            return []
        # 流向太平洋的位置
        res1 = set()
        # 流向大西洋的位置
        res2 = set()
        
        row = len(matrix)
        col = len(matrix[0])

        
        def dfs(i, j, cur, res):
            res.add((i, j))
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                ni = i + dx
                nj = j + dy
                if 0 <= ni < row and 0 <= nj < col and matrix[i][j] <= matrix[ni][nj] and (ni, nj) not in res: 
                    dfs(ni, nj, matrix[i][j], res)
                    
        # 从四条边的边界开始遍历
        # 太平洋
        for i in range(row):
            dfs(i, 0, 0, res1)
        # 太平洋
        for j in range(col):
            dfs(0, j, 0, res1)
        # 大西洋
        for i in range(row):
            dfs(i, col - 1, 0, res2)
        # 大西洋
        for j in range(col):
            dfs(row - 1, j, 0, res2)

        return res1 & res2


class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    m = len(heights)
    n = len(heights[0])
    seenP = [[False] * n for _ in range(m)]
    seenA = [[False] * n for _ in range(m)]

    def dfs(i: int, j: int, h: int, seen: List[List[bool]]) -> None:
      if i < 0 or i == m or j < 0 or j == n:
        return
      if seen[i][j] or heights[i][j] < h:
        return

      seen[i][j] = True
      dfs(i + 1, j, heights[i][j], seen)
      dfs(i - 1, j, heights[i][j], seen)
      dfs(i, j + 1, heights[i][j], seen)
      dfs(i, j - 1, heights[i][j], seen)

    for i in range(m):
      dfs(i, 0, 0, seenP)
      dfs(i, n - 1, 0, seenA)

    for j in range(n):
      dfs(0, j, 0, seenP)
      dfs(m - 1, j, 0, seenA)

    return [[i, j]
            for i in range(m)
            for j in range(n)
            if seenP[i][j] and seenA[i][j]]
