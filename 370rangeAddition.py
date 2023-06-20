# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:38:38 2020

@author: liuga
"""

class Solution(object):
    def rangeAddition(self, length, updates):
        
        res = [0 for _ in range(length+1)]
        
        for update in updates:
            s,e,inc = update[0], update[1], update[2]
            res[s] += inc  #只处理第一位和最后一位
            res[e+1] -= inc
        
        for i in range(1, length):
            res[i] += res[i-1] #得到前缀和
        
        return res[::-1] #最后一位不要
#开头加 结尾减，最后累加和


#此解法为主 prefix sum
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0 for _ in range(length+1)]
        ans = []
        for update in updates:
            s,e,inc = update[0], update[1], update[2]
            res[s] += inc  #只处理第一位和最后一位
            
            res[e+1] -= inc
        s = 0
        for i in range(length):
            s += res[i] #得到前缀和
            ans.append(s)
        
        return ans 
