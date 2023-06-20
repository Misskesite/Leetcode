# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 22:35:34 2020

@author: liuga
"""

class UnionFind():
    def _init_(self):
        self.parent = {}
        self.count = 0
        
    def find(self, p):
        while p != self.parent[p]:
            p = self.parent[p]

        return p

    def add_island(self, pos):
        if pos not in self.parent:
            self.parent[pos] = pos
            self.count += 1
            
    #把其中一个的根节点连接到另一个根节点上
    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp != rootq:
            self.parent[rootp] = self.parent[rootq]
            self.count -= 1

class Solution(object):
    def numIslands(self, m, n, positions):
        uf = UnionFind()
        ans = []
        for (r, c) in positions:
            uf.add_island((r, c))
            for neigh in [(r-1, c), (r+1, c), (r, c+1), (r, c-1)]:
                if neigh in uf.parent:
                    uf.union((r,c), neigh)

            ans.append(uf.count)
        return ans
        

    
#此解法为主
class Unionfind(object):
    def __init__(self):
        self.father = {}
        self.count = 0
                
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return
        else:
            self.father[pb] = pa
            self.count -= 1
            
    
    def find(self, x):
        while x != self.father[x]:
            x = self.father[x]
            
        return x  

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
       
        islands = set()
        res = []
        uf = Unionfind()
        
        for pos in positions:
            x = pos[0]
            y = pos[1]
            if (x, y) in islands:
                res.append(uf.count)
                continue
            
            islands.add((x, y))
            uf.father[(x, y)] = (x, y)
            uf.count += 1
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (nx, ny) in islands:
                    uf.union((x,y),(nx, ny))
            res.append(uf.count)
        return res


#hashmap,每个1的位置对应岛的id，如果连在一起，对应相同的id，否则对应不同的id。
#遍历每个位置，查看四个邻接的位置是都原本有岛，如果四个位置没有岛，当前位置自成一个岛，赋予新的id
#如果邻接位置与原本的岛相连，那么岛的总数不变，将当前位置赋予相连的岛的id
#如果邻接位置和2个，3个或者4个岛相连，那么岛的总数会相应的减少，需要将相连的几个岛合并这几个岛的任意id,同时将当前的位置赋予这个id
class Solution2(object):
    def numberIslands(self, m, n, positions):
         island_map = {}

         dirs = [[0,1], [0,-1], [-1, 0], [1, 0]]
         ans = []
         count = 0
         island_id = 0

         for pos in positions:
             if (pos[0], pos[1]) in island_map:
                  ans.append(count)
                  continue
             connected_island = set() #存的是岛id?
             for d in dirs:
                 x = pos[0] + d[0]
                 y = pos[1] + d[1]

                 if 0 <= x < m and 0 <= y < n and (x, y) in island_map:
                     connected_island.add(island_map[(x,y)])

              if len(connected_island) == 0:   #连接的4个位置没有岛?
                  island_map[(pos[0], pos[1])] = island_id
                  island_id += 1
                  count += 1
                  
              elif len(connected_island) == 1: #邻接位置原本有个岛
                  for _id in connected_islands:
                      island_map[(pos[0], pos[1])] = _id

              else:
                  for _id in connected_island: #邻接位置有2个以上的岛相连
                      new_id = _id             #任意取一个id?
                      break

                  for k, v in island_map.items():
                      if v in connected_island:
                          island_map[k] = new_id

                  island_map[(pos[0] ,pos[1])] = new_id
                  count = count - len(connected_island) + 1

             ans.append(count)

         return ans
            
