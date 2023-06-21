# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:38:36 2020

@author: liuga
"""

class Solution(object):
    def findSubsequenece(self, nums):
        dp = set()
        for n in nums:
            for y in list(dp):
                if n >= y[-1]:
                    dp.add(y + (n,))
                dp.add((n,))
        return list(e for e in dp if len(e)>1)

#nums = [4,6,7,7] 输出 [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
#backack
class Solution2(object):
    def findSubsequence(self, nums):
        if not nums:
            return
        res = []
        s = set()

        dfs(0, [])

        def dfs(index, path):
            if len(path) >= 2:
                p = str(path)
                if p not in s:                    
                    res.append(path[:])
                    s.add(p)
            
            for i in range(index, len(nums)):                
                if not path or nums[i] >= path[-1]:                    
                    path.append(nums[i])
                    dfs(i+1, path)
                    path.pop()
                
        return res


#nums = [4,6,7,7] 输出[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(s: int, path: List[int]) -> None:
            if len(path) > 1:
                ans.append(path)

            used = set() #去重同一层的？

            for i in range(s, len(nums)):
                if nums[i] in used:
                    continue
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return ans
    

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.res = set()
        
        def dfs(i, path=[]):
            if len(path) > 1:
                self.res.add(tuple(path[:]))
            
            for j in range(i, len(nums)):
                if not path or path[-1] <= nums[j]:
                    dfs(j+1, path+[nums[j]])
        
        dfs(0)
        return self.res

