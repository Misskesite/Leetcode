# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:33:54 2020

@author: liuga
"""

class Solution(object):
    def reversevowel(self, s):
        res = list(s)
        vowel = []
        for i in range(len(s)):
            if res[i] in ['a','e','0','i','u','A', 'O', 'E', 'I', 'U']:
                vowel.append(i,res[i])
        for j in range(len(vowel)/2):
            res[vowel[j][0]] = vowel[len(vowel)-j-1][1]
            res[vowel[len(vowel)-j-1]][0] = vowel[j][1]
        return '.'.join(res)
            

class Solution:
  def reverseVowels(self, s: str) -> str:
    charList = list(s)
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    l = 0
    r = len(s) - 1

    while l < r:
      while l < r and charList[l] not in vowels:
        l += 1
      while l < r and charList[r] not in vowels:
        r -= 1
      charList[l], charList[r] = charList[r], charList[l]
      l += 1
      r -= 1

    return ''.join(charList)
