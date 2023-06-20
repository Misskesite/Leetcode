# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 10:05:43 2019

@author: liuga
"""
import collections
class Solution(object):
    def dfs(self, graph, visited, i):
        if visited[i] == 1: 
            return False
        if visited[i] == 2: 
            return True
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        visited[i] = 2
        return True
    
    def courseschedule(self, n, pre):
        graph = collections.defaultdict(list)
        for u, v in pre:
            graph[u].append(v)
        visited = [0] * n
    
        for i in range(n):
            if not self.dfs(graph, visited, i):
                return False
        return True

#此解法更简单    
#bfs 时间复杂度O(N+M)节点数和边数. 空间复杂度O(N+M),建立邻表需要的额外空间 adjancency长度为N，存储M条临时的边
from collections import deque

class Solution2(object):
    def canFinish(self, n, prerequisites):
        indegrees = [0]*n
        adjancency = [[] for _ in range(n)]
        
        queue = deque()
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjancency[pre].append(cur)
        
        for i in range(n):
            if indegrees[i] == 0:
                queue.append(i)
        #BFS Top sort
        while queue:
            pre = queue.popleft()
            n -= 1
            for cur in adjancency[pre]:
                indegrees[cur] -= 1
                if ndegrees[cur] == 0:
                    queue.append(cur)
        return not n
    
#dfs 对 numCourses 个节点依次执行 DFS，判断每个节点起步 DFS 是否存在环
class Solution3:
    def canFinish(self, numCourses, prerequisites):
        def dfs(i, adjacency, flags):
            if flags[i] == -1: #说明当前节点已被其它节点启动DFS访问，无需重复搜索
                return True
            if flags[i] == 1: #已被当前节点的DFS第二次访问，有环
                return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): 
                    return False
            flags[i] = -1     #复原？
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): 
                return False
        return True


                
                
