# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:04:12 2020

@author: liuga
"""
from collections import Counter

class Solution(object):
    def findAnagram(self, s, p):
        ans = []
        m = len(s)
        n = len(p)
        if m < n:
            return ans
        pc = Counter(p)
        sc = Counter(s[:n-1])
        
        i = 0
        for i in range(n-1, m):
            sc[s[i]] += 1
            if sc == pc:
                ans.append(i - n + 1)
            sc[s[i-n+1]] -= 1
            if sc[s[i-n+1]] == 0:
                del sc[s[i-n+1]]
        return ans
    
#滑动窗口
import collections
class Solution2(object):
    def findAnagram(self, s, p):
        
        counter = collections.Counter()
        m = len(s)
        n = len(p)
        
        pcount = collections.Counter(p)
        
        l, r = 0 ,0
        res = []
        while r < m:
            counter[s[r]] += 1
            if r -l +1 == n:
                if counter == pcount:
                    res.append(l)
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1
            r += 1
        return res    



from collections import Counter

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters 
                res.append(i-len(p)+1)   # append the starting index
            sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
        return res
