# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 23:17:43 2020

@author: liuga
"""

class Solution(object):
    def hindex(self, citations):
        n = len(citations)
        citations.sort()
        h = 0
        for i, c in enumerate(citations):
            h = max(h, min(n-i, c))
        return h
    
def hindex(self, citations):
    n = len(citations)

    citations.sort()

    for i, citation in enumerate(citations):
      if citation >= n - i:
        return n - i

    return 0


#排序+二分 最快
class Solution2(object):
    def hIndex(self, citations):        
        h = 0        
        n = len(citations)
        citations.sort()
        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l)/2
            h = max(h, min(citations[mid], n- mid))
            if citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid - 1
            
        return h
