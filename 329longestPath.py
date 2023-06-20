# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:56:11 2020

@author: liuga
"""
#不需要进行visit状态的记录，因为只有邻居比自己大的时候才会进行搜索；搜索沿途记录路径长度即可。
#不会返回前置节点，和该节点的前置节点有任何交集
#Time O(m*n)
class Solution(object):
    def longestPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        cache = [[0]*n for _ in range(m)] #记录每个节点的最长路径
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, cache, m, n, i, j))
        return res
    
    def dfs(self, matrix, cache, m, n, i, j):
        if cache[i][j] != 0:
            return cache[i][j]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        res = 1         #每个节点初始路径为1
        for dir in directions:
            x = i + dir[0]
            y = j + dir[1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]: #邻居比自己大的时候搜索
                continue
            res = max(res, 1 + self.dfs(matrix, cache, m, n, x, y))
        cache[i][j] =  res
        return cache[i][j]
            
   
#dp[i][j] = 1 + max(dp[i - 1][j], dp[i + 1][j], dp[i][j - 1], dp[i][j + 1])
#时间复杂度O(m*n)
class Solution2(object):
    
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        
        @lru_cache(None) #用作缓存，反复调用相同参数的函数，是不会再次执行，而是直接返回函数之前的执行结果，大大优化了算法执行时间
        def dfs(row, column):
            res = 1
            DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in DIRS:
                newRow, newColumn = row + dx, column + dy
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[row][column]:
                    res = max(res, dfs(newRow, newColumn) + 1)
            return res

        ans = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))
        return ans


import functools
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dfs(x, y):
            length = 1
            for r, c in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                if 0 <= r < m and 0 <= c < n and matrix[x][y] < matrix[r][c]:
                    length = max(length, dfs(r, c) + 1)
            return length

        if not any(matrix): return 0
        m, n = len(matrix), len(matrix[0])
        return max(dfs(i, j) for i in range(m) for j in range(n))
    

#拓扑排序 O(m*n)
from collections import deque
class Solution3(object):
    
    def longestIncreasingPath(self, matrix):
        
        f not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        outdegrees = [[0]*n for _ in range(m)] #这里是出度，如果是入度，则计算周围比它小的个数
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                for dx, dy in directions:
                    newRow = i + dx
                    newColumn = j + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[i][j]:
                        outdegrees[i][j] += 1
                if outdegrees[i][j] == 0:
                    queue.append((i, j))

        ans = 0
        while queue:
            ans += 1
            size = len(queue)
            for _ in range(size): #一层一层的出列
                row, col = queue.popleft()
                for dx, dy in directions:
                    newRow, newCol = row + dx, col + dy
                    if 0 <= newRow < m and 0 <= newCol < n and matrix[newRow][newCol] < matrix[row][col]:
                        outDegrees[newRow][newCol] -= 1
                        if outDegrees[newRow][newCol] == 0:
                            queue.append((newRow, newCol))
        return ans 
                        

        
