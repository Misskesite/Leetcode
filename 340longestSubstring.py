# -*- codrng: utf-8 -*-
"""
Created on Tue Feb 11 12:12:22 2020

@author: lruga
"""
#类似于159 此方法为准？
from collections import defaultdict
class Solution(object):
    def longestSubstring(self, s, k):
        mp = collections.defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            mp[s[r]] += 1
            while len(mp) > k:
                mp[s[l]] -= 1
                if mp[s[l]] == 0:
                    del mp[s[l]]
                l += 1
            res = max(res,r - l +1)
        return res
                    
        
#滑动窗口  s = "eceba" k =2 -> output : 3(ece)        
class Solution2(object):
    def longestSubstring(self, s, k):
        mp = collections.defaultdict(int)
        l = 0
        r = 0
        counter = 0
        max_len = 0
        while r < len(s):
            if mp[s[r]] == 0:
                counter += 1
            mp[s[r]] += 1
            r += 1
            while counter > k:
                
                if mp[s[l]] == 1:
                    counter -= 1
                mp[s[l]] -= 1                
                l += 1
            max_len = max(max_len, r - l)
        return max_len


class Solution:
  def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    ans = 0
    distinct = 0
    count = Counter()

    l = 0
    for r, c in enumerate(s):
      count[c] += 1
      if count[c] == 1:
        distinct += 1
      while distinct == k + 1:
        count[s[l]] -= 1
        if count[s[l]] == 0:
          distinct -= 1
        l += 1
      ans = max(ans, r - l + 1)

    return ans
        
