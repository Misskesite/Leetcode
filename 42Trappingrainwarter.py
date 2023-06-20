# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 21:06:28 2019

@author: liuga
"""
#时间复杂度O(n)  空间复杂度O(n) 木桶效应:左右最大值中比较小的
class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        n = len(height)
        result = 0
        maxh = [0 for _ in range(n)]
        
        h = height[n -1]
        
        for i in range(n-2, -1, -1):
            maxh[i] = h                  #右边最大高度
            h = max(h, height[i])
            #maxh[i] = max(maxh[i+1], height[i+1])
            
        lh = height[0]        
        
        for i in range(1, n-1):
            lh = max(lh, height[i])
            #max_left[i] = max(max_left[i-1], height[i-1])
            
            result += max(0 , min(lh, maxh[i])- height[i]) #左右最大值中比较小的 小于当前高度，不能积水，值为0
            
        return result
    
#双指针决定容量的是左右最大高度中较小的那一个，减去当前的高度
#时间复杂度 O(n),空间复杂度O(1)
class Solution2:
    def trap(self, height): 
        if not height: 
            return 0
        left_max = right_max = res = 0
        left, right = 0, len(height) - 1
 
        while left < right:
            #只要保证height[left] < height[right], left_max就小于right_max
            if height[left] < height[right]:   # 左指针操作
                if height[left] < left_max:    #换成 left_max = max(left_max, height[left]), if left_max > height[left]: res += left_max - height[left] left+=1
                    res += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1                      # 移动左指针
                
            else:
                if height[right] < right_max:  # 右指针操作
                    res += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1                     # 移动右指针
        return res
