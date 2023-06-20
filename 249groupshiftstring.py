# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:28:17 2020

@author: liuga
"""
import collections

class Solution(object):
    def groupstrings(self, strings):
        groups = collections.defaultdict(list)
        for s in strings:
            groups[self.hashstr(s)].append(s)
        res  = []
        for key, val in groups.items():
            res.append(sorted(val))
            
        return res
    
    #计算与首字符差 key是可以转换的数字字符串 (0,1,2):['abc', 'bcd']
    
    def hashStr(self, s):
        base = ord[s[0]]
        hashcode = ""
        for i in range(len(s)):
            if ord[s[i]]- base >= 0:
                '''
            for char in s:
                hashcode += (ord(char) - ord(s[0]))%26

            groups[hashcode].append(s)
                

                '''
                hashcode += chr(ord('a') + ord(s[i])- base )
            else:
                hashcode += chr(ord('a') + ord(s[i])- base + 26 )
        
        return hashcode
    
#chr() return unicode string


class Solution:
  def groupStrings(self, strings: List[str]) -> List[List[str]]:
    keyToStrings = defaultdict(list)

    # 'abc' . '11' because diff(a, b) = 1 and diff(b, c) = 1
    def getKey(s: str) -> str:
      key = ''

      for i in range(1, len(s)):
        diff = (ord(s[i]) - ord(s[i - 1]) + 26) % 26
        key += str(diff) + ',' #必须用，分开，不然abc(012) 和am（012相同）

      return key

    for s in strings:
      keyToStrings[getKey(s)].append(s)

    return keyToStrings.values()


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        keyToStrings = defaultdict(list)
        def getKey(s):
            key = ''
            for i in range(1, len(s)):
                key += str((ord(s[i]) - ord(s[0]) + 26)%26) + '-'
            return key
        
        for s in strings:
            keyToStrings[getKey(s)].append(s)
        return keyToStrings.values()
