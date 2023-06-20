# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 21:10:18 2019

@author: liuga
"""

class Solution(object):
    def reversewords(self, s):
        s[:] = list(" ".join("".join(s).split(" ")[::-1]))
        
        
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        res = "".join(s).split(" ")[::-1]
        s[:] = list(" ".join(res))
