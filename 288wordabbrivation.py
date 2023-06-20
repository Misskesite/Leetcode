# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:39:45 2020

@author: liuga
"""
#当缩写一致的时候，字典中的单词均和给定单词相同时，返回 true，建立hashset,把缩写的相同单词放在一个hashset里面，给定单词缩写的hashset里面单词个数和元素总个数相同
from collections import defaultdict

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dic = defaultdict(list)
        self.visit = set(dictionary)
        for word in dictionary:
            k = word
            if len(word)> 2:
                k = word[0] + str(len(word)-2) + word[-1]
            self.dic[k].append(word)
            

    def isUnique(self, word: str) -> bool:
        s = ""
        if len(word) > 2:
            s = word[0] + str(len(word)-2) + word[-1]
        if s not in self.dic:
            return True
        if len(self.dic[s]) == 1 and word in self.visit: #缩写已经存在字典中，也在set中，说明就是字典中的字符。如果不在，有重复的缩写
            return True
        return False


#list.count(value)
from collections import Counter
class Solution(object):
    def wordAbbrivation(self, dictionary, tword):
        
        dict = defaultdict(list)
        for word in dictionary:
            k = word
            if len(word)> 2:
                k = word[0] + str(len(word)-2) + word[-1]
            dict[k].append(word)

        s = tword
        if len(tword) > 2:
            s = tword[0] + str(len(tword)-2) + tword[-1]

        #return list(dict[s]).count(tword) == len(dict[s])
        return Counter(dict.values())[towrd] == len(dict[s])

class ValidWordAbbr:
  def __init__(self, dictionary: List[str]):
    self.dictset = set(dictionary) #key 对应的word只有一个？
    # T := unique, F := not unique
    self.abbrUnique = {}

    for word in self.dict:
      abbr = self._getAbbr(word)
      self.abbrUnique[abbr] = abbr not in self.abbrUnique #里面已经有映射的值？

  def isUnique(self, word: str) -> bool:
    abbr = self._getAbbr(word)
    return abbr not in self.abbrUnique or self.abbrUnique[abbr] and word in self.dictset

  def _getAbbr(self, s: str) -> str:
    n = len(s)
    if n <= 2:
      return s
    return s[0] + str(n - 2) + s[-1]
