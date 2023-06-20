# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 13:41:25 2019

@author: liuga
"""

class TreeNode(object):
    def _init_(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def BuildTree(self, postorder, inorder):
        if not postorder or not inorder:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(root.val)
        root.left = self.BuildTree(inorder[:index], postorder[:index])
        root.right = self.BuildTree(inorder[index+1:], postorder[index:-1])
        return root