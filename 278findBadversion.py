# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:28:57 2020

@author: liuga
"""

class Solution(object):
    def findbadVersion(self, n):
        left = 1
        right = n
        while True:
            mid = (left + right)/2
            if isBadVersion(mid):
                if mid == 1 or not isBadVersion(mid-1):
                    return mid
                right = mid-1
            else:
                left = mid +1


class Solution:
  def firstBadVersion(self, n: int) -> int:
    l = 1
    r = n

    while l < r:
      m = (l + r) >> 1
      if isBadVersion(m):
        r = m
      else:
        l = m + 1

    return l
