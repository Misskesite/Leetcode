# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:22:07 2019

@author: liuga
"""
from collections import defaultdict
#bucket sort
class Solution(object):
    def topkFrequent(self, nums, k):
        n = len(nums)
        cntDict = defaultdict(int)
        
        for i in nums:
            cntDict[i] += 1
            
        freqList = [[] for i in range(n+1)]
        for p in cntDict:
            freqList[cntDict[p]] += p
            ans = []
            for p in range(n, 0, -1):
                ans += freqList[p]
        return ans[:k]
            
        
#最小堆
import collections
import heapq
class Solution2(object):
    def topKFrequent(self, nums, k):
        dic = collections.Counter(nums)
        heap, ans = [], []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i))
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans

