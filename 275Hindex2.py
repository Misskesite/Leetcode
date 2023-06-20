# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 23:36:33 2020

@author: liuga
"""
#二分法 分割点右边的数值个数为 n - i，根据 H 指数 的定义，必然有 citations[i] >= n - i关系：
#代一些 corner case 来进行检验，比如 [], [0], [1,2] 这种最简便的例子。
class Solution(object):
    def hindex2(self, citations):
        n = len(citations)
        l = 0
        r = n-1
        h = 0
        while l <= r:
            mid = l + (r-l)//2 
            h = max(h, min(citations[mid], n-mid)) #改变mid，比较试探，寻找合适的h值
            if citations[mid] < n - mid:
                l = mid+1
            else:
                r = mid-1
        return h
    
#即对于citations[i]，h指数是 n-i. 要h最大，需要i最小，citations[i] + i(递增，可以使用二分法) >= n
class Solution2:
    def hIndex(self, citations):
        n = len(citations)
        left = 0; right = n - 1
        while left <= right: # 这里必须用<= ？ 不然[0]会失败
            mid = left + (right - left) // 2
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1
        return n - left



class Solution:
  def hIndex(self, citations: List[int]) -> int:
    l = 0
    r = len(citations)

    while l < r:
      m = (l + r) // 2
      if citations[m] >= len(citations) - m:
        r = m
      else:
        l = m + 1

    return len(citations) - l
