# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:10:18 2019

@author: liuga
"""

class UndirectedGrapghNode:
    def _init_(self, x):
        self.val = x
        self.neighbors = []
        
class Solution(object):
    def cloneGrapgh(self, node):
            
        if not node :
            return None
        
        def dfs(self,input, mp):
            if input in mp:
                return mp[input]
            output = UndirectedGrapghNode(input.val)
            mp[input] = output
            for neibor in input.neighbors:
                output.neighbors.append(self.dfs(neibor, mp))
                
            return output

        return dfs(node, {})

#hashmap 原节点 -> 复制节点，递归调用当前节点node的邻接节点neighbors，并进行克隆，最后将这些克隆的邻接节点加入克隆节点的邻接表中
#时间复杂度O(V+E)
class Solution2(object):
    def cloneGraph(self, node):
        lookup = {}

        def dfs(node):
            if not node:
                return
            if node in lookup:
                return lookup[node]
            #克隆节点
            clone = Node(node.val, [])
            lookup[node] = clone

            #克隆边
            for neighbor  in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
    

    
class Solution3(object):
    def cloneGrapgh(self, node):
        node_copy = self.dfs(node, dict())
        return node_copy
    
    def dfs(self, node, hashd):
        if not node:
            return None
        if node in hashd:
            return hashd[node]
        
        node_copy = UndirectedGrapghNode(node.val,[])
        hashd[node] = node_copy
        
        for n in node.neighbors:
            n_copy = self.dfs(n, hashd)
            if n_copy:
                node_copy.neighbors.append(n_copy)
                
        return node.copy
            
            
    
