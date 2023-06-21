# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:53:22 2020

@author: liuga
"""

import collections

class Solution(object):
    def kthDifferent(self, nums,k):
        answer = 0
        counter = collections.Counter(nums)
        for num in set(nums):
            if k >0 and num+k in counter:
                answer += 1
            if k == 0 and counter[num] > 1:
                answer += 1
        return answer
                
                
