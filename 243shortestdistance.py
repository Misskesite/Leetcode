# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:17:04 2020

@author: liuga
"""
#只遍历一遍数组
class Solution(object):
    def shortestdistance(self, words, word1,word2):
        size = len(words)
        index1, index2 =  -1, -1
        ans = size
        
        for i in range(size):
            if words[i]== word1:
                index1 = i
                
            elif words[i]== word2:
                index2 = i
                
            if index1 != -1 and index2 != -1:
                ans = min(ans, abs(index1-index2))
        return ans
