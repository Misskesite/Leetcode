# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:23:18 2019

@author: liuga
"""

class Solution(object):
    def combineSum(self,n,k):
        res = []
        self.helper(1, [])
        def dfs(s: int, path: List[int]) -> None:
            if len(path) == k:
                ans.append(path.copy())
                return

            for i in range(s, n + 1):
                path.append(i)
                dfs(i + 1, path)
                path.pop()
        return res
    
            
    
#求组合需要用dfs解决
class Solution2(object):
    def combination(self, n, k):
        def dfs(start, path):
            if self.count == k:
                self.res.append(path)
                return
            for i in range(start, n+1):
                self.count += 1
                dfs(i+1, path + [i])
                self.count -= 1
        res = []
        self.count = 0
        dfs(1, [])
        return res


#回溯法
class Solution(object):
    def combineSum(self, n, k):
        res = []
        nums = range(1, n+1)
        self.backtracking(nums, k, res, [])
        return res


    def backtracking(self, nums, k, res, path):
        if k > len(array):
            return
        if k == 0:
            res.append(path)
        else:
            #抽取第一个再从后面的n-1个中抽取m-1个;抽取第二个,从后面n-2中抽取m-1个
            #每次向后寻找，不用担心重复
            for i in range(len(nums)):
                self.backtracking(nums[i+1:], k-1, res, path + [nums[i]])
        
