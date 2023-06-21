# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:47:35 2020

@author: liuga
"""
#二叉查找树中，中间节点的值一定是其左右节点值的中间数，因此最小差别一定是在中间节点与左右节点之间
class Solution(object):
    def minimumDifference(self, root):
        self.pre = -0x80000000
        self.ans = 0x7FFFFFFF #float("inf")
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.ans = min(self.ans, root.val - self.pre)
            self.pre = root.val
            inorder(root.right)
        inorder(root)
        return self.ans
        
                
class Solution(object):
    def minimumDifference(self, root):
        self.pre = -1
        self.ans = float("inf")
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.pre != -1 :
                self.ans = min(self.ans, root.val - self.pre)
            self.pre = root.val
            inorder(root.right)
        inorder(root)
        return self.ans            
