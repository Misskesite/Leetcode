# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:47:57 2020

@author: liuga
"""

class Solution(object):
    def longestUncommonsequence(self,a,b):
        if a != b:
            return max(len(a), len(b))
        else:
            return -1
''''
一个长的序列一定不是一个短的序列的子序列
相同长度的序列只要有一个字符不同就不是子序列
