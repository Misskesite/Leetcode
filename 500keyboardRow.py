# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:09:03 2020

@author: liuga
"""
#建立映射，所有的字母都映射为一个值
class Solution(object):
    def findwords(self, words):
        
        rowdict = {}
        for c in "qwertyuiopQWERTYUIOP":
            rowdict[c] = 1
        for c in "asdfghjklASDFGHJKL":
            rowdict[c] = 2
        for c in "zxcvbnmZXCVBNM":
            rowdict[c] = 3
        res = []
        for word in words:
            if len(set(rowdict[c] for c in word)) == 1:
                res.append(word)
        return res   
        
        
            

class Solution:
  def findWords(self, words: List[str]) -> List[str]:
    ans = []
    rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]

    for word in words:
        lowerWord = set(word.lower())
        if any(lowerWord <= row for row in rows):
            ans.append(word)

    return ans
