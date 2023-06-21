# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 20:38:52 2020

@author: liuga
"""
#双指针，当前字符串中的出现次数最多的字母个数+K > 串长度
import collections

class Solution(object):
    def longestRepeate(self, s, k):
        
        table = collections.Counter()
        res = 0
        p1 = p2 = 0
        while p2 < len(s):
            table[s[p2]] +=1
            p2 += 1
            while p2 - p1 - max(table.values()) > k:
                table[s[p1]] -= 1
                p1 += 1
            res = max(res, p2 - p1)
        return res
        
#此法为主
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]]) #效率更高
            if maxf + k < r - l + 1:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
