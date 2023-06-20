# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:21:17 2019

@author: liuga
"""

class TreeNode(object):
    def _init_(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def rightsideView(self, root):
        res = []
        self.levelOrder(root, 0, res)
        return [level[-1] for level in res]
    
    def levelOrder(self, root, level, res):
        if not root:
            return
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
            
        if root.left:
             self.levelOrder(root.left, level+1, res)
             
        if root.right:
            self.levelOrder(root.right, level+1, res)

#时间复杂度O(n）每个节点出入队一次，空间复杂度O(n) 使用额外的队列空间
import collections
class Solution2(object):
    def levelOrder(self, root):
        res = []
        if not root: 
            return res
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == n-1:
                    res.append(node.val)
        return res
