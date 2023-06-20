# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:47:07 2020

@author: liuga
"""
#利用已经搜索过的信息 时间复杂度O(m*n) 空间复杂度O(n)碰到墙，重新计算(为0？)
class Solution(object):
    def maxkillenemy(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return
        row = len(grid)
        col = len(grid[0])
        rowHits = 0       #rowCnt 变量，用来记录到下一个墙之前的敌人个数
        colHits = [0]*col #遍历顺序决定的，逐行遍历
        ans = 0
        for i in range(row):
            for j in range(col):
                if i == 0 or grid[i-1][j] == "W": #上一行位置是墙？
                    colHits[j] = 0 #colHits[j] 表示j列到下一个墙之前的敌人个数
                    for k in range(i, row): #剩余行，下方的行到墙或者边界
                        if grid[k][j] != "W":
                            colHits[j] += (grid[k][j] == "E")
                
                if j == 0 or grid[i][j-1] == "W":
                    rowHits = 0 #临时变量记录值？
                    for k in range(j, col):
                        if grid[i][k] != "W":
                            rowHits += (grid[i][k] == "E")
                if grid[i][j] == 0: #可以放炸弹
                    ans = max(ans, colHits[j] + rowHits)
        return ans


class Solution:
  def maxKilledEnemies(self, grid: List[List[chr]]) -> int:
    m = len(grid)
    n = len(grid[0])
    enemyCount = 0
    # dp[i][j] := max enemies grid[i][j] can kill
    dp = [[0] * n for _ in range(m)]

    def update(i: int, j: int) -> None:
      nonlocal enemyCount
      if grid[i][j] == '0':
        dp[i][j] += enemyCount
      elif grid[i][j] == 'E':
        enemyCount += 1
      else:  # grid[i][j] == 'W'
        enemyCount = 0

    # Extend four directions, if meet 'W', need to start over from 0
    for i in range(m):
      enemyCount = 0
      for j in range(n):
        update(i, j)
      enemyCount = 0
      for j in reversed(range(n)):
        update(i, j)

    for j in range(n):
      enemyCount = 0
      for i in range(m):
        update(i, j)
      enemyCount = 0
      for i in reversed(range(m)):
        update(i, j)

    # Returns sum(map(sum, dp))
    return max(map(max, dp))

#此法为主    
#O(m*n) 空间复杂度比较大， 每个位置，从左上角到它，然后右下角到它
class Solution2(object):
    def maxkillenemy(self, grid):
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        ans = 0
        arr = [[0]*col for i in range(row)]

        #left to right
        for i in range(row):
            count = 0
            for j in range(col):
                if grid[i][j] == "E": #遇到E递增
                    count += 1
                elif grid[i][j] == "W":
                    count = 0
                else:
                    arr[i][j] += count #遇到0 加到arr

        #right to left
        for i in range(row):
            count = 0
            for j in range(col-1, -1, -1):
                if grid[i][j] == "E": 
                    count += 1
                elif grid[i][j] == "W":
                    count = 0
                else:
                    arr[i][j] += count 

        #from up to down
        for j in range(col):
            count = 0
            for i in range(row):
                if grid[i][j] == "E": 
                    count += 1
                elif grid[i][j] == "W":
                    count = 0
                else:
                    arr[i][j] += count

        #from down to up
        for j in range(col):
            count = 0
            for i in range(row-1, -1, -1):
                if grid[i][j] == "E": 
                    count += 1
                elif grid[i][j] == "W":
                    count = 0
                else:
                    arr[i][j] += count
                    ans = max(ans, arr[i][j])

        return ans
                
