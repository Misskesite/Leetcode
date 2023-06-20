# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:51:14 2020

@author: liuga
"""
#题目类似207
import collections
#连通图不能有环，题目变成了验证联通图是否有环
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n -1:
            return False
        lookup = collections.defaultdict(list)
        for n1, n2 in edges:
            lookup[n1].append(n2)
            lookup[n2].append(n1)
        visited = set()

        def dfs(i):
            if i in visited:
                return False
            visited.add(i)
            for j in lookup[i]:
                if j not in visited:
                    if not dfs(j):
                        return False
            return True
        return dfs(0) and len(visited) == n #有可能有孤独的一个点，有的边没有被访问
    
    
#global关键字修饰变量后标识该变量是全局变量，对该变量进行修改就是修改全局变量，而nonlocal关键字修饰变量后标识该变量是上一级函数中的局部变量
#global关键字可以用在任何地方，包括最上层函数中和嵌套函数中，即使之前未定义该变量，global修饰后也可以直接使用，而nonlocal关键字只能用于嵌套函数中，并且外层函数中定义了相应的局部变量，否则会发生错误
class Solution2(object):
    def gravalidTree(self, n, edges):
        graph = collections.defaultdict()
        l = len(edges)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        visited = set()
        
        def dfs(i):
            nonlocal l   #nonlocal 只在闭包里面生效，外函数内函数都受影响，闭包外面不影响
            visited.add(i)
            for j in graph(i):
                if j not in visited:
                    l -= 1
                    dfs(j)
        dfs(0)
        return len(visited) == n and l == 0 #边个数相等
    
#bfs O(n) we use BFS start from a certain node and find all related to this node and append them to the visited set.
#If the final size of the visited set is not equal to the number of nodes. That means there are more than 1 graph can be built by given input
from collections import deque
class Solution3(object):
    def gravalidTree(self, n, edges):
        if len(edges) != n-1:
            return False
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue = deque([0])
        visited = set()
        while queue:
            u = queue.popleft()
            visited.add(u)
            for v in graph[u]:                
                if v not in visited:
                    queue.append(v)
                    visited.add(v)
                #else: return False #已经存在，说明有重复边？返回false
        return len(visited) == n        


#并查集 union find
class Solution(object):
    def validTree(self, n, edges):
        if n -1 != len(edges):
            return False

        self.father = [i for i in range(n)]
        self.size = n

        for a, b in edges:
            self.union(a,b)
            
        return self.size == 1

    def union(self, a ,b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.size -= 1
            self.father[root_a] = root_b

    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]

        for n in path:
            self.father[n] = node

        return node
        
    
