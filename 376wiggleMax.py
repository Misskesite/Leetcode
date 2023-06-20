# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 20:54:36 2020

@author: liuga
"""
#[1,7,4,9,2,5] 时间复杂度O(n) 求最大长度？
class Solution(object):
    def wiggleMax(self, nums):
        n = len(nums)
        if n <= 1:
            return n
        inc = [1]*n #当前状态为递增子序列最大长度
        dec = [1]*n #当前状态为递减子序列最大长度
        
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                inc[i] = dec[i-1]+1
                dec[i] = dec[i-1]
            elif nums[i] < nums[i-1]:
                inc[i] = inc[i-1]
                dec[i] = inc[i-1] +1
            else:
                inc[i] = inc[i-1]
                dec[i] = dec[i-1] 
                
        return max(inc[-1], dec[-1])

 #空间复杂度进一步优化 O(1) 如果当前数字比前一个数字大，则p=q+1，如果比前一个数字小，则q=p+1，最后取p和q中的较大值
    def wiggleMax(self, nums):
        if not nums:
            return 0
        n = len(nums)
        inc = dec = 1 # cur is incresing/decresing
        for x in range(1, n):
            if nums[x] > nums[x-1]:
                inc = dec + 1
            elif nums[x] < nums[x-1]:
                dec = inc + 1
        return max(inc, dec)
    
        #改写
        if not nums:
            return 0
        
        length = 1
        up = None # current is increasing or not
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and up != True:
                length += 1
                up = True
            if nums[i] < nums[i - 1] and up != False:
                length += 1
                up = False
        return length


#DP 时间复杂度O(n*n) 冗余，跟前一个值比大小有关系
class Solution3(object):
    def wiggleMax(self, nums):
        if not nums:
            return 0
        n = len(nums)
        inc = [1]*n
        dec = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    inc[i] = max(inc[i], dec[j] + 1)
                
                elif nums[i] < nums[j]:                    
                    dec[i] = max(dec[i], inc[j] + 1)
        return max(inc[-1], dec[-1])
                
                
