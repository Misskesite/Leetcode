# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:50:13 2020

@author: liuga
"""
# canWin 这个函数的意思是 “在当前这种状态下，至少有一种选法，能够让他赢”。所以 1p 要看的是，是否存在这样一种情况，无论 2p 怎么选，都不会赢
#穷举所有的情况，用回溯法来解
class Solution(object):
    def flipgame(self, s):
        for i in range(1, len(s)):
            if s[i-1]=='+' and s[i]== '+' and not self.flipgame(s[:i]+ '--' + s[i+1:]): #not self.flipgame意思是在当前这种状态下，无论怎么选2p都不会赢
                return True
        return False

#此方法更好？
class Solution(object):
    def canWin(self, s):
        for i in range(len(s) - 1):
            if s[i:i+2] == "++":
                current = s[0:i] + "--" + s[i+2:]
                if not self.canWin(current):
                    return True

        return False

#此法为主
class Solution:
    def canWin(self, currentState: str) -> bool:
        if not currentState:
            return False
        memo = {}
        def dfs(s):
            if s in memo:
                return memo[s]
            
            for i in range(len(s)-1):
                if s[i] =='+' and s[i+1]=='+' and not dfs(s[:i]+'--'+s[i+2:]):
                    memo[s] = True
                    return True
            memo[s] = False
            return False

        return  dfs(currentState)
    
