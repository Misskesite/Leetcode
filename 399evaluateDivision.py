# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:22:53 2020

@author: liuga
"""
#DFS
import collections

class Solution(object):
    def evaluateDivision(self, equations, values, queries):
        table = collections.defaultdict()
        for (x,y), value in zip(equations, values):
            table[x][y] = value
            table[y][x] = 1.0/value
        
        ans = [self.dfs(x, y, table, set()) if x in table and y in table else -1.0 for (x,y) in queries]
        '''
        ans = []
        
        for x, y in queries:
            visited = set()
            if x in table and y in table:
                ans.append(self.dfs(x, y, table, visited))
            else:
                ans.append(-1)

        '''
        return ans
    
    def dfs(self, x, y, table, visited):
        if x == y:
            return 1.0
        visited.add(x)
        for n in table[x]: #n 对应字典的key？
            if n in visited:
                continue
            visited.add(n)
            d = self.dfs(n, y ,table, visited)
            if d > 0:
                return d*table[x][n] #table[x][n]对应value
        return -1.0
        

#O(e+q) 看成一个图 顶点之间的权值是A/B
class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        #graph[A][B] := A/B
        graph = defaultdict(dict)
        
        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1/value

        def devide(A, C, visited):
            if A == C:
                return 1.0

            visited.add(A)

            # value := A / B
            for B, value in graph[A].items():
                if B in seen: #Seen来记录已经访问过的表达式，防止在DFS中走已经走过了的路
                    continue
                res = devide(B, C, visited)  # B / C
                if res > 0:  # valid
                    return value * res  # (A / B) * (B / C) = A / C

             return -1.0  # invalid

    for A, C in queries:
        if A not in graph and C not in graph:
            ans.append(-1.0)
        else:
            ans.append(devide(A, C, set()))

    return ans



#此解法为主
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        #graph[A][B] := A/B
        graph = defaultdict(dict)
        
        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1/value

        def devide(A, C, visited):
            if A == C:
                return 1.0
            for n in graph[A]:
                if n not in visited:
                    visited.add(n)
                    res = devide(n, C, visited)
                    if res > 0:
                        return res*graph[A][n]
            return -1.0
        
        for A, C in queries:
            if A not in graph or C not in graph:
                res.append(-1.0)
            else:
                res.append(devide(A, C, set()))

        return res
