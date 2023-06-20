# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 23:26:02 2020

@author: liuga
""" any connected graph without simple cycles is a tree
#BFS 把所有的叶子节点放入队列中，然后同时向中间遍历，这样最后剩下来的就是整棵树中间的元素
#要树的高度最矮，根节点越靠近中间越矮。叶子节点为根节点的树都很高，从叶子节点往中间夹逼，广度搜索每次从叶子节点往里搜索
import collections

class Solution(object):
    def findminHeight(self, n, edges):
        if n == 1:
            return [0]
        leaves = collections.defaultdict(set)
        for u, v in edges:
            leaves[u].add(v)
            leaves[v].add(u)
        
        que = collections.deque()
        for u, vs in leaves.items():
            if len(vs) == 1:  #无向图度为1(跟顶点连接的边的个数)
                que.append(u) #叶子节点入队
            
        while n > 2: #最后结束的标准是，整个图只留下了1个或者两个元素
            _len = len(que)
            n -= _len  # 一次减去当前队列这么多个结点(叶子节点)
            for _ in range(_len):
                u = que.popleft()
                for v in leaves[u]:
                    leaves[v].remove(u)
                    if len(leaves[v]) == 1:
                        que.append(v)
        return list(que)
    

    #用list保存最后的一层节点？ 从两边向中间靠拢，相当于中间的节点把距离二分了,这样高度最小
    def findminHeight(self, n, edges):
        if n == 1:
            return [0]
        
        mp = collections.defaultdict(set)
        degrees = [0]*(n+1)
        for u, v in edges:
            mp[u].add(v)
            mp[v].add(u)
            degree[u] += 1
            degree[v] += 1

        que = collections.deque()
        for i in range(n):
            if degree[i] == 1:  #无向图度为1
                que.append(i) #叶子节点入队

        while que:
            res = []
            size = len(que)
            for i in range(size):
                u = que.popleft()
                res.append(u)
                degree[u] -= 1
                for v in mp[u]:
                    degree[v] -= 1
                    if degree[v] == 1:
                        que.append(v)
        return res
                    
The actual implementation is similar to the BFS topological sort. Remove the leaves, update the degrees of inner vertexes. Then remove the new leaves. 
Doing so level by level until there are 2 or 1 nodes left. What's left is our candidate root node.
We start with the nodes having the minimum indegree (ie; indegree=1, i.e the leaf nodes) and we go on removing them i.e decrementing the indegree of nodes that're connected to them, until we reach the middle nodes.
         
Our problem want us to find the minimum height trees and return their root labels
It is easy to see that the last two pointers are from the two ends of the longest path in the graph.
we need to start from the leaf nodes and find a way to approach the middle nodes, add them to the result    
    

#拓扑排序，逐层删除叶子节点，直到剩下根节点
class Solution2(object):
    def findMinHeight(self, n, edges):
        if n == 1:
            return [0]
        
        leaves = collections.defaultdict(set)
        for u, v in edges:
            leaves[u].add(v)
            leaves[v].add(u)
            
        verticals = set(leaves.keys())
        while len(verticals)> 2:
            que = [x for x in leaves if len(leaves) == 1]
            for x in que:
                for y in leaves[x]:
                    leaves[y].remove(x)
                del leaves[x]
                verticals.remove(x)

        return list(verticals)
