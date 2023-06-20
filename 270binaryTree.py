# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 23:30:13 2020

@author: liuga
"""

class Solution(object):
    def binarytreeclosest(self, root, target):
        if not root:
            return
        gap = abs(root.val - target)
        ans = root
        
        while root:
                    
            if root.val == target:
                return root.val
            
            elif root.val > target:
                if abs(root.val - target) < gap:
                    ans = root
                    gap = abs(root.val - target)
                root = root.left
            else:
                if abs(root.val - target) < gap:
                    ans = root
                    gap = abs(root.val - target)
                root = root.right
                
        return ans.val


    def closetValue(self, root, target):
        if root is None:
            return float('inf')

        if root.val == target:
            return root.val

        elif root.val < target:
            rightRes = self.closetValue(root.right, target)
            return root.val if abs(root.val - target) < abs(rightRes - target) else rightRes
        elif root.val > target:
            leftRes = self.closetValue(root.left, target)
            return root.val if abs(root.val - target) < abs(leftRes - target) else leftRes

#迭代方法 计算机对一组指令（或一定步骤）进行重复执行
class Solution2(object):
    def closestValue(self, root, target):
        res = root.val
        while root:
            if abs(res - target) >= abs(root.val - target):
                res = root.val
            
            root = root.left if target < root.val else root.right

        return res

#递归方法
class Solution3(object):
    def closetValue(self, root, target):
        res = root.val
        if root.left and target < root.val:
            l = self.closetValue( root.left, target)
            if abs(res- target) >= abs(l - target):
                res = l
        elif  root.right and target > root.val:
            r = self.closetValue(root.right, target)
            if abs(res- target) >= abs(r - target):
                res = r
        return res

#改写
class Solution:
  def closestValue(self, root: Optional[TreeNode], target: float) -> int:
    # If target < root.val, search left subtree
    if target < root.val and root.left:
      left = self.closestValue(root.left, target)
      if abs(left - target) < abs(root.val - target):
        return left

    # If target > root.val, search right subtree
    if target > root.val and root.right:
      right = self.closestValue(root.right, target)
      if abs(right - target) < abs(root.val - target):
        return right

    return root.val
