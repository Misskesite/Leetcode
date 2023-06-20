# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:43:37 2019

@author: liuga
"""

class Solution(object):
    def fourSum(self, num, target):
        n = len(num)
        res = set()
        dict = {}
        
        if n < 4:
            return []
        num.sort()
        for p in range(n):
            for q in range(p+1, n):
                if num[p] + num[q] not in dict:
                    dict[num[p] + num[q]] = [(p,q)]
                    
                else:                        
                    dict[num[p] + num[q]].append((p,q))
                    
        for i in range(n):
            for j in range(i+1, n-2):
                T = target - num[i] -num[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j:# 不相等？
                            res.add(tuple(sorted(num[i],num[j],num[k[0]],num[k[1]])))
                                        
        return [list(i) for i in res]



    def fourSum(self, num, target):
        n = len(nums)
        seen = set()
        ans = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    lastNumber = target - nums[i] - nums[j] - nums[k]
                    if lastNumber in seen:
                        arr = sorted([nums[i], nums[j], nums[k], lastNumber])
                        ans.add((arr[0], arr[1], arr[2], arr[3]))
            seen.add(nums[i])
        return ans
    
