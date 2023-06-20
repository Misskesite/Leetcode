# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:21:27 2020

@author: liuga
"""
#重复的数为target cnt[i]数组里面小于等于i的数有多少个。[1, target-1]里面的数都满足cnt[i]<=i [target, n]里面所有的数满足cnt[i] > i
class Solution(object):
    def findduplicate(self, nums):
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = l + (r-l)/2
            cnt = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    cnt += 1
            if cnt > mid:
                r = mid - 1
            else:
                l = mid + 1
        return l

    #以下面的方法为准 鸽巢原理
    #这里比较特殊， l ，r对应数字，不是index
    def findduplicate2(self, nums):
        l = 1
        r = len(nums)-1
        while l < r:
            mid = l + (r-l)/2
            cnt = 0
            for i in range(len(nums)): #个数小于等于 mid，则说明重复值在 [mid+1, n] 之间，反之，重复值应在 [1, mid-1] 之间
                if nums[i] <= mid:
                    cnt += 1
            if cnt > mid:
                r = mid
            else:
                l = mid + 1
        return l
# choose middle element m = n//2 and count number of elements in list, which are less or equal than m. If we have m+1 of them it means we need to search for duplicate in [1,m] range, else in [m+1,n] range.
#Each time we reduce searching range twice, but each time we go over all data. So overall complexity is O(n log n).

#数组里有重复的数，就会有多对1的映射，形成的链表就有环路了    
class Solution2(object):
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast: # fast, slow相遇点？
            fast = nums[nums[fast]]
            slow = nums[slow]
        finder = 0
        while slow != finder:
            finder = nums[finder]
            slow = nums[slow]
        return finder
