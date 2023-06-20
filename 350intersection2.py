# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:00:04 2020

@author: liuga
"""
#首先遍历较短的数组
class Solution(object):
    def intersection(self,nums1,nums2):
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i]+1 if i in map else 1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] -= 1
        return res

#O(m+n)
class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) > len(nums2):
      return self.intersect(nums2, nums1)

    ans = []
    count = Counter(nums1)

    for num in nums2:
      if count[num] > 0:
        ans.append(num)
        count[num] -= 1

    return ans


class Solution(object):
    def intersection(self, nums1, nums2):
        inter = set(nums1) & set(nums2)
        res = []
        for i in inter:
            res += [i] * min(nums1.count(i), nums2.count(i))
        return res
