# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:31:11 2020

@author: liuga
"""

class Solution(object):
    @lru_cache(None)
    def integerreplacement(self, n):
        if n == 1:
            return 0
        if n%2 ==0:
            return 1 + self.integerreplacement(n/2)
        else:
            return 1 + min(self.integerreplacement(n+1), self.integerreplacement(n-1)) #+1当心溢出


class Solution:
    def integerReplacement(self, n: int) -> int:
        @lru_cache(None)
        def dfs(n):
            if n == 1:
                return 0
            ans = 0
            return ans + (dfs(n // 2) + 1) if n % 2 == 0 else (min(dfs(n + 1), dfs(n - 1)) + 1)
        return dfs(n)


class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = dict() # 记忆

        def recur(n):
            if n in memo: # 先查记忆
                return memo[n]
            if n == 1: # 出递归的条件
                return 0
            if n < 0: # 这一个判断写不写都行，只是我习惯加了，当题目改成n-2,n+2的时候，这个越界判断就有用了
                return 0xffffffff # 
            if n % 2 == 0:
                memo[n] = recur(n//2) + 1
                return memo[n]
            elif n % 2 == 1:
                memo[n] = min(recur(n+1),recur(n-1)) + 1
                return memo[n]
        
        return recur(n)


