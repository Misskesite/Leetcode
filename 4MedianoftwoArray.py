# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 16:24:13 2019

@author: liuga
"""
#O(log(m+n))
class Solution(object):
    def getKth(self, nums1,nums2,k):
        lenA = len(nums1)
        lenB = len(nums2)
        
        if lenA > lenB:
            return self.getKth(nums2,nums1,k) #保证第二个数组长
        
        if lenA == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0],nums2[0])
        pa = min(k//2, lenA) #逐渐删掉一半
        pb = k-pa
        
        if nums1[pa-1] <= nums2[pb-1]:
            return self.getKth(nums1[pa:], nums2, pb)
        else:
            return self.getKth(nums1, nums2[pb:], pa)
        
    def medianTwoarray(self, nums1, nums2):
        lenA = len(nums1)
        lenB = len(nums2)
        
        if (lenA +lenB) %2 == 1:
            return self.getKth(nums1, nums2, (lenA+lenB)//2 +1)
        
        else:
            return (self.getKth(nums1, nums2, (lenA+lenB)//2 ) + self.getKth(nums1, nums2, (lenA+lenB)//2 +1)) / 2

