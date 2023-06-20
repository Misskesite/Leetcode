# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:04:41 2019

@author: liuga
"""
#时间复杂度O(m+n), 原地修改
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k = m + n -1
        p = m - 1
        q = n - 1
        
        while p >= 0 and q >= 0:
            if nums1[p] > nums2[q]:
                nums1[k] = nums1[p]
                p -= 1
            else:
                nums1[k] = nums2[q]
                q -= 1
            k -= 1
            
        while q >= 0:
            nums1[k] = nums2[q]
            q -= 1
            k -= 1


                
                
            
        
        
