# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:19:31 2020

@author: liuga
"""
#DFS 求值为1的点的left most position, right most position, top most position, bottom most position
#时间复杂度O(m*n) 类似于暴力搜索法
class Solution(object):
    def smallestRectangle(self, grid, x, y):
        row = len(grid)
        col = len(grid[0])
        
        if row == 0 or col == 0:
            return 0
        visited = [[False]*col for _ in range(row)]
        left, up = 10000, 100000
        right, down = 0, 0
        for r in range(row):
            for c in range(col):
                self.dfs(grid, visited, r, c)
                
        return (right - left + 1)*(down - up + 1)
    
        def dfs(grid, visited, row, col):
            if row < 0 or row > len(grid) or col < 0 or col > len(grid[0]) or visited[row][col] or grid[row][col] == "0":
                return False
            
            #更新上下左右的值?
            left = min(left, col)
            right = max(right, col)
            up = min(up, row)
            down = max(down, row)

            visisted[row][col] = True
            
            dfs(grid, visited, row + 1, col)
            dfs(grid, visited, row - 1, col)
            dfs(grid, visited, row, col + 1)
            dfs(grid, visited, row, col - 1)

    #DFS更复杂，跟暴力搜索没有区别
        left, up = y, x
        right, down = y, x
        for i in range(row):
            for j in range(col):
                if image[i][j] == "1":
                    left = min(left, i)
                    right = max(right, j)
                    up = min(up, i)
                    down = max(down, i)
        return (right - left + 1)*(dowm - up + 1)


#Binary search, 以row search为例， 所有含有black pixel的column，映射到row x上时，必定是连续的,0到y里面搜索最左边含有black pixel的一列            
#接下来搜索上下和右边界，要找的是第一个'0'，传入一个变量判断 时间复杂度O(mlogn + nlogm) 空间复杂度O(1)
class Solution(object):
    def minArea(self, grid, x, y):
        if grid == 0 or grid[0] == 0:
            return 0

        row = len(grid)
        col = len(grid[0])

        #搜索右边界和下边界时，我们要找的是第一个0
        def binarySearch(self, gird, lo, hi, min, max, flagh, flagl):
            while  lo < hi:
                mid = lo + (hi - lo)/2
                blackPixel = False
                for i in range(min, max):
                    flagh == True ? grid[i][mid] : grid[mid][i] == '1'
                    if flagh == True:
                        blackPixel == True
                        break
                if blackPixel == flagl:
                    hi = mid
                else:
                    lo = mid + 1

            return lo
                    
        
        left = binarySearch(grid, 0, y, 0, row, True, True)
        right = binarySearch(grid, y+1, col, 0, row, True, False)
        top = binarySearch(grid, 0, x, left, right, False, True)
        bot = binarySearch(grid, x+1, row, left, right, False, False)
    
        return (right - left)*(bot - top)

#O(m*logn + n*logm)
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        def firstAnyone(l:int, r:int, allZeros: Callable[[int], bool]) -> int:
            while l < r:
                m = (l + r)//2
                if allZeros(m): 
                    l = m + 1
                else:
                    r = m
            return l

        def firstAllZero(l:int, r:int, allZeros: Callable[[int], bool]) -> int:
            while l < r:
                m = (l + r)//2
                if allZeros(m):
                    r = m
                else:
                    l = m + 1
            return l


        def colAllZeros(colIndex: int) -> bool:
            for i in range(len(image)):
                if image[i][colIndex] == "1":
                    return False
            return True
     

        def rowAllZeros(rowIndex: int) -> bool:
            for pixel in image[rowIndex]:
                if pixel == "1":
                    return False
            return True

        x1 = firstAnyone(0, x, rowAllZeros)
        x2 = firstAllZero(x+1, len(image), rowAllZeros)
        y1 = firstAnyone(0, y, colAllZeros)
        y2 = firstAllZero(y+1, len(image[0]), colAllZeros)

        return (x2-x1)*(y2-y1)
    


                    
                
        
#BFS
from collections import deque
class Solution(object):
    def minArea(self, grid, x, y):
        m = len(grid)
        n = len(grid[0])

        dirs = [(1,0), (-1,0),(0,1),(0, -1)]
        q = deque()
        q.append((x, y))

        grid[x][y] = '0'
        while q:
            i, j = q.popleft()
            x1 = min(x1, i)
            x2 = max(x2, i)
            y1 = min(y1, j)
            y2 = max(y2, j)
            for dir in dirs:
                nx = i + dir[0]
                ny = j + dir[1]
                if nx >= 0 and nx < m and ny < n and ny >= 0 and grid[nx][ny] == '1':
                    q.append((nx, ny))
                    grid[nx][ny] = '0' #访问过了

        return (x2- x1 +1)*(y2- y1+1)
                
        
