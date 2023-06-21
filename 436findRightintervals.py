# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:52:52 2020

@author: liuga
"""
#二分搜索 + 哈希
class Interval(object):
    def _init_(self, s = 0, e = 0):
        self.start = s
        self.end = e
        
class Solution(object):
    def findRightinterval(self, intervals):
        n = len(intervals)
        start_map = {interval.start: i for i,interval in enumerate(intervals)}
        start_list = [interval.start for interval in intervals] #[interval[0] for interval in intervals]
        res = []
        start_list.sort()
        
        for interval in intervals:
            pos = self.high_find(start_list, interval.end)
            res.append(start_map[start_list[pos]] if pos != -1 else -1)
        return res
    
    def high_find(self, array, v):
        lo = 0
        hi = len(array)-1
        first = -1
        
        while lo <= hi:
            mid = lo + (hi -lo)//2
            if array[mid] >= v:
                hi = mid -1
                first = mid
                
            else:
                lo = mid +1
        return first #lo = len(array) 说明没找到
    
#bisect_left 0  (neginf, a1] 1(a1, a2]
#bisect_right 0 (neginf, a1) 1[a1, a2)
import bisect
class Solution2(object):
    def findRightIntercals(self, intervals):
        intervals = sorted((e[0], i, e[1]) for i, e in enumerate(intercals))
        n = len(intercals)
        res = [0]*n
        for e in intervals:
            r = bisect.bisect_left(intervals, (e[2],)) #相同返回bisect_left
            res[e[1]] = intervals[r][1] if r < n else -1
        return res
        
    def findRightInterval(self, intervals):
        l = sorted((e.start, i) for i, e in enumerate(intervals))
        res = []
        for e in intervals:
            r = bisect.bisect_left(l, (e.end,)) #这里一定要用括号 
            res.append(l[r][1] if r < len(l) else -1)
        return res

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def binarySearch(nums: List[int], target: int):
            n = len(nums)
            left = 0
            right = n-1

            while left <= right:
                mid = (right - left) // 2 + left
                if target == nums[mid]:
                    return target
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            if left >= n: return float("inf")  # 找不到合适的右侧区间的情况
            return nums[left]
        
        starts = []  # 存所有的start
        ends = []  # 存所有的end
        for i in intervals:
            starts.append(i[0])
            ends.append(i[1])
        
        hashmap = {}  # 存储start的下标
        for i in range(len(starts)):
            hashmap[starts[i]] = i
        
        starts.sort()  # 排序以便于二分
        
        res = []
        for i in range(len(ends)):
            end = ends[i]
            val = binarySearch(starts, end)  # 二分找第一个大于等于end的元素
            if val == float("inf"): res.append(-1)
            else: res.append(hashmap[val])  # 根据值来添加下标
        
        return res

