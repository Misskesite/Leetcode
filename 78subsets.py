# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 22:36:16 2019

@author: liuga
"""

#回溯法 此题不需要剪枝 时间复杂度O(2^n) [1,2,3]
class Solution(object):
    def subsets(self, nums):
         res = []
         self.dfs(nums, 0, res, [])
         return res
    #dfs函数意义:当前index元素使用的情况下，从nums的index后面抽取0个或者全部数字放入path的后面
    def dfs(self, nums, index, res, path):
         res.append(path)
         for i in range(index, len(nums)): #for循环，当前元素如果使用，后面的那个元素从哪里开始，也就决定了后面的数字选择多少个
             self.dfs(nums, i+1, res, path + [nums[i]])
         #选择列表的起始位置 index，标识了每一层的状态，即状态变量

'''
回溯类型：
子集，组合，全排列，搜索(解数独，单词搜索，N皇后，分割回文串，二进制手表)
(1) 画出递归树，找到状态变量(回溯函数的参数)
(2) 确定结束条件
(3) 找到选择列表(与函数参数相关)
(4) 判断是否需要剪枝
(5) 做出选择，递归调用，进入下一层
(6) 撤销选择

每一个数字，要么存在，要么不存在

                        []        
                   /          \        
                  /            \     
                 /              \
              [1]                []
           /       \           /    \
          /         \         /      \        
       [1 2]       [1]       [2]     []
      /     \     /   \     /   \    / \
  [1 2 3] [1 2] [1 3] [1] [2 3] [2] [3] []    
