# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:05:37 2020

@author: liuga
"""
#此解法为主，对比下面，剪枝更多
import heapq
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        visited = {}
        visited[(start[0], start[1])] = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        heap = [(0, (start[0], start[1]))]
        while heap:
            distance, cur = heapq.heappop(heap)
            
            if cur == tuple(destination):
                return distance            
            
            for dx, dy in dirs:
                step = 0
                x = cur[0]
                y = cur[1]
                while x+dx < m and x+dx >= 0 and y+dy < n and y+dy >= 0 and maze[x+dx][y+dy] == 0:
                    x += dx
                    y += dy
                    step += 1       
                if (x,y) not in visited or visited[(x,y)] > distance+step:
                    visited[(x,y)] = distance + step         
                    heapq.heappush(heap, (distance+step, (x, y)))
            
        return -1
    
import heapq
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        visited = {} #pos:shortest distance
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        heap = [(0, (start[0], start[1]))] #这里一定加() initial start distance as 0
        while heap:
            distance, cur = heapq.heappop(heap)
            if cur in visited and visited[cur] <= distance: #prune paths where the distance to reach a cell is more than the current shortest distance
                continue
            if cur == tuple(destination):
                return distance
            visited[cur]= distance #shortest distance?
            
            for dx, dy in dirs:
                step = 0
                x = cur[0]
                y = cur[1]
                while x+dx < m and x+dx >= 0 and y+dy < n and y+dy >= 0 and maze[x+dx][y+dy] == 0:
                    x += dx
                    y += dy
                    step += 1                
                heapq.heappush(heap, (distance+step, (x, y)))
            
        return -1
            

       
class Soution2(object):
    def shortestDistance(self, maze, start, destination):      
            start, destination = tuple(start), tuple(destination)
            row, col = len(maze), len(maze[0])
            
            def neighbors(maze, node):
                temp = []
                used = set()
                used.add(node)
                for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                    (x,y), dist = node, 0
                    while 0 <= x+dx < row and 0 <= y+dy < col and maze[x+dx][y+dy] == 0:
                        x += dx
                        y += dy
                        dist += 1
                    if (x,y) not in used:
                        temp.append((dist, (x,y)))
                return temp
    
            heap = [(0, start)]
            visited = set()
            while heap:
                dist, node = heapq.heappop(heap)
                if node in visited: 
                    continue
                if node == destination:
                    return dist
                visited.add(node)
                for neighbor_dist, neighbor in neighbors(maze, node): #四个方向走到底的坐标，距离
                    heapq.heappush(heap, (dist+neighbor_dist, neighbor))
            return -1

#改写
def shortestDistance(self, maze, start, destination):
    if not maze:
        return False
    m, n = len(maze), len(maze[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    heap = []
    heapq.heappush(heap, [0, start[0], start[1]]) #heap = [(0, start[0], start[1])]
    visited = set()

    while heap:
        dist, x, y = heapq.heappop(heap)
        if (x,y) in visited:
            continue
        visited.add((x, y))
        if x == destination[0] and y == destination[1]:
            return dist

        for dx, dy in dirs: #每个方向走到底
            newx = x
            newy = y
            steps = 0 #这里每走一个方向，需要重置
            while 0 <= newx + dx < row and 0 <= newy + dy < col and maze[newx+dx][newy+dy] == 0:
                newx += dx
                newy += dy
                steps += 1
            if (newx ,newy) not in visited:
                heapq.heappush(heap, (dist + steps, newx, newy))
        return -1
            
                
