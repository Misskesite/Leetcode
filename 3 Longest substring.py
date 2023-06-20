# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 11:35:15 2019

@author: liuga
"""     

#sliding window + hash
import collections
class Solution(object):
    def longestSubstring(self, s):
        if not s:
            return 0        
        n = len(s)
        l, r = 0 ，0 
       
        if n == 1:
            return 1

        counter = 0
        mp = collections.defaultdict()
        while r < n:
            if mp[s[r]] > 0:
                counter += 1
            mp[s[r]] += 1
            r += 1
            while counter > 0: #有重复字符？
                if mp[s[l]] > 1:
                    counter -= 1
                mp[s[l]] -= 1
                start += 1
            max_len = max(max_len, r -l)
        return max_len
                    
            


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        count = Counter()

        l = 0
        for r, c in enumerate(s):
            count[c] += 1
            while count[c] > 1:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans
        
