# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 10:58:31 2020

@author: liuga
"""
import collections
#奇数个数> 1
class Solution(object):
    def panlindrom(self, s):
        count = collections.Counter(s)
        flag = 1
        for char in count:
            if count[char]%2==0:
                flag -= 1
                if flag < 0:
                    return False
        return True
        
