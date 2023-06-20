# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 23:43:01 2020

@author: liuga
"""

class UnionFind(object):
    def _init_(self, n):
        self.set = range(n)
        self.count = n
        
    def find_set(self,x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set(x))
        return self.set[x]
    
    def union_set(self,x,y):
        x_root, y_root = map(self.find_set,(x,y))
        if x_root != y_root:
            self.set[min(x_root,y_root)] = max(x_root. y_root)
            self.count -=1
            
class Solution(object):
    def countComponent(self, n, edges):
        union_find =  UnionFind(n)
        for i, j in edges:
            union_find.union_set(i,j)
        return union_find.count
    

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(0, n))
        self.rank = [1] * n
        self.cnt = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) #压缩？ 找grandparent
        return self.parent[x]
        '''
        res = x
        while res != parent(res):
            parent[res] = parent[parent[res]]
            res = parent[res]

        return res

        '''
        
    
    def merge(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:  #已经连接
            return
        
        if self.rank[px] > self.rank[py] :
            self.parent[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py] += self.rank[px]
                
        self.cnt -= 1
    
class Solution2:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        
        for e in edges :
            uf.merge(e[0], e[1])
        
        return uf.cnt


#BFS for each index, use BFS to find all the related numbers and append them to set. if index has no more related num, count+1, start from next index, if it is in set, skip to next index
    
from collections import defaultdict
class Solution2(object):
    def countComponent(self, n. edges):
        dic = defaultdict(list)
        for source, target in edges:
            dic[source].append(target)
            dic[target].append(source)
        count = 1

        visited = set()
        queue = collections.deque()
        for x in range(n):
            if x not in visited:
                continue
            queue.append(x)
            while queue:
                source = queue.popleft()
                if source in visited:
                    continue
                visited.add(source)
                for target in dic[source]:
                    queue.append(target)
            count += 1
        return count
            

#DFS 此解为主
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(u):            
            for v in pair[u]:
                if v not in visited:
                    visited.add(v)
                    dfs(v)
        pair = defaultdict(set)
        for u,v in edges:
            pair[u].add(v)
            pair[v].add(u)
        count = 0
        visited = set()
        for i in range(n):
            if i not in visited: 
                visited.add(i)               
                dfs(i)
                count += 1
        return count


class Solution:
  def countComponents(self, n: int, edges: List[List[int]]) -> int:
      ans = 0
      graph = [[] for _ in range(n)]
      seen = set()

      for u, v in edges:
          graph[u].append(v)
          graph[v].append(u)

      def dfs(u: int, seen: Set[int]) -> None:
          for v in graph[u]:
              if v not in seen:
                  seen.add(v)
                  dfs(v, seen)

     for i in range(n):
         if i not in seen:
            seen.add(i)
            dfs(graph, i, seen)
            ans += 1

       return ans
