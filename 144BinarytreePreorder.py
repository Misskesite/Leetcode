# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:33:57 2019

@author: liuga
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#迭代
class Solution(object):
    def preOrder(self,root):
        if not root:
            return []
        res = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return res
        
    def preOrder2(self,root):
        
        result = []
        stack = []
        
        while root or stack:
             if not root:
                 root = stack.pop()
             result.append(root.val)
                 
             if root.right:
                 stack.append(root.right)
                     
             root = root.left
                     
        return result
                     
                     

#递归 时间复杂度O(n), 空间复杂度O(n) 为递归过程中栈的开销，平均情况下是O(logn)
class Solution(object):
    def preorderTraversal(self, root):
        
        def preOrder(root):
            if not root:
                return
            res.append(root.val)
            preOrder(root.left)
            preOrder(root.right)
            
        res = []
        preOrder(root)
        return res
        
        
