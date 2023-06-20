# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:28:50 2019

@author: liuga
"""
from collections import heapq
#每次弹出logn logn*k+n 创建堆(顺序是bottom-top)的时间复杂度为O(n) k+(n-k)logn?
class Solution(object):
    def findkthLarget(self, nums, k):
        if not nums:
            return -1
        h = []
        for i in range(len(nums)):
            if len(h) < k :
                heapq.heappush(h, nums[i])
            else:
                if h[0] < nums[i]:
                    heapq.heappop(h)
                    heapq.heappush(h, nums[i])                    
        return h[0]

    
#最小堆，移除了n-k个最小的元素，剩下k个大元素   
class Solution2(object):
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        l = len(nums)
        while l > k:
            heapq.heappop(nums)
            l -= 1
        return nums[0]

#快速排序 平均时间复杂度O(n) (n + n/2 + n/4) 如果每次选pivot最大值，最大时间复杂度为O(n*n)
class Solution(object):
    def findKthLargest(self, nums, k):
        def partition(nums, left, right):
            pivot = nums[left]
            i ,j = left, right
            while i < j:
                while i < j and nums[j] >= pivot: #从后往前，找到一个比pivot更小的数
                    j -= 1
                nums[i] = nums[j]    #更小的数放左边
                while i < j and nums[i] <= pivot: #从前往后,找到一个比pivot更大的数
                    i += 1           
                nums[j] = nums[i]    #更大的数放右边
            #循环结束,i 和j 相等
            nums[i] = pivot
            return i

        def topk_split(nums, k, left, right):
            #寻找第k个数停止递归, 使得nums数组 index左边是前k个小的数，index右边是n-k个大的数
            if left < right:
                index = partition(nums, left, right)
            if index == k:
                return
            elif index < k :
                topk_split(nums, k, index+1, right)
            else:
                topk_split(nums, k, left, index-1)

        #partition是按从小到大划分的,如果让index左边为前n-k个小的数，则index右边为前k个大的数
        topk_split(nums, len(nums)-k, 0, len(nums)-1) #k换成len(nums)-k
        return nums[len(nums)- k]

#quickselect 此题为准
class Solution(object):
    def findKthLargest(self, nums, k):
        k = len(nums) - k #第n-k小

        def quickSelcet(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p] #p放中间，左边的比P小，右边的比p大

            if p > k:
                return quickSelect(l, p-1)
            elif p < k:
                return quickSelect(p+1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums)- 1)
                
            
#快速选择,第k大    O(n)     
import random
class Solution1:
    
    def findKthLargest(self, nums, k):
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        if k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        return pivot #相等


    
class MaxHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count-1)  # 维持堆的特性

    def _siftup(self, ndx):
        if ndx > 0:
            parent = int((ndx-1)/2)
            if self._elements[ndx] > self._elements[parent]:    # 如果插入的值大于 parent，一直交换
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftup(parent)    # 递归
                
    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]    # 保存 root 值
        self._count -= 1
        self._elements[0] = self._elements[self._count]   # 最右下的节点放到root后siftDown
        self._siftdown(0)    # 维持堆特性
        return value
    
    def _siftdown(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        # determine which node contains the larger value
        largest = ndx
        if (left < self._count and     # 有左孩子
                self._elements[left] >= self._elements[largest] and
                self._elements[left] >= self._elements[right]):  # 原书这个地方没写实际上找的未必是largest
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx]
            self._siftdown(largest)
