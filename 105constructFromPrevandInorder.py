# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:31:30 2019

@author: liuga
"""

class TreeNode(object):
    def _init_(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        
        return self._buildTree(0, len(preorder), 0, len(inorder))
    
    def _buildTree(self, pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end:
            return None
        root = TreeNode(self.preorder[pre_start])
        offset = self.inorder[in_start: in_end+1].index(root.val)
        
        root.left = self._buildTree(pre_start+1, pre_start + offset+1, in_start, in_start+offset)
        root.right = self._buildTree(pre_start + offset+1, pre_end, in_start+ offset+1, in_end)
        return root


#时间复杂度O（N） 空间复杂度O（N）       
class Solution2(object):
    def buildTreePreIn(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTreePreIn(preorder[1: mid+1],inorder[:mid])
        root.right = self.buildTreePreIn(preorder[mid+1:], inorder[mid+1:])
        return root
