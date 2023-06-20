# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:54:26 2019

@author: liuga
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.check(root.left, root.right)
    
    def check(self, left, right):
        if not left and not right:
            return True
        if not left or not right: #有一个为空 not (left and right)
            return False
        if left.val != right.val:
            return False
        
        return self.check(left.left, right.right) and self.check(left.right, right.left)
    
    
