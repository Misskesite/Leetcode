# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 23:18:29 2020

@author: liuga
"""
#使用和s1等长的滑动窗口判断，S2在这个窗口的字符的出现个数是否相等 时间复杂度O(n)
import collections
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s2) < len(s1):
            return False
        c = collections.Counter(s1)
        n = len(s1)
        l,r = 0, n-1
        s = collections.Counter(s2[l:r])
        while r < len(s2):
            s[s2[r]] +=1
            if s == c:
                return True
            s[s2[l]] -= 1
            if s[s2[l]] == 0:
                del s[s2[l]]
            l += 1
            r += 1
        return False
# particular substring in s2 is having the same number of characters as in the s1.
#create a hashmap with the count of every character in the string s1. Then we slide a window over the string s2 and decrease the counter for characters on the right

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1),len(s2)
        d1 = Counter(s1)
        d2 = Counter(s2[:n1-1])
        l = 0
        for r in range(n1-1,n2):
            d2[s2[r]] += 1
            if d1 == d2:
                return True
            d2[s2[l]] -= 1
            if d2[s2[r]] == 0:
                del d2[s2[j]]
            l += 1
        return False
    
#此法为主？        
class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:  # renamed s1 to p, s2 to s
        cnt = Counter(p)
        
        l = 0
        for r, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < 0:  # If number of characters `c` is more than our expectation
                cnt[s[l]] += 1  # Slide left until cnt[c] == 0
                l += 1
            if r - l + 1 == len(p):  # If we already filled enough `p.length()` chars
                return True
            
        return False
''''
Firstly, we count the number of characters needed in p string.
Then we sliding window in the s string:
Let l control the left index of the window, r control the right index of the window (inclusive).
Iterate r in range [0..n-1].
When we meet a character c = s[r], we decrease the cnt[c] by one by cnt[c]--.
If the cnt[c] < 0, it means our window contains char c with the number more than in p, which is invalid.
So we need to slide left to make sure cnt[c] >= 0.
If r - l + 1 == p.length then we already found a window which is perfect match with string 
'''
Input:s1 = "ab" s2 = "eidbaooo"
Output:True

Input:s1= "ab" s2 = "eidboaoo"
Output: False
