# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:10:40 2019

@author: liuga
"""

class Solution(object):
    def zigZag(self, s, numRows):
        if numRows == 1:
            return s
        ans = ""
        interval = 2 *(numRows -1)
        for i in range(0, len(s), interval):
            ans += s[i]
            
        for row in range(1,numRows-1):
            inter = 2 * row
            i = row
            while i < len(s):
                ans += s[i]
                inter = interval - inter
                i += inter                
                
                for i in range(numRows-1,len(s),interval):
                    ans+=s[i]
        return ans
    
