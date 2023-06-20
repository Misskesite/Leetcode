# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 16:29:50 2019

@author: liuga
"""

class TreeNode(object):
    def _init_(self,x):
        self.val=x
        self.left = None
        self.right = None
    
#时间复杂度O(n) 空间复杂度O(h)   
class Solution(object):    
        def sortedArrayToBst(self,nums):
            if not nums:
                return None
        
            mid = (len(nums)) //2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBst(nums[:mid])
            root.right = self.sortedArrayToBst(nums[mid+1:])
            return root


#中序遍历，总是选择中间位置左边的数字作为根节点
#时间复杂度O(n), 空间复杂度O(logn) 递归栈的深度
class Solution(object):    
    def sortedArrayToBst(self, nums):
        def helper(left, right):
            if left > right:
                return None

            mid = (left + right)//2

            root = TreeNode(nums[mid])

            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)
            return root

        return helper(0, len(nums)-1)
                
        
