# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:20:11 2020

@author: liuga
"""
#回溯 从0开始 二进制存储状态 1 << (n - 1) 表示n已被选 递归过程出现重复状态 先手选了3，后手选了5(或者先手选了5， 后手选了3)
class Solution(object):
    def canIwin(self, maxinteger, desiredtital):
        dp = dict()
        
        def search(muaion, total):
            for x in range(maxinteger,0,-1):
                if not state &(1 << (x-1)): #没有使用了
                    if total + x >= desiredtital:
                        dp[state] = True
                        return True
                    break
                
            for x in range(1, maxinteger + 1):
                if not state & (1 <<(x-1)):
                    nstate = state | (1 <<(x-1))
                    if nstate not in dp:
                        dp[nstate] = search(nstate, total+x)
                    if not dp[nstate]:
                        dp[nstate]= True
                        return True                    
            dp[state] = False #我选择任何数都不会赢，才返回false
            return False
                        
        if maxinteger >= desiredtital:
            return True
        if (1+maxinteger)*maxinteger < 2*desiredtital: #左边是求和
            return False
        return search(0,0)

#改写 此解法为主
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger: #先手选max稳赢
            return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False
        memo = {}

        
        def dfs(state, desiredTotal): #state位运算表示 数字的使用状态
            if state in memo:
                return memo[state]
            for i in range(1, maxChoosableInteger + 1): #遍历，找到能让我赢的数字i
                cur = 1 << i-1    #如果 state中 i 位置是0，数字 i 没有被使用，那么接下来就用数字 i
                if cur & state == 0: #没有被访问过
                    if  i >= desiredTotal or not dfs(cur | state, desiredTotal - i): ## 两种赢，要么我到目的了，要么你在后面的回合不可能赢，注意 当前和 + i，以及 数字i 被使用了
                        memo[state] = True
                        return True
            memo[state] = False
            return False
        
        return dfs(0, desiredTotal)  # 初始状态，当前和为0，所有数字都没有被使用
    


                        
                
#记忆化搜索 由于maxChoosableInteger 不会大于 20，所以可以使用一个int型的各个位标记是否使用, 比如1101 代表134被使用了
class Solution2:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:        
        if sum(i for i in range(1, maxChoosableInteger + 1)) < desiredTotal: #一定加这句，这种情况，2个都无法赢，防止后面对手输，自己赢这种误判
            return False

        @lru_cache(None)
        def dfs(state, curSum):
            for i in range(maxChoosableInteger):
                if not 1 << i & state: #state 最大为 1<< maxChoosableInteger -1 ？
                    if curSum + i + 1 >= desiredTotal or not dfs(1 << i | state, curSum + i + 1): #更新各个元素使用情况，将state的第i位（从低到高）标记为1
                        return True
            return False
        
        return dfs(0, 0)

#时间复杂度：O(2 ^ n * n) 空间复杂度：O(2 ^ n)
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger: #先手选max稳赢
            return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False

        @cache
        def dfs(state, cursum): #state位运算表示 数字的使用状态
            for i in range(1, maxChoosableInteger + 1): #遍历，找到能让我赢的数字i
                cur = 1 << i    #如果 state中 i 位置是0，数字 i 没有被使用，那么接下来就用数字 i
                if cur & state == 0: #没有被访问过
                    if cursum + i >= desiredTotal or not dfs(cur | state, cursum + i): ## 两种赢，要么我到目的了，要么你在后面的回合不可能赢，注意 当前和 + i，以及 数字i 被使用了
                        return True
            return False
        #dfs.cache_clear()
        return dfs(0, 0)  # 初始状态，当前和为0，所有数字都没有被使用
'''
暴力法 M个数进行permutation，然后进行evaluate O(M!)
优化：permutaion 优化成combination(顺序不重要)
1 memorization
2 use 1 bit to store solution
3 use a integer to represent the number(bit operation)
