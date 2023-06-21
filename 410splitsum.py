# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:53:56 2020

@author: liuga
"""

class Solution(object):
    def splitsum(self, nums, m):
        size = len(nums)
        high = sum(nums)
        low = high/m
        
        while low <= high:
            mid = (low + high)/2
            n = m
            cnt = 0
            valid = True
            for x in range(size):
                if nums[x]> mid:
                    valid = False
                    break
                if cnt + nums[x]> mid:
                    n -= 1
                    cnt = 0
                cnt += nums[x]
                if n == 0:
                    valid = False
                    break
            if valid:
                high = mid -1
            else:
                low = mid +1
        return low
                    
#类型：最大值极小化                    
#时间复杂度O(n*(n*log(sum - maxn))  空间复杂度O(1)
#[使...最大值尽可能小]是二分搜索常见的问题，选定一个x，线性的验证是否存在一种分割方案，满足最大分割子数组和不超过x
#计算数组和最大值不大于mid对应的子数组个数 cnt(这个是关键！) 为什么要贪心的使子数组和不断逼近mid。先猜一个mid，然后遍历数组划分，使每一个子数组和都接近mid，这样子数组数会最小
#如果这样子数组数量多于m个，说明mid猜小了，lo = mid + 1,如果子数组数量小于等于m，mid可能更小，因此high = mid
class Solution:
    def splitArray(self, nums: List, m):
        def check(x):
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= k #如果相等，left!= right 会继续收敛，取左半边，最终找到确切值，即取得最大值的数组和
        '''
        for num in nums:
            total += num
            if total > x:
                cnt += 1
                total = num

                if cnt > m:
                    return False
        return True
                    

        '''
        


        left = max(nums)
        right = sum(nums)
        while left < right: #left == right终止，返回任意一个
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
