# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:10:56 2020

@author: liuga
"""

class Treenode(object):
    def _init_(self,x):
        self.val = x
        self.left = None
        self.right = None
        
#递增或递减长度 the path can be in the child-parent-child order
class Solution(object):
    def Solve(self, root):
        inc = dec = 1
        for child in (root.left, root.right):
            if not child:
                continue
            cinc, cdec = self.solve(child)
            if child.val == root.val-1:
                dec = max(dec, cdec+1)
            elif child.val == root.val+1:
                inc = max(inc, cinc+1)
        self.ans = max(self.ans, dec+inc-1)
        return inc, dec
    
    #改写
    def Solve(self, root):
        if not root:
            return (0, 0)

        inc , dec = 1, 1
        if root.left:
            l = self.solve(root.left):
            if root.val = root.left.val + 1:
                dec = max(dec, l[1] + 1)
            elif root.val = root.left.val - 1:
                inc = max(inc, l[0] + 1)
        if root.right:
            r = self.solve(root.right):
            if root.val = root.right.val + 1:
                dec = max(dec, r[1] + 1)
            elif root.val = root.left.val - 1:
                inc = max(inc, r[0] + 1)
        self.ans = max(self.ans, dec + inc -1)
        return (inc, dec)
        

    def BinarytreeConsecutive(self,root):
        self.ans = 0
        if root:
            self.solve(root)
        return self.ans
    
#此法为主
class Solution2(object):
    def longestConsecutive(root):
        self.res = 0
        
        def dfs(node, parent):
            if not node:
                return (0, 0)
            left = dfs(node.left, node)
            right = dfs(node.right, node)
            
            self.res = max(self.res, left[0] + right[1] + 1)
            self.res = max(self.res, left[1] + right[0] + 1)
            inc = 0
            dec = 0
            if node.val == parent.val + 1:
                inc = max(left[0], right[0]) + 1
            elif node.val == parent.val - 1:
                dec = max(left[1], right[1]) + 1
            return (inc, dec)
        
        dfs(root, root)
        return self.res        
            
#类似于先序遍历 
class Solution3(object):
    def binarytreeConsecutive(self, root):
        if not root:
            return 0        

        def dfs(node, diff):
            if not node:
                return 0
            left = 0
            right = 0
            if node.left and node.val - node.left.val == diff:
                left = 1 + dfs(node.left, diff)
            if node.right and node.val - node.right.val == diff:
                right = 1 + dfs(node.right, diff)
            return max(left, right)


        res = dfs(root, 1) + dfs(root, -1) + 1 #经过root, 对两边递归，不经过root
        return max(res, binarytreeConsecutive(root.left), binarytreeConsecutive(root.right))
                
                
        
        
