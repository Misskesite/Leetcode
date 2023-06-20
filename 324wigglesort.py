# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:23:44 2020

@author: liuga
"""
#输入nums = [1,5,1,1,6,4] 输出[1,6,1,5,1,4]
class Solution(object):
    def wigglesort(self, nums):
        nums.sort()
        mid = (len(nums)+1)//2
        left = nums[:mid]
        right = nums[mid:]
        nums[::2] = left[::-1]
        nums[1::2] = right[::-1] #从1开始，每隔2个取？
 
        
#follow up O(n)时间复杂度， 原地O(1)的额外空间
three-way partition, O(n)-average time, O(1)-space, 找到中位数k = (len+1)//2, pivot随机选
#输入nums = [1,3,2,2,3,1] 输出[2,3,1,3,1,2]
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        #使用O(n)时间复杂度的quickSelect算法，从未经排序的数组nums中选出中位数mid
        def quickSelect(left, right):
            if left >= right:
                return

            pivot_idx = random.randint(left, right) #pivot随机选
            swap(pivot_idx, right)
            pivot = nums[right]
            start, mid, end = left, left, right

            while mid <= end:
                if nums[mid] < pivot:
                    swap(mid, start)
                    mid += 1
                    start += 1
                elif nums[mid] > pivot: #在这种情况下mid不要移动 因为交换过来的数字nums[end]可能仍是>pivot
                    swap(mid, end)
                    end -= 1
                else:
                    mid += 1
            
            if start <= k <= mid - 1: #第k个刚好是pivot? start对应pivot?
                return
            elif k < start:
                quickSelect(left, start-1) #递归排序
            else:
                quickSelect(mid, right)    #递归排序

        #用3-way partition进行划分，并且找到中位数，对应的位置位k=(len+1)//2，即较大数字分组中的首个。
        k = (len(nums) + 1) // 2
        quickSelect(0, len(nums)-1)
        
        A = nums[k-1::-1]  #开始索引，结束索引，步长(负说明倒序) 从k个倒序取？
        B = nums[:k-1:-1]

        for i in range(len(A)):
            nums[2*i] = A[i]   #[2 1 1]
        
        for i in range(len(B)):
            nums[2*i+1] = B[i] #[3,3,2]

        '''' 上面的方法改写
        A = [:k]
        B = [k:]
        nums[::2] = A[::-1]
        nums[1::2] = B[::-1]

        ''''


class Soluion2
    def wiggleSort(nums):
        n = len(nums)
        if n<= 1:
            return nums
        k = (n+1)//2-1
        mid_value = partition(nums, k, 0, n-1)
        three_way_partition(nums, mid_value)
        nums0 = nums.copy()
        for k in range(n):
            nums[k] = nums0[(n+1)//2-1-k//2] if (not k%2) else nums0[(n-1)-k//2]

    def partition(nums, k, start, end):
        key = nums[start]
        left, right = start, end
     
        while left < right:
            while left < right and nums[right] >= key:
                right = right - 1
            if left < right:
                nums[left],nums[right] = nums[right],nums[left]
            while left < right and nums[left] <= key:
                left = left + 1
            if left < right:
                nums[left],nums[right] = nums[right],nums[left]

        if left == k:
            return nums[left]
        elif left > k:
            return partition(nums, k, start, left-1)
        else:
            return partition(nums, k, left+1, end)

    def three_way_partition(nums, value):
        n = len(nums)
        l, r = 0, n-1
        i = 0
        #不能让i越过r 否则如果nums[l]<=nums[r]<nums[i] 会在下一次中让右侧更大的数字被换到左侧
        while i <= r: 
            if nums[i] < value:
                nums[l],nums[i]=nums[i],nums[l]
                l+=1
                i+=1
            elif nums[i] > value: #在这种情况下i不要移动 因为交换过来的数字nums[r]可能仍是>value
                nums[r],nums[i]=nums[i],nums[r]
                r -= 1
            else:
                i += 1
