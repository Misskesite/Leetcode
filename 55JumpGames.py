# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 21:19:10 2019

@author: liuga
"""
#尽可能到达最远位置（贪心), 如果能到达某个位置，那一定能到达它前面的所有位置
class Solution(object):
    def jumpGame(self,nums):
        if not nums:
            return False
        
        n = len(nums)
        i = 0
        longest = nums[0]
        
        while i <= longest:
            if longest >= n -1:
                return True
            longest = max(longest, i + nums[i])
            i += 1
            
        return False
        

