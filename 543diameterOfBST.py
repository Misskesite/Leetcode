# -*- coding: utf-8 -*-
"""
Created on Mon May 25 19:49:03 2020

@author: liuga
"""
#类似124 两点之间的最远距离,左右子树深度的比较
class Treenode(object):
    def _init_(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def diameterofBST(self,root):
        self.res = 0
        
        def maxDepth(node):
            if not node:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            self.res = max(self.res, left+right) # 每个结点都要去判断左子树+右子树的高度 left+right如果比res大就更新
            return max(left, right) + 1
        
        maxDepth(root)
        return self.res
            
