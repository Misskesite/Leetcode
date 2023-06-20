# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:53:40 2019

@author: liuga
"""
#用sliding window + hashtable 时间复杂度O(n) 这种方法更好
import collections
class Solution(object):
    def longestSubstring(self, s):
        n = len(s)
        if len(s) == 0:        
            return 0
        res = 0
        j = 0
        m = collections.defaultdict(int)
        for i in range(n):
            m[s[i]] += 1
            while j <= i and len(m) > 2:
                m[s[j]] -= 1
                if m[s[j]] == 0:
                    del m[s[j]]
                
                j += 1
            res = max(res, i - j +1) #少于2个？等于2个

        return res
                
                    

    
#滑动窗口   至少包含两个不同字符的最长子串 eceba -> 输出3(ece)
class Solution(object):    
     def lengthOfLongestSubstring(self, s):
         n = len(s)
         if len(s) == 0:        
            return 0
        
         table = collections.defaultdict()
        
         begin, end, max_len, cnt = 0 ,0 ,0, 0
         
         while end < n:                
             if table[s[end]] == 0:                
                 cnt += 1
             table[s[end]] += 1
             end += 1
            
             while cnt > 2:                
                 if table[s[begin]] == 1:                         
                         cnt -= 1           
                    
                 table[s[begin]] -= 1
                 begin += 1                     
             max_len = max(max_len, end - begin)
              
          return len;


        

        
