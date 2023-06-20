# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:40:59 2020

@author: liuga
"""
#时间复杂度O(n)
import collections
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dic = collections.defaultdict(list)
        self.lenth = len(wordsDict)
        for i in range(self.lenth):
            self.dic[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = self.lenth
        for pos1 in self.dic[word1]:
            for pos2 in self.dic[word2]:
                res = min(res, abs(pos1- pos2))

        return res
