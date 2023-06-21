# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:24:22 2020

@author: liuga
"""
#DFS更简单一些， while循环一直走，走到撞墙

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        row, col = len(maze), len(maze[0])
        visited = set()
        dirs = [(1,0),(0,1),(-1,0),(0, -1)]

        def dfs(x,y):
            if [x,y] == destination:
                return True
            if (x,y) in visited:
                return False
            visited.add((x,y))
            for dx, dy in dirs:
                newx, newy = x, y
                while newx + dx < row and newx + dx >= 0  and newy + dy < col and newy + dy >= 0 and maze[newx+dx][newy+dy] == 0: 
                    newx += dx
                    newy += dy
                if dfs(newx, newy):
                    return True
            return False
        
        
        return dfs(start[0], start[1])
        
                    

#BFS 
import collections 
class Solution2(object):
    def hasPath(self, maze, start, destination):
        m = len(maze)
        n = len(maze[0])
        dirs = [(1,0),(-1,0),(1,0),(-1,0)]
        q = deque([(start[0], start[1])])
        seen = {(start[0], start[1])}

        def isValid(x: int, y: int) -> bool:
            return 0 <= x < m and 0 <= y < n and maze[x][y] == 0

        while q:
            i, j = q.popleft()
            for dx, dy in dirs:
                x = i
                y = j
                while isValid(x + dx, y + dy):
                  x += dx
                  y += dy
                if [x, y] == destination:
                  return True
                if (x, y) in seen:
                  continue
                q.append((x, y))
                seen.add((x, y))

        return False

    

class Solution3(object):
    def hasPath(self, maze, start, destination):
        row = len(maze)
        col = len(maze[0])
        q = collections.deque([(start[0], start[1])])
        
        visited = set()
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        
        def neighbors(x,y):
            temp = []
            used = set()
            used.add((x,y))
            
            for dx, dy in dirs:
                nx, ny = x, y
                while 0 <= nx+dx < row and 0 <= ny+dy < col and maze[nx+dx][ny+dy] == 0:
                    nx+=dx
                    ny+=dy
                if (nx,ny) not in used:
                    temp.append((nx, ny))
            return temp
        
        while q:
            cell = q.popleft()
            if cell in visited:
                continue
            if cell == (destination[0], destination[1]):
                continue
            
            visited.add(cell)
            for neighbor in neighbors(cell[0],cell[1]):
                q.append(neighbor)
        return False
            
