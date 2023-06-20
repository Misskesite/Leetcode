# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 22:03:08 2020

@author: liuga
"""

class Solution(object):
    def randomNote(self, randomnote, magazine):
        for i in randomnote:
            if i in magazine:
                magazine = magazine.replace(i,'',1)
            else:
                return False
        return True
    


class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
      count1 = collections.Counter(ransomNote)
      count2 = collections.Counter(magazine)
      return all(count1[c] <= count2[c] for c in string.ascii_lowercase)
