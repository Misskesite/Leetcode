# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 16:37:50 2020

@author: liuga
"""

class Solution(object):
    def reverseWords(self,s):
        return ' '.join([ss[:-1] for ss in s.split(' ')])