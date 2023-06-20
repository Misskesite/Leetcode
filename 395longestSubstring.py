# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:10:47 2020

@author: liuga
"""
#递归
class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) <k:
            return 0
        for c in set(s):
            if s.count(c) <k:
                return max(self.longestSubstring(t,k) for t in s.split(c))
        return len(s)


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:        
        if s == [] or k > len(s):
            return 0
        freq = collections.Counter(s)
        for i, char in enumerate(s):
            if freq[char] < k:
                return max(self.longestSubstring(s[:i], k),  self.longestSubstring(s[i+1:], k)) # we use all the infrequent elements as splits
        return len(s)

#If every character appears at least k times, the whole string is ok. Otherwise split by a least frequent character
#(because it will always be too infrequent and thus can't be part of any ok substring) and make the most out of the splits.
    
#滑动窗口
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        sz = len(s)
        ans = 0
        for kind_limit in range(1,27): #窗口字符种类的上限，用来限制窗口的长度
            total = 0     #窗口内字符种类
            sat_total = 0 #满足出现次数不少于k的条件，窗口内字符种类
            right = 0
            left = 0
            window = collections.defaultdict(int)

            while right < sz:
                window[s[right]] += 1
                if window[s[right]] == 1:
                    total += 1
                if window[s[right]] == k:
                    sat_total += 1

                #当种类超过限制时， 左边界收缩
                while total > kind_limit:
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        total -= 1
                    if window[s[left]] == k-1:
                        sat_total -= 1
                    left += 1

                #窗口内字符种类等于满足条件的字符种类时
                if total == sar_total:
                    ans = max(ans, right - left + 1)

                right += 1
            return ans
    

def longestSubstring(self, s: str, k: int) -> int:
    res = 0
    for n_c in range(1, len(Counter(s))+1):
          
        found = 0
        dct = defaultdict(int)
        start = 0
        for end in range(len(s)):
            
            c = s[end]
            dct[c] += 1
            if dct[c] == k:
                found += 1

            while len(dct) > n_c:
                c = s[start]
                start += 1
                dct[c] -= 1
                if dct[c] == k-1:
                    found -= 1
                if dct[c] == 0:
                    del dct[c]

            if len(dct) == n_c and found == n_c:
                res = max(res, end-start+1)
                        
    return res

Basically iterate through the number of possible unique letters 1 to 26. Lets call our target amount of unique letters u
We expand, if our number of unique letters is less than or equal to u, we need to add a letter, so we increment the right pointer, and add the count of the right letter by 1. If the count is equal to 1 we know this is a new letter so we increment unique
We shorten, if our number of unique letters is more than u , we need to remove a letter, so we decrement the left pointer, and decrease the count of the left letter by 1. If the count is equal to 0 we decrement the number of unique letters 
