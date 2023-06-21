# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:37:15 2020

@author: liuga
"""
#访问过的信息记录，不会冗余 时间空间复杂度O(n)
class Solution(object):
    def arrayNesting(self, nums):
        
        visited = [False]*(len(nums))
        ans = 0
        for i in range(len(nums)):
            count = 0
            while not visited[i]:
                count += 1
                visited[i] = True
                i = nums[i]
            ans = max(ans, count)
        return ans
    
                
