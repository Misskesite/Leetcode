# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 20:54:37 2020

@author: liuga
"""

class Solution(object):
    def intersection(self,nums1,nums2):
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i]+1 if i in map else 1
        for j in nums2:
            if j in map and map[j]>0:
                res.append(j)
                map[j] =0
        return res
            

class Solution:
  def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    ans = []
    nums1 = set(nums1)

    for num in nums2:
      if num in nums1:
        ans.append(num)
        nums1.remove(num)

    return ans
