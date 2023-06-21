# -*- coding: utf-8 -*-
"""
Created on Mon May 18 21:16:25 2020

@author: liuga
"""
import collections

class Solution(object):
    def uncommon(self, parent, child): #检测一个是另一个的子序列？
        lp,lc = len(parent), len(child)
        pp, pc = 0,0
        while pp < lp and pc < lc:
            if parent[pp] == child[pc]:
                pc+=1
            pp += 1
        return pp != pc
    
    def longestSequence(self, strs):
        cnt = collections.Counter(strs)
        slist = sorted(set(strs), key = len, reverse = True)
        for i, c in enumerate(slist):
            if cnt[c] > 1 :
                continue
            if all(self.uncommon(p,c) for p in slist[:i]):
                return len(c)
        return -1
    
#此解法为主    
def findLSUlength(self, strs):
    def subseq(w1, w2):
        if len(w1) > len(w2):
                return False
        i = 0
        for c in w2:
            if i < len(w1) and w1[i] == c:
                i += 1
        return i == len(w1)
        
    A.sort(key = len, reverse = True)
    for i, word1 in enumerate(A):
        if all(not subseq(word1, word2) 
                for j, word2 in enumerate(A) if i != j): #字符串也是自己的子序列，找其它包含它的序列？ 没有 。 [abcde, abcfg, abchi] 答案是5
            return len(word1)
    return -1
#We want the max length of all candidates with the desired property, so we check candidates in descending order of length. When we find a suitable one, we know it must be the best global answer.
#We only need to check whether X is not a subsequence of any of the other words Y. To save some time, we could have quickly ruled out Y when len(Y) < len(X),
#either by adding "if len(w1) > len(w2): return False" or enumerating over A[:i] (and checking neighbors for equality.) 
            
#strs = ["aba","cdc","eae"] 输出3        
from collections import Counter        
class Solution2(object):
    def findLSUlength(self, strs):        
        def subseq(a,b):
            if not (len(a) <= len(b) and set(a) <= set(b)):
                return False
            i = 0
            n = len(a)
            for c in b:
                if i < n :
                    if c == a[i]:
                        i+=1
                else:
                    break
            return i == n
    
        c = Counter(strs) #字典去重？
        dstrs = sorted(c.keys(), key = len, reversed = True)
        
        for i, w in enumerate(dstrs):
            if c[w] == 0 and all(not subseq(w, s) for s in dstrs[:i]): #没有重复的
                return len(w)
        return -1
        

#可以利用集合的去重复特性    
class Solution:
  def findLUSlength(self, strs: List[str]) -> int:
    def isSubsequence(a: str, b: str) -> bool:
        i = 0
        j = 0

        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
            j += 1

        return i == len(a)

    seen = set()
    duplicates = set()

    for s in strs:
      if s in seen:
        duplicates.add(s)
      seen.add(s)

    strs.sort(key=lambda s: -len(s))

    for i in range(len(strs)):
        if strs[i] in duplicates:
            continue
        isASubsequence = False
        for j in range(i):
            isASubsequence |= isSubsequence(strs[i], strs[j])
        if not isASubsequence:
            return len(strs[i])

    return -1
