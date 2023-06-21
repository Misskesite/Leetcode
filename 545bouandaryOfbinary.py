# -*- coding: utf-8 -*-
"""
Created on Tue May 26 11:52:17 2020

@author: liuga
"""

class Solution(object):
    def bounadaryBST(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        
        leaves = []
        def traverse(root):
            if not root.left and not root.right:
                leaves.append(root)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
        
        traverse(root)
        
        left = []
        node = root
        while node and node != leaves[0]:
            left.append(node)
            if node.left:
                node = node.left
            else:
                node = node.right
        
        right = []
        node = root
        while node and node != leaves[-1]:
            right.append(node)
            if node.right:
                node = node.right
            else:
                node = node.left
                
        left = left[1:] if root.left else []
        right = right[1:] if root.right else []
        
        return [node.val for node in [root] + left + leaves + right[::-1]]
    
 #此解法为主   
class Solution2(object):
    def boundaryOfBinaryTree(self, root):
        
        def leftboundary(node): #左边类似先序遍历
            if not node or (node.left is None and node.right is None): #空或者叶子节点不算左边界
                return
            res.append(node.val)
            if node.left:
                leftboundary(node.left)
            else:
                leftboundary(node.right) # no left tree, then search right
        
        def leaves(node):
            if not node:
                return
            
            if node != root and node.left is None and node.right is None:
                res.append(node.val)
                
            leaves(node.left)
            leaves(node.right)          

                
        def rightboundary(node):
            if not node or (node.left is None and node.right is None):
                return
            if node.right:
                rightboundary(node.right)
            else:
                rightboundary(node.left)
            res.append(node.val) #post order. 逆序的，所以node最后加
            
        if not root:
            return []
        
        res = [root.val]
        leftboundary(root.left)
        leaves(root)
        rightboundary(root.right)
        return res

            
                

            
