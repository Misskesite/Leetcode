# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:15:36 2020

@author: liuga
"""
#s = "abpcplea", dictionary = ["ale","apple","monkey","plea"] 输出 apple
#我们从前往后匹配时，可以发现每次贪心地匹配最靠前的字符是最优决策

import collections

class Solution(object):
    def findLongest(self,s,d):
        ans = []
        dmap = collections.defaultdict(list)
        for w in d:
            dmap[w[0]].append((0,w))
        for c in s:
            wlist = dmap[c]
            del dmap[c]
            for i,w in wlist:
                if i+1 == len(w):
                    ans.append(w)
                else:
                    dmap[w[i+1]].append((i+1,w))
        if not ans:
            return ''
        max1 = len(max(ans,key=len))
        return min(w for w in ans if len(w) == max1)
    
                
#双指针+贪心 O(d*(m+n)) d是字典长度，m是s长度，n字典中字符串的平均长度。我们需要遍历d个字符串，判断该字符串是不是s的子序列
class Solution(object):
    def findLongest(self, s, dictionary):
        res = ""
        for t in dictionary:
            i = j = 0
            while i < len(t) and j < len(s):
                if t[i] == s[j]:
                    i += 1
                j += 1
            if i == len(t):
                if len(t) > len(res) or len(t) == len(res) and t < res: #当前长度最长，字典序最小
                    res = t
        return res
            

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x)) #字符串长度降序，字典序的升序，从前往后找第一个满足条件的
        for t in dictionary:
            i = j = 0
            while i < len(t) and j < len(s):
                if t[i] == s[j]:
                    i += 1
                j += 1
            if i == len(t):
                return t
        return ""

