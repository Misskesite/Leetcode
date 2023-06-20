# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 17:22:06 2019

@author: liuga
"""

class Solution(object):
    def permutation2(self,nums):
         result = []
         nums.sort()
         self.get_permute([], nums, result)
         return result
     
    def get_permute(self, path, num, result):
         if not num:
             result.append(path)
             return
         for i , v in enumerate(num):
            if i-1 >= 0 and num[i] == num[i-1]:
                continue
            self.get_permute(path + [v], num[:i] + num[i+1:], result)

#此解法为主
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res
            
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            

#两个相同的数字，选一个，这种情况需要剪枝
class Solution2(object):
    def permuteUnique(self, nums):        
        res = []
        visited = [0]*len(nums)
        nums.sort()
        def dfs(path):
            if len(path) == len(nums):
                res.append(path) 
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                visited[i] = 1
                dfs(path + [nums[i]])
                visited[i] = 0
        dfs([])
        return res
