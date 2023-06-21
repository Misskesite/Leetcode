# -*- coding: utf-8 -*-
"""
Created on Fri May 15 16:02:59 2020

@author: liuga
"""

class Solution(object):
    def detectCapital(self,word):
        return word[1:].islower() or word.islower() or word.isupper()
    
        