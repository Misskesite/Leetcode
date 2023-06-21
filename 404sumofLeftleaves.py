# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 21:53:43 2020

@author: liuga
"""

class Solution(object):
    def isleaf(self,root):
        if root.left == None and root.right == None:
            return True
        
    def sumLeftleaves(self, root):
        if root == None:
            return 0
        s = 0 #临时变量
        if root.left and self.isleaf(root.left):
            s = root.left.val
        return s + self.sumLeftleaves(root.left) + self.sumLeftleaves(root.right)


class Solution2(object):
    def sumLeftleaves(self, root):
        if not root:
            return 0
        return self.sumLeftleaves(root.left) + self.sumLeftleaves(root.right) + (root.left and  root.left.left == None and root.left.right == None)? root.left.val: 0
        
#此解法为主       
class Solution(object):
    def sumLeftleaves(self, root):
        if not root:
            return 0
        #左边是叶子节点
        if root.left and  root.left.left == None and root.left.right == None:
            return root.left.val + self.sumLeftleaves(root.right)
        #左边不是叶子节点
        return self.sumLeftleaves(root.left) + self.sumLeftleaves(root.right)
