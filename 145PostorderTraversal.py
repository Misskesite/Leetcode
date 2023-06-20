# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 20:12:24 2019

@author: liuga
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTravasal(self, root):
         stack = []
         stack.append(root)
         
         result = []
         
         while stack:
             temp = stack.pop()
             
             if temp:
                result.append(temp.val)
                stack.append(temp.left)
                stack.append(temp.right)
                
         return result[::-1]
            
            