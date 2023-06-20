# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:44:31 2019

@author: liuga
"""

class Solution(object):
    def longestPrefix(self ,strs):
        if not strs :
            return ""
        longest = strs[0]
        for i in range (len(strs[0])):
            for str in strs:
                if len(str) <= i or strs[0][i] != str[i]:
                    return strs[0][:i]
            
        return strs[0]