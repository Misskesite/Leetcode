# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 17:27:18 2020

@author: liuga
"""
#递归
class Node(object):
    def _init_(self, val, children):
        self.val = val
        self.children = children
        

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        if not root.children:
            return 1
        depth = 1 + max(self.maxDepth(child) for child in root.children)
        return depth
        
        
