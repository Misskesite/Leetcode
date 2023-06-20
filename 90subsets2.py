# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:10:30 2019

@author: liuga
"""
#回溯算法与 DFS 的区别就是有无状态重置
#回溯法去重是使用过的元素不能重复选取，组合问题可以抽象成树形结构，去重2个维度: 一个是同一树枝上使用过，一个是同一数层上使用
#对于这一题，需要的是数层去重
class Solution(object):
    def subsets2(self, nums):
         res = []
         nums.sort()
         self.dfs(nums, 0, res, [])
         return res
     
    def dfs(self, nums, index, res, path):
         res.append(path)
         if index == len(nums):
             return
            
         for i in range(index, len(nums)):
             if i > index and nums[i] == nums[i-1]: #pass the same number
                 continue
             
             self.dfs(nums, i+1, res, path + [nums[i]])
             #每次在搜索的时候都新建一个 path 变量，而不是复用全局的 path,复用全局需要deepcopy, copy.copy 浅拷贝 只拷贝父对象，不会拷贝子对象
             #copy.deepcopy 深拷贝 拷贝对象及其子对象, 拷贝后跟父对象是独立的，
