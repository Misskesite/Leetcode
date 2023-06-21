# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:00:36 2020

@author: liuga
"""
#BFS
class Solution(object):
    def trappingWater(self, heightMap):
        m = len(heightMap)
        n = len(heightMap[0]) if m else 0
        peakMap = [[float('inf')]*n for _ in range(m)]
        queue = []
        
        for x in range(m):
            for y in range(n):  # 把矩形的四边入队
                if x in (0, m-1) or y in (0, n-1):
                    peakMap[x][y] = heightMap[x][y]
                    queue.append((x,y))
        
        while queue:
            x,y = queue.pop(0)
            for dx, dy in zip((1,0,-1,0),(0,1,0,-1)):
                nx,ny = x+dx, y+dy
                if nx<=0 or nx>=m-1 or ny <=0 or ny >=n-1:
                    continue  #在边界上，和在边界之外，不做操作
                limit = max(peakMap[x][y],heightMap[nx,ny])  
                if peakMap[nx][ny] > limit:
                    peakMap[nx][ny] = limit
                    queue.append((nx,ny))
        return sum(peakMap[x][y] - heightMap[x][y] for x in range(m) for y in range(n))
                    


#从最小的开始出队，所有的点均进出一次优先队列(堆) 复杂度O(m*n)log(m*n) 空间复杂度O(m*n)
import heapq

class Solution2(object):
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        res = 0

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1: #边界入queue
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i, j))
        
        while heap:
            bar = heapq.heappop(heap)

            for (delta_x, delta_y) in directions:
                next_x, next_y = bar[1] + delta_x, bar[2] + delta_y
                if self.is_valid(next_x, next_y, m, n, visited):
                    res += max(0, bar[0] - heightMap[next_x][next_y]) #出队元素(比如边界元素)是被更新的元素(next_x, next_y)的最小高度的邻点,邻居当前最小就能容纳水？
                    heapq.heappush(heap, (max(bar[0], heightMap[next_x][next_y]), next_x, next_y))#当前围栏的高度                                                                                             
                    visited.add((next_x, next_y))
        
        return res
    
    def is_valid(self, x, y, m, n, visited):
        return x >= 0 and x <= m-1 and y >= 0 and y <= n-1 and (x, y) not in visited
                   
''''
把最外围的一圈作为围栏， 选择一个最低的围栏， 如果这个围栏的邻节点都比它大， 此围栏可删除，邻节点作为新的围栏； 如果邻节点比它小， 那么邻节点可储蓄的水为 二者高度之差, 时在邻节点设置围栏，高度为当前围栏高度即可。
'''

#周围的高度都应该比当前的高度高，形成一个凹槽才能装水，而且装水量取决于周围最小的那个高度
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

	# Initial
	# Board cells cannot trap the water
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
			
	# Add Board cells first
        heap = []
        visited = set()
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i,j))
					
					
	# Start from level 0
        level, res = 0, 0
        while heap:	    
            height, x, y = heapq.heappop(heap)
            level = max(height, level)

            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n and (i, j) not in visited:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
					
		    # If cell's height smaller than the level, then it can trap the rain water
                    if heightMap[i][j] < level:
                        res += level - heightMap[i][j]
						
		    # Set the height to -1 if the cell is visited
                    visited.add((i,j))

        return res
