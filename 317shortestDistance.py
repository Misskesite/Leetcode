# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 20:56:34 2020

@author: liuga
"""
#building比空地少，从building出发，找到每个空地与building的距离
class Solution(object):
    def shortestDistance(self, grid):
        
        def bfs(grid, dists, cnts, x, y):
            
            dist, m, n = 0, len(grid), len(grid[0])
            visited = [[False for i in range(n)] for j in range(m)]
            
            q = [(x,y)]
            visited[x][y]= True
            while q:
                dist +=1
                cur_level = []
                for i,j in q:
                    for dir in [(-1,0),(1,0),(0,1),(0,-1)]:
                        ni = i + dir[0] 
                        nj = j + dir[1]
                        if 0 <= ni <m and 0 <= nj <n and grid[ni][nj] == 0 and not visited[ni][nj]:
                            cnts[ni][nj] += 1 #cnt表示某个位置已经计算过的建筑数
                            dists[ni][nj] += dist
                            cur_level.append((ni,nj))
                            visited[ni][nj] = True
                q = cur_level
        '''
        def bfs(grid, dists, cnts, x, y):
            visited = [[False for i in range(n)] for j in range(m)]
            q = collections.deque()
            q.append((x,y,1))

            dirs = [(-1,0),(1,0),(0,1),(0,-1)]

            while q:
                i,j,dis = q.popleft()
                for d in dirs:
                    ni = i + d[0]
                    nj = j + d[1]
                    if 0 <= ni <m and 0 <= nj <n and grid[ni][nj] == 0 and not visited[ni][nj]:
                        dists[ni][nj] += dis
                        cnts[ni][nj] += 1
                        q.append((ni,nj,dis+1))
                        visited[ni][nj] = True


        '''
        
        m = len(grid)
        n = len(grid[0])
        build_num = 0
        dists = [[0 for _ in range(n)] for _ in range(m)]
        cnts = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==1:
                    build_num +=1
                    bfs(grid, dists, cnts, i ,j)
                    
        shortest = float("inf")
        for i in range(m):
            for j in range(n):
                if dists[i][j] < shortest and cnts[i][j]== build_num:
                    shortest = dists[i][j]
                    
        if shortest != float("inf"):
            return shortest  
        else:
            return -1
                
    
#BFS O(m*2 n*2) BFS的特性使得其非常适合建立距离场，
import deque
        
class Solution2(object):
    def shortestDistance(self, grid):
        row = len(grid)
        col = len(grid[0])
        
        distance = [[[0,0] for i in range(row)] for j in range(col)]
        homes = set()
        zero_loc  = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    homes.add((i,j))
                    distance[i][j][0] = -1
                elif grid[i][j] == 0:
                    zero_loc += 1
        if not zero_loc:
            return -1
        
        def bfs(i,j):
            step  = 0
            queue = deque([(i,j)])
            visited = set([(i,j)])
            while queue:
                n = len(queue)
                for _ in range(n):
                    i,j = queue.pop()
                    distance[i][j][0] += 1
                    distance[i][j][1] += step
                    for x, y in [[0,-1], [-1,0],[0,1],[1,0]]:
                        tmp_i = i + x
                        tmp_j = j + y
                        if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == 0 and (tmp_i, tmp_j) not in visited:
                            visited.add((tmp_i,tmp_j))
                            queue.appendleft((tmp_i, tmp_j))
                step += 1
        
        for i, j in homes:
            bfs(i,j)
        return min([b for dis in distance for a, b in dis if a == len(homes)] or [-1])
                        
            

class Solution:
  def shortestDistance(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    dirs = [0, 1, 0, -1, 0]
    nBuildings = sum(a == 1 for row in grid for a in row)
    ans = math.inf
    # dist[i][j] := total distance of grid[i][j] (0) to reach all buildings (1)
    dist = [[0] * n for _ in range(m)]
    # reachCount[i][j] := # Of buildings (1) grid[i][j] (0) can reach
    reachCount = [[0] * n for _ in range(m)]

    def bfs(row: int, col: int) -> bool:
      q = deque([(row, col)])
      seen = {(row, col)}
      depth = 0
      seenBuildings = 1

      while q:
        depth += 1
        for _ in range(len(q)):
          i, j = q.popleft()
          for k in range(4):
            x = i + dirs[k]
            y = j + dirs[k + 1]
            if x < 0 or x == m or y < 0 or y == n:
              continue
            if (x, y) in seen:
              continue
            seen.add((x, y))
            if not grid[x][y]:
              dist[x][y] += depth
              reachCount[x][y] += 1
              q.append((x, y))
            elif grid[x][y] == 1:
              seenBuildings += 1

      # True if all buildings (1) are connected
      return seenBuildings == nBuildings

    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:  # Bfs from this building
          if not bfs(i, j):
            return -1

    for i in range(m):
      for j in range(n):
        if reachCount[i][j] == nBuildings:
          ans = min(ans, dist[i][j])

    return -1 if ans == math.inf else ans       
        
            
                    
                
#O(m*2 n*2)
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        buildings = []
        candidate_lands = {} # {position, distance}

        # 1. Find all buildings and candidate empty lands
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    buildings.append((r, c))

                elif grid[r][c] == 0:
                    candidate_lands[(r, c)] = 0

        # 2. Compute min distance from each building to all candidate empty lands
        for building_position in buildings:
            self.bfs(candidate_lands, building_position)

        return min(candidate_lands.values()) if buildings and candidate_lands else -1
    
    def bfs(self, candidate_lands: dict, position: (int, int)):
        distance = 0
        visited = set()

        # 1. BFS:  bfs traversal makes it possible to avoid storing the distance for each node
        q = deque()
        q.append(position)
        while q:
            distance += 1
            n = len(q)
            for _ in range(n):
                position = q.popleft()
                for dir in [[0,-1], [-1,0], [0,1], [1,0]]:
                    adj_position = (position[0] + dir[0] ,position[1] + dir[1])

                    if adj_position in candidate_lands and adj_position not in visited:
                        candidate_lands[adj_position] += distance
                        
                        visited.add(adj_position)
                        q.append(adj_position)
            

        # 2. All empty lands that are not reachable from a building are excluded
        if len(visited) != len(candidate_lands):
            for position in set(candidate_lands.keys()).difference(visited):
                candidate_lands.pop(position)
                
        
        
        
