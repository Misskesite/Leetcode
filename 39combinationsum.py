# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 16:54:37 2019

@author: liuga
"""
#DFS,进行了全集的搜索, 对比40，这里数字可以重复选
class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        
        candidates.sort()
        self.dfs(candidates, target, 0 ,res ,[])
        
        return res
    
    def dfs(self, nums, target,index, res, path):
         if target < 0:
            return
        
         elif target == 0:
               res.append(path)
               return
     
         for i in range(index, len(nums)):
            if nums[index] > target:
                return
            self.dfs(nums, target-nums[i], i, res, path+[nums[i]])
        
         
#回溯法
class Solution(object):
    def combinationSum(self, candidates, target):
        res = []        
        candidates.sort()
        n = len(candidates)

        def backtrack(i, tmp_sum, path):
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(path)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j]> target:
                    break
                path.append(candidates[j])
                backtrack(j, tmp_sum + candidates[j], path)
                path.pop()
        backtrack(0,0,[])
        return res

            
