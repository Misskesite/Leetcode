# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:54:30 2019

@author: liuga
"""

class Solution(object):
    def panlinDrome(self,x):
        if x < 0:  #负数
            return False
        x = str(x)
        N = len(x)
        
        for i in range(N/2):
            if x[i] != x[N -1 -i] :
                return False
        return True
            
