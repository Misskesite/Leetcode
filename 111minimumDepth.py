# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:01:38 2019

@author: liuga
"""

class TreeNode(object):
    def _init_(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
     
    def minimumDepth(self, root):
        if root == None:
            return 0
        
        if not root.left:
            return 1 + self.minimumDepth(root.right)
        
        elif not root.right:
            return 1 + self.minimumDepth(root.left)
        
        else:
            return 1 + min(self.minimumDepth(root.left), self.minimumDepth(root.right))
        
        
