# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 22:07:41 2020

@author: liuga
"""
#类似的题 1365

#元素当时被插入list的index，同时也是这个元素的右侧有多少个元素小于他自己的个数。
'''[5 2 6 1] 从后往前扫描  输出[2,1,1,0]
list为空，插入1 index 0 [1]: 插入6, index是1[ 1, 6] 右侧有一个比它小

'''
import bisect

class Solution(object):
    def countSmall(self, nums):
        n = len(nums)
        ans = [None]*n
        tmp = []
        for i in range(n-1, -1, -1):
            t = nums[i]
            pos = bisect.bisect_left(tmp, t) #找到右边比当前值小的元素个数
            ans[i] = pos
            tmp.insert(pos, t)  #当前值加入有序数组中
        return ans

#Traverse from the back to the beginning of the array, maintain an sorted array of numbers have been visited.
#using binary search to find the first element in the sorted array which is larger or equal to target number
#the index where 2 should be inserted and is also the number smaller than 2. Then we insert 2 into the sorted array 

#归并求逆序数 merge sort
class Solution(object):
    def countSmaller(self, nums):
        def sort(enum):
            half = len(enum)/2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                m, n = len(left), len(right)
                i = j = 0
                while i < m and j < n:
                    if j == n or i < m and left[i][1] <= right[j][1]:
                        enum[i+j] = left[i]
                        smaller[left[i][0]] += j
                        i += 1
                    else:
                        enum[i+j] = right[j]
                        j += 1
            return enum
    smaller = [0]* len(nums)
    sort(list(enumerate(nums))
    return smaller
                

#Binary Index Tree 对树状数组+1操作，统计右侧小于当前元素的个数，对它们求和，(0, iNums[i])的区间和
#prefix sum of prefences
class Solution(object):
         def countSmaller(self, nums):
         idxes = {}
         for k, v in enumerate(sorted(set(nums)))
             idxes[v] = k + 1

         iNums = [idxes[x] for x in nums]
         ft = FenwickTree(len(iNums))
         ans = [0]*len(nums)
         for i in range(len(iNums)-1, -1, -1):
             ans[i] = ft.sum(iNums[i] - 1)
             ft.add(iNums[i], 1) #increase the count?
         return ans

class FenwichTree(object):
    def _init_(self, n):
         self.n = n
         self.sums = [0]*(n+1)

    def add(self, x, val):
         while x <= self.n:
             self.sum[x] += val
             x += self.lowbit(x)

    def lowbit(self, x):
         return x &(-x)

    def sum(self, x):
         res = 0
         while x > 0:
             res += self.sums[x]
             x -= self.lowbit(x)
         return res
         
         
         
