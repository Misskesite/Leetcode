# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 22:03:36 2020

@author: liuga
"""
#BFS
class Solution(object):
    def narrayTree(self, root):
        if not root:
            return []
        queue = [(root,0)]
        res = [[]]
        while queue:
            node, level = queue.pop(0)
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
            for child in node.childen:
                queue.append((child, level+1))
        return res

import collections
#O(N)
class Solution2(object):
    def narrayTree(self, root):        
        res = []
        que = collections.deque()
        que.append(root)
        while que:
            level  = []
            size = len(que)
            for i in range(size):
                node = que.popleft()
                if not node:
                    continue
                level.append(node.val)
                for child in node.children:
                    que.append(child)
            if level:
                res.append(level)
        return res



class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        Q, ans = deque([root]), []
        
        while Q:
            level = []
            for i in range(len(Q)):
                node = Q.popleft()
                for child in node.children:
                    Q.append(child)
                level += [node.val] 
            ans += [level]

        return ans
