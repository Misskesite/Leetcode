# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:26:55 2019

@author: liuga
"""

class Solution(object):
    def jumpGame(self, nums):
        length = len(nums)
        count = 0
        longest = 0
        reach = 0
        for i in range(length):
            if longest < i:
                count += 1
                longest = reach
                reach = max(reach, nums[i]+1)
        return count
    


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        end = 0
        farthest = 0

        # Implicit BFS
        for i in range(len(nums) - 1):
            if nums[i] = 0:
                return -1
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                ans += 1
                return ans
            if i == end:      # Visited all the items on the current level
                ans += 1        # Increment the level
                end = farthest  # Make the queue size for the next level
        
        return ans
