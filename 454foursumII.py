# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:16:21 2020

@author: liuga
"""

import collections

class Solution(object):
    def foursum(self, A,B,C,D):
        count  = collections.Counter(a+b for a in A for b in B)
        return sum(count[-c-d] for c in C for d in D)

#Time O(n*n)
class Solution2(object):
    def fourSums(self, A, B, C, D):
        mp = colelctions.defaultdict()
        for a in A:
            for b in B:
                mp[a+b] += 1

        res = 0
        for c in C:
            for d in D:
                res += mp[-c-d]

        return res
