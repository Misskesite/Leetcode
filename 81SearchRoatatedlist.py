# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 12:00:02 2019

@author: liuga
"""
#nums[l] > num[r]是永远成立的 [2,5,6,0,0,1,2]
class Solution(object):
    def searchRoatatedlist(self, nums,target):
        
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                 return True
             
            if nums[mid] > target :
                if nums[left] <= target or nums[mid] < nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            else:
                if nums[left] > target or nums[mid] > nums[left]:
                    left = mid + 1
                    
                else:
                    right = mid -1
                    
        return False
        


#如果mid比nums[l]还大，说明l到mid是有序的 如果旋转点，从相同的元素中间开始分裂，会丧失二段性
#如果mid比nums[r]还小，说明mid到r有序的 二段性：通过划分数组，使前半段> nums.back, 后半段<= nums.back
class Solution2(object):
    def search(self, nums):
        n = len(nums)
        if not nums:
            return False
        l,r = 0, n-1
        while l <= r:         

            mid = l + (r-l)/2
            
            if nums[mid] == target:
                return True

            if nums[l] == nums[mid]:
                l += 1
                continue
            
            #前半部分有序
            if nums[mid] > nums[l]:     #[1,2,2,5,6,0,0]
                if nums[l] <= target < nums[mid]: #target = 2
                    r = mid - 1
                else:                             #target = 6?
                    l = mid + 1
            #nums[mid] <= nums[r] 可以省略
            elif nums[mid] <= nums[r]:  #[2,5,6,0,0,1,2]
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

            return False
        


#找到翻转点，两边分别二分查找
class Solution3(object):
    def search(self, nums):
        k = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] <  nums[i-1]:
                k = i

        l = 0
        r = k-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True

            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        l = k
        r = n-1    
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True

            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False

#此法为准
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)- 1
        
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            if target == nums[l] or target == nums[r]:
                return True

            if nums[mid] == nums[l]:
                l += 1
                continue
            if nums[mid] == nums[r]:
                r -= 1
                continue

            if nums[mid] > nums[r]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and  nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
