# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 15:36:58 2019

@author: liuga
"""
#时间复杂度O(logn*logn) 空间复杂度O(logn)
class Solution(object):
    def countreeNode(self, root):
        if not root:
            return 0
        nodes = 0
        lh = self.getheight(root.left)
        rh = self.getheight(root.right)
        if lh == rh:
            #左子树是满二叉树，右子树是完全二叉树
            nodes = 2**lh + self.countreeNode(root.right)  #(2 << lh)
        else:
            #左子树是完全二叉树，右子树是满二叉树
            nodes = 2**rh + self.countreeNode(root.left)
            
        return nodes
        
    def getheight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height


#层次遍历 时间复杂度O(n) 空间复杂度O(n) BFS
from collections import deque 
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        q = deque()
        q.append(root)
        res = 0
        while q:
            n = len(q)
            for i in range(n):
                node = p.popleft()
                res += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res
