# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:49:13 2020

@author: liuga
"""

class Solution(object):
    def kdifferenceTree(self, nums, k):
        if k < 0:
            return
        vis = set()
        diff = set()
        for i in nums:
            if i - k in vis:
                diff.add(i -k)
            if i + k in vis:
                diff.add(i)
            vis.add(i)
        return len(diff)

    
#k不小于k
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        numDict = {}
        for i in nums:
            numDict[i] = numDict.get(i, 0) + 1
        res = 0
        for key in numDict.keys():
            if k == 0:
                if numDict[key] > 1:
                    res += 1
            elif k > 0:
                if numDict.get(k+key) is not None:
                    res += 1
            else:
                break
        return res
