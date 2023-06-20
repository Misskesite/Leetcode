c# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:28:23 2019

@author: liuga
"""
class TreeNode(object):
    def _init_(self, x):
        self.val = x
        self.left = None
        self.right = None

#递归
class Solution(object):
    def sumrootToleaf(self, root):
        if root == None:
            return 0
        return self.dfs(root, 0)
    
    def dfs(self, root, presum):
        
         presum = presum*10 + root.val
         
         if(root.left or root.right) is None:
             return presum
         
         sum = 0
         if root.left:
             sum += self.dfs(root.left, presum)
         if root.right:
             sum += self.dfs(root.right, presum)
         return sum

class Solution:
  def sumNumbers(self, root: Optional[TreeNode]) -> int:
    ans = 0

    def dfs(root: Optional[TreeNode], path: int) -> None:
      nonlocal ans
      if not root:
        return
      presum = path * 10 + root.val
      if not root.left and not root.right:
        ans += presum
        return

      dfs(root.left, presum)
      dfs(root.right, presum)

    dfs(root, 0)
    return ans          
     
class Solution2:
    def sumNumbers(self, root):
        def Sum(root, preSum):
            if not root: #节点不存在返回0
                return 0
            preSum = preSum * 10 + root.val  #root是当前遍历的节点
            if not root.left  and not root.right: #是叶子节点，直接返回和
                return preSum
            
            #不是叶子节点，就递归，把当前和传给孩子节点
            return Sum(root.left, preSum) + Sum(root.right, preSum)
        
        return Sum(root, 0)
