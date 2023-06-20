# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:46:14 2019

@author: liuga
"""

#时间复杂度O(n) 空间复杂度O(1)
#左值<中值 中值<右值 最小值在最左边
#左值>中值 中值<右值 最小值在左半边，收缩右边界
#左值<中值 中值>右值 最小值在左半边，收缩右边界
#通过比较中值与右值，可以确定最小值的位置范围，从而决定边界收缩的方向
class Solution(object):
    def findMin(self, nums): #找最小值，朝左找？
        n = len(nums)
        
        if n == 1:
            return nums[0]
        left, right = 0, n-1
        
        while left < right and nums[left] > nums[right]: #while left < right:
            mid = (left + right) /2
            if nums[mid] < nums[right]: #最小值在左半边，收缩右边界
                right = mid
            else:
                left = mid+1 #中值> 右值，中值肯定不是最小值，左边界可以跨过mid
        return nums[left]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return nums[l]

'''
这里用中间的值 nums[mid] 和右边界值 nums[right] 进行比较，
若数组没有旋转或者旋转点在左半段的时候，中间值是一定小于右边界值的，所以要去左半边继续搜索，反之则去右半段查找 即可

[3,4,5,1,2] 输出 1
[4,5,6,7,0,1,2] 输出0 
