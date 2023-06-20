# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:53:56 2019

@author: liuga
"""
#二分查找要注意细节，比如边界，可以调用 bisect的bisect_left 和 bisect_right

class Solution:
    def searchRange(self, nums, target):
        left = self.serachLeft(nums, target)
        right = self.serachRight(nums, target)
        return [left, right]
    
    #搜索区间[left, right]
    def serachLeft(self, nums: List[int], target: int):
        left = 0
        right = len(nums)-1   # 搜索区间为闭区间
        while left <= right:  # 因为是闭区间，所以left=right才是最后一个搜索区间
            mid = int(left + (right - left)/2)
            if nums[mid] == target:
                right = mid-1 #收缩右边界
            elif nums[mid] < target:
                left = mid + 1 #[mid+1, right]
            elif nums[mid] > target:
                right = mid-1  #[left, mid-1]
        if left >= len(nums) or nums[left] != target:
            return -1
        return left
  
    def serachRight(self, nums: List[int], target: int):
        left = 0
        right = len(nums)-1 # 搜索区间为闭区间 终止条件是 left == right + 1
        while left <= right: # 因为是闭区间，所以left=right才是最后一个搜索区间
            mid = int(left + (right - left)/2)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid-1
        if right < 0 or nums[right] != target:
            return -1
        return right
    

#low_bound 返回的是第一个满足条件的位置，high_bound 返回的是第一个不满足条件的位置(需要-1？) 相等表示没有找到
class Solution2(object):
    def searchRange(self, nums, target):

        left = self.lower_bound(nums, target)
        right = self.higer_bound(nums, target)

        if left == right:
            return [-1, -1]

        return [left, right-1]

    #类似于bisect.bisect_left
    def lower_bound(self, nums, target): #find in range[left,right)
        l, r = 0, len(nums)
        while l < r:   #搜索区间[left, right) 终止条件left == right
            mid = l + (r - l)/2  #对应的 (l+ r)/2
            if nums[mid] < target:
                l = mid +1
            else:
                r = mid #下一步去掉mid，分割成两个区间[left, mid)或者[mid+1, right)
        return l
    
    #类似于bisect.bisect_right
    def higher_bound(self, nums, target): #find in range[left,right)
        l , r = 0, len(nums)
        while l < r:
            mid = l + (r - l)/2
            if nums[mid] <= target:
                l = mid +1 #边界不停右缩，锁定右侧边界
            else:
                r = mid
        return l

#二分用这个模板细节。满足条件的都写l = mid或者r = mid，mid首先写成l + r >> 1，如果满足条件选择的是l = mid，那么mid，写成l + r + 1 >> 1。
#然后就是else对应的写法l = mid对应r = mid - 1，r = mid对应l = mid + 1
#寻找左边界，将m设置为居中偏左位置m = l + r >> 1，并慢慢将右边界左移r = m
#寻找右边界，将m设置为居中偏右位置m = l + r + 1 >> 1，并慢慢将左边界右移l = m
class Solution3(self, nums, target):
    if not nums:
        return [-1,-1]
    
    l, r = 0, len(nums)-1
    while l < r:
        mid = l + (r - l)/2  #对应的 (l+ r)/2
        if nums[mid] >= target:
            r = mid     #收缩右边界不影响 first equals
        else:  
            l = mid + 1
    if nums[l] == target:
        left_bound = l
    else:
        return [-1, -1]

    l, r = 0, len(nums)-1
    while l < r:
        mid = (l + r + 1)/2 #右中位数
        if nums[mid] <= target:
            l = mid    #收缩左边界不影响 last equals
        else:
            r = mid -1
    if nums[r] == target:
        right_bound = r
    else:
        right_bound = left_bound
        
    return [left_bound, right_bound]
