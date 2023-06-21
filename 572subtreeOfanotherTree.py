# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:34:51 2020

@author: liuga
"""

class Solution(object):
    def isSame(self,s,t): #same tree?
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val != t.val:
            return False
        return self.isSame(s.left,t.left) and self.isSame(s.right,t.right)
    
    def isSubtree(self, s,t):
         if s is None:
             return False
         if self.isSame(s, t):
             return True
         return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

#此解法为主，递归
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return root.val == subRoot.val and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)

''''
从s的某个结点开始，跟t的所有结构都一样，那么问题就转换成了判断两棵树是否相同，也就是Same Tree的问题了
