# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 22:43:25 2020

@author: liuga
"""

class Solution(object):
    def maxproduct(self, words):
        word_dict = {}
        for word in words:
            word_dict[word] = set(word)
        max_len = 0
        for i1, w1 in enumerate(words):
            for i2 in range(i1+1, len(words)):
                w2 = words[i2]
                if not (word_dict[w1] & word_dict[w2]):
                    max_len = max(max_len, len(w1)*len(w2))
        return max_len

class Solution2(object):
    def maxProduct(self, words):
        d = defaultdict(int)
        ans = 0
        ''' he通过以下位运算获得
        def hashset(word):
            # 用26位位运算表示二十六个字母在word中被使用的情况
            return sum(1 << (ord(c) - ord('a')) for c in set(word))
        '''
        fow w in words:
            s = set(w)
            he = "".join(sorted(s)) #拼接后的字符串作为哈希值
            if d[he] < len(w):
                for other in d:
                    #取出来的字符串再取集合。集合没有交集才能作为答案
                    if not (set(other) & s):
                        ans = max(ans, len(w)* d[other])

                d[he] = len(w)
        return ans


class Solution:
  def maxProduct(self, words: List[str]) -> int:
    ans = 0

    def getMask(word: str) -> int:
      mask = 0
      for c in word:
        mask |= 1 << ord(c) - ord('a')
      return mask

    masks = [getMask(word) for word in words]

    for i in range(len(words)):
      for j in range(i):
        if not (masks[i] & masks[j]):
          ans = max(ans, len(words[i]) * len(words[j]))

    return ans
