# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:42:42 2020

@author: liuga
"""
class Solution:
  def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
      ans = "impossible"
      minSteps = math.inf

      def dfs(i: int, j: int, dx: int, dy: int, steps: int, path: str):
          nonlocal ans
          nonlocal minSteps
          if steps >= minSteps:
            return

          if dx != 0 or dy != 0:  # Both are zero for the initial ball position
              while 0 <= i + dx < len(maze) and 0 <= j + dy < len(maze[0]) and maze[i + dx][j + dy] != 1:
                i += dx
                j += dy
                steps += 1
                if i == hole[0] and j == hole[1] and steps < minSteps:
                    minSteps = steps
                    ans = path

          if maze[i][j] == 0 or steps + 2 < maze[i][j]:
              maze[i][j] = steps + 2  # +2 to because of maze[i][j] == 0 || 1
              if dx == 0:
                  dfs(i, j, 1, 0, steps, path + 'd')
              if dy == 0:
                  dfs(i, j, 0, -1, steps, path + 'l')
              if dy == 0:
                  dfs(i, j, 0, 1, steps, path + 'r')
              if dx == 0:
                  dfs(i, j, -1, 0, steps, path + 'u')

      dfs(ball[0], ball[1], 0, 0, 0, '')
      return ans
                    
#此解法为主 让球在最小步数内滚到陷阱之中，此时返回的并不是最小步数，而是滚动的方向
class Solution(object):
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        dirs = [(0, 1, 'r'), (0, -1,'l'), (1, 0, 'd'), (-1, 0, 'u')]
        heap = [(0, "", ball[0], ball[1])]
        distance = collections.defaultdict()
        distance[(ball[0], ball[1])] = [0 , ""]

        while heap:
            dist, pattern, i, j = heapq.heappop(heap)
            if [i, j] == hole:
                return pattern
            for dx, dy, dr in directions:
                step, x, y = dist, i, j
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x+dx][y+dy] != 1:
                    x += dx
                    y += dy
                    step += 1

                    if [x ,y] == hole: #如果碰到孔，跳出到下一步检查距离。 505题终点是墙，所以不需要这一步
                        break

                if (x, y) not in distance or [step, pattern + dr] < distance[(x,y)]: #这里相比505多了一个字母序更小，也入队
                    distance[(x,y)] = [step, pattern + dr]
                    heapq.heappush(heap, (step, pattern + dr, x, y))
        return 'impossible'
        
                
from collections import deque            
class Solution(object):
    direct = {'d':(1,0), 'u':(-1,0), 'l':(0, -1), 'r':(0, 1)}
    def findShortestWay(self, maze, ball, hole):
        disntance = [[(float'inf'),'') for _ in range(len(maze(0))] for _ in range(len(maze))]

        distance[ball[0]][ball[1]] = (0 , '')
        que = deque()
        que.append((ball[0], ball[1]))

        while que:
            x, y  = que.popleft()
            for d in direct.keys():
                dx, dy = direct[d]
                nx, ny = x, y
                step = 0
                while self.valid(maze, nx + dx, ny + dy):
                    nx += dx
                    ny += dy
                    step += 1
                    if nx == hole[0] and ny == hole[1]: #遇到洞，更新距离入队
                        self.check(maze, d, step, x, y, nx, ny, distance, que) #这里可以直接用beak? 
                self.check(maze, d, step, x, y, nx, ny, distance, que) #没有遇到洞，撞到墙，也更新距离 入队
        if distance[hole[0]][hole[1]][1] == '':
            return 'impossible'

        return distance[hole[0]][hole[1]][1]

    def valid(self, maze, x, y):
        if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
            return False
        return maze[x][y] == 0

    def check(maze, d, step, x, y, nx, ny, distance, que): #类似于剪枝，距离更小或者距离相等，字母顺序更小
        if distance[x][y][0] + step < distance[nx][ny][0] or (distance[x][y][0] + step == distance[nx][ny][0] and distance[x][y][1] + d < distance[nx][ny][1]):
            disntance[nx][ny] = (distance[x][y][0] + step, distance[x][y][1] + d)
            queue.append((nx, ny))

from collections import deque
class Solution3(object):
    def findShortestWay(self, maze, hole, ball):
        m = len(maze)
        n = len(maze(0)
        disntance = [[float('inf') for _ in range(len(maze[0]))] for _ in range(len(maze))]
        mp = {}
        dirs = [[1,0], [-1,0], [0,1] , [0,-1]]
        way = ['u', 'd', 'r', 'l']
        q = deque((ball[0], ball[1]))
        distance[ball[0]][ball[1]] = 0
        while q:
            x, y = q.popleft()
            for i in range(4):
                dist = distance[x][y]
                path = mp[x*n + y]
                while  0 =< x  < m and 0 =< y < n and maze[x][y] == 0 and !(x == hole[0] and y == hole[1]):
                    x += dir[i][0]
                    y += dir[i][1]
                    dis += 1
                if x != hole[0] or y != hole[1]:
                    x -= dirs[i][0]
                    y -= dirs[i][1]
                    dist -= 1
                path.append(way[i])
                if distance[x][y] > dist:
                    dist = distance[x][y]
                    mp[x*n + y] = path
                    if x != hole[0] or y != hole[1]: #对于不是陷阱的点，我们加入队列queue中继续滚
                        q.append((x, y))
                elif distance[x][y] == dist and mp[x*n + y] > path: #步数相等，新的滚法字母顺序小
                    mp[x*n + y] = path
                    if x != hole[0] or y != hole[1]:
                        q.append((x, y))
            res = mp[hole[0]*n + hole[1]]
            return "impossible" if not res else res
                    
'''
dists[i][j]表示到达(i,j)这个位置时需要的最小步数,在后在遍历的过程中不断用较小值来更新每个位置的步数值
                
                
                
            
        
        
