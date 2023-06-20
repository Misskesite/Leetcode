# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:11:10 2019

@author: liuga
"""
#每到一个节点，有 3 种选择：1. 停在当前节点。2. 走到左子节点。3. 走到右子节点
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    
    def maxPathsum(self,root):
        self.maxSum = float("-inf")
        self._maxPathsum(root)
        
        return self.maxSum
    
    def _maxPathsum(self, root):
         if root == None:
             return 0
         left = max(0, self._maxPathsum(root.left))
         right = max(0, self._maxPathsum(root.right))
        
         
         self.maxsum = max(self.maxvalue, root.val + left + right)
         
         return max(left, right) + root.val #当前节点的贡献值


#维护一个全局变量 maxSum存储最大路径和，在递归过程中更新maxSum的值. 在递归到每个节点时，用经过该节点的最大路径和更新最终结果
#时间复杂度O(N),每个节点访问不超过2次，空间复杂度O(N),取决于递归调用层数(树的高度)，最坏的结果高度等于节点个数
class Solution(object):
    def maxPathsum(self, root):
        max_pathsum = float("-inf")
        
        def traversal(root):
            nonlocal max_pathsum
            if not root:
                return 0
            #递归计算左子节点的贡献值
            left = max(0, traversal(root.left))
            #递归计算右子节点的贡献值
            right = max(0, traversal(root.right))

            #经过当前节点的最大路径和
            max_pathsum = max(max_pathsum, left + right + root.val)

            #当前节点的贡献值(非叶子节点)，取左右子节点中的更优方案. 叶子节点贡献值节点本身
            node_contr = max(left, right) + root.val
            
            return node_contr  #返回的贡献值给当前节点的上游节点

        traversal(root)
        return max_pathsum


    #最大收益取三者最大：root.val+ max(0, dfs(root.left), dfs(root.right))
    def maxPathsum(self, root):
        max_pathsum = float("-inf")
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            innerMax = root.val + left + right
            max_pathsum = max(max_pathsum , innerMax)
            outputSum = root.val + max(0, left, right)
            return outputSum < 0 ? 0 : outputSum

        dfs(root)
        return max_pathsum
            
