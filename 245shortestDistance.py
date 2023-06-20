# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 14:11:47 2020

@author: liuga
"""

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        res = len(words)
        
        if word1 != word2:
            pos1, pos2 = -1, -1
            for i, word in enumerate(words):
                if word == word1:
                    pos1 = i
                elif word == word2:
                    pos2 = i
                if pos1 != -1 and pos2 != -1:
                    res = min(res, abs(pos1 - pos2))
        else:
            pos = -1
            for i , word in enumerate(words):
                if word == word1:
                    if pos != -1:
                        res = min(res, i - pos)
                    pos = i
        return res
    

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        n = len(wordsDict)
        minimum = n
        w1 = -1
        w2 = -1
        for i in range(n):
            if wordsDict[i] == word1:
                w1 = i
                if w2 != -1:
                    minimum = min(w1-w2,minimum)
            if wordsDict[i] == word2:
                w2 = i
                if w1 != -1 and w1 != w2:
                    minimum = min(w2-w1,minimum)
        return minimum
