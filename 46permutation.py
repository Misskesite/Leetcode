# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 17:13:57 2019

@author: liuga
"""
#递归法
class Solution(object):
    def permute(self,nums):
        
        res = []
        self.dfs(nums, res, [])
        return res
    
    def dfs(self, nums, res, path):
        if not nums:
           res.append(path)
           return
           
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i+1:], res, path + nums[i])

#回溯方法
class Solution2(object):
    def permutation(self, nums):
        
        visited = [0] * len(nums)
        res = []
        
        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = 1
                        dfs(path + [nums[i]])
                        visited[i] = 0
        
        dfs([])
        return res
       
#优化不用visited
class Solution3(object):
    def permutation(self, nums):
        res = []
        path = [] #存放符合条件的结果
        
        def backtrack(nums):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(nums)
                path.pop() #回溯
        backtrack(nums)
        return res
