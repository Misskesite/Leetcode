# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:51:26 2020

@author: liuga
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        words = str.split('')
        if len(words) != len(pattern):
            return False
        return map(pattern.find, pattern) == map(words.index, words)


#时间复杂度O(m+n), 空间复杂度O(m+n)
class Solution2(object):
    def wordPattern(self, pattern, str):
        words = str.split('')
        if len(words) != len(pattern):
            return False

        dic1, dic2 = {}, {}
        for p, w in zip(pattern, str):
            if p not in dic1:
                dic1[p] = w
            elif dic1[p] != w:
                return False
            if w not in dic2:
                dic2[w] = p
            elif dic2[w] != p:
                return False
        return True


    def wordPattern2(self, pattern, s):
        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        charToWord, wordToChar = {}, {}
        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
               
        return True


