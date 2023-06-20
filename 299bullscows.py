# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 20:50:40 2020

@author: liuga
"""
import collections
class solution(object):
    def bullscows(self, secret, guess):
        bulls = 0
        cows = 0
        dict = collections.defaultdict(int)
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                dict[s] += 1
        for i, g in enumerate(guess):
            if secret[i] != guess[i] and dict[g]:
                cows += 1
                dict[g] -= 1
        return str(bulls) + "A" + str(cows) + "B"
                
            
                
class Solution(object):
    def getHint(self, secret, guess):
        s1, s2 = collections.defaultdict(), collections.defaultdict()
        A = B = 0
        for s, g in zip(secret, guess):
            if s == g :
                A += 1
            else:
                s1[s] += 1
                s2[g] += 1

        for k in s1.keys():
            if k in s2:
                B += min(s1[k], s2[k])

        return "%sA%sB" % (A, B)
    

