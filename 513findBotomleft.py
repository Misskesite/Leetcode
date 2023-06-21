# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:36:31 2020

@author: liuga
"""
import collections

class Solution(object):
    def findbottomleft(self, root):
        
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            level = []
            for i in range(size):
                node = q.popleft()
                if not node:
                    continue
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if level:
                res.append(level)
                
        return res[-1][0]

#BFS
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            # 先右后左
            if node.right: 
                queue.append(node.right)
            if node. left:
                queue.append(node.left)
        return node.val
