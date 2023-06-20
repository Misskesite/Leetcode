# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:00:01 2019

@author: liuga
"""
#时间复杂度O(NlogN),最差情况遍历所有的节点O(N),乘以每个节点的复杂度， 空间复杂度O(N) 最坏情况下需要的栈空间
#子树的节点数的复杂度为O(logN)?
class Solution(object):
    def Height(self, root):
        if root == None:
            return 0
        return max(self.Height(root.left), self.Height(root.right)) + 1
    
    def balanceBST(self, root):
        if root == None:
            return True
        
        if abs(self.Height(root.left) - self.Height(self.right)) <= 1:
            return self.balanceBST(root.left) and self.balanceBST(root.right)
        else:
            return False


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def maxDepth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            return 1 + max(maxDepth(root.left), maxDepth(root.right))

        return abs(maxDepth(root.left) - maxDepth(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)
