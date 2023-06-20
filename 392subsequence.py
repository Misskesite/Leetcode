# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:47:26 2020

@author: liuga
"""
#原字符删除一些(或者不删除)，不改变剩余字符的相对位置 s = "abc" t = "ahbgdc"
import collections

class Solution(object):
    def issequence(self, s, t):
        queue = collections.deque(s)
        for c in t:
            if not queue:
                return True
            if c == queue[0]:
                queue.popleft()
        
        return not queue

#双指针
class Solution(object):
    def isSequence(self, s, t):
        n = len(s)
        m = len(t)
        while i < n and j < m:
            if s[i] == s[j]:
                i += 1
            j += 1    #不匹配，j右移，i不变
        return i == n
