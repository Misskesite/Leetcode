# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 16:50:46 2020

@author: liuga
"""
#左右子节点的和的绝对差
class TreeNode(object):
    def _init_(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def findTilt(self, root):
        self.sum  = 0
        self.preOrder(root)
        return self.sums
    
    def postOrder(self, root):
        if not root:
            return 0
        left = self.preOrder(root.left)
        right = self.preOrder(root.right)
        self.sums += abs(left-right)
        return left + right + root.val
