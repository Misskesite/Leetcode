# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:10:44 2019

@author: liuga
"""
#选取数字不重复就按照顺序搜索 时间复杂度O(n*2^n)
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        
        res = []
        self.dfs(candidates, target, 0, res, [])
        return res
    
    def dfs(self, nums , target , index , res, path):
        if target < 0:
            return
        elif target ==0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i]== nums[i-1]: #保证同一级不出现相同的元素
                continue #结束后面的递归
            self.dfs(nums, target-nums[i],i+1, res, path+[nums[i]])        
        
#for 循环里面都是同一级的，放过第一个，不放过第二个，第一个刚好是i== index？

#回溯法 
class Solution2:

    def combinationSum2(self, candidates , target):
        n = len(candidates)
        if n == 0:
            return []

        candidates.sort()
        res = []
        
        def dfs(index, path, target):
            if target < 0:
                return
            if target == 0:
                res.append(path) 
                return

            for i in range(index, n):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                dfs(i + 1, path + candidates[i], target - candidates[i]) # i+1保证不重复调用自己
                
        
        dfs(0, [], target)
        return res
