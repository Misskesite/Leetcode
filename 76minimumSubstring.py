# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:12:20 2019

@author: liuga
"""
from collections import defaltdict

class Solution(object):
    def minimumSubstring(self, s, t):
        #MAX_INT = 2147483647        #2**31 -1
        
        l = r = 0
        
        char_need = defaultdict(int)
        
        count_need = len(t)
        
        min_len = float('inf')
        min_start = 0
        
        for i in t:
            char_need[i] += 1
            
        while r < len(s):
            if char_need[s[r]] >0:
                count_need -= 1
            char_need[s[r]] -= 1
                
            r += 1
                
            while count_need == 0:  #滑动窗口包含了所有T元素
                if min_len > r - l:
                    min_len = r - l
                    min_start = l
                    
                # current window does not contain s[l] any more
   
                char_need[s[l]] += 1 # char_need数值为0刚好
                 #when some count in char_need is positive， it means there is char in t but not current window        
                if char_need[s[l]] > 0  #增加l 寻找新的滑动窗口.(char_need数值为负的，说明多余字符(不在t里面))
                    count_need += 1
                    
                l += 1
                    
         return "" if min_len == float('inf') else s[min_start: min_start + min_len]

#时间复杂度O(n)                    
from collections import defaultdict
class Solution2(object):
    def minimumSubstring(self, s, t):
        if not s or not t:
            return
        mp = defaultdict(int)
        for c in t:
            mp[c] += 1

        l , r = 0 , 0
        min_len = float('inf')
        counter = len(t)

        res = ""

        while r < len(s):            
            mp[s[r]] -= 1
            if mp[s[r]] >= 0: 
                counter -= 1
            r += 1
            while counter == 0:
                if min_len > r - l:
                    min_len = r - l
                    res = s[l:r]

                mp[s[l]] += 1
                if mp[s[l]] > 0: #不可缺少的字母?
                    counter += 1
                
                l += 1
        return res
                     
        
        
