# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 21:10:23 2019

@author: liuga
"""

class Solution(object):
    def Maxarea(self, height) :
        if not height:
            return 0
        l = 0
        r = len(height) -1
        result = 0
        #选左右挡板比较小的高度
        while l < r:
            if height[l] < height[r]:
                result = max(result, area)
                area = height[l]*[r - l]                
                left += 1
            
            else:
                area = height[r]*(r - l)
                result = max(result, area)
                right -=1
            
        return result
        
            
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height) - 1

        while l < r:
            minHeight = min(height[l], height[r])
            ans = max(ans, minHeight * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

    return ans
