# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:16:53 2020

@author: liuga
"""
#数学方法 o(n) 从5开始，数字都需要先拆出所有的3，一直拆到剩下一个数为2或者4，因为剩4就不用再拆了，拆成两个2和不拆没有意义
class Solution(object):
    def integerBreak(self,n):
        if n == 2:
            return 1
        if n == 3:
            return 2
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res*n


#O(n*2) dp[i] 表示数字i拆分为至少两个正整数之和的最大乘积. dp[i]=max(dp[i−2]∗2,dp[i−3]∗3) 乘积为2^n * 3^m

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            # 假设对正整数 i 拆分出的第一个正整数是 j（1 <= j < i），则有以下两种方案：
            # 1) 将 i 拆分成 j 和 i−j 的和，且 i−j 不再拆分成多个正整数，此时的乘积是 j * (i-j)
            # 2) 将 i 拆分成 j 和 i−j 的和，且 i−j 继续拆分成多个正整数，此时的乘积是 j * dp[i-j]
            for j in range(1, i - 1): #j≥4 时，计算dp[i] 只需要考虑 j×dp[i−j]，不需要考虑j×(i−j)

                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n]


'''
当一个数分解成两部分后，其中一部分仍有分解的必要时，进行分解可以使得乘积变大
'''
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = max(2 * (i - 2), 2 * dp[i - 2], 3 * (i - 3), 3 * dp[i - 3])
        
        return dp[n]

'''
数字4拆成 2+2，乘积最大，为4。

数字5拆成 3+2，乘积最大，为6。

数字6拆成 3+3，乘积最大，为9。

数字7拆为 3+4，乘积最大，为 12。

数字8拆为 3+3+2，乘积最大，为 18。

数字9拆为 3+3+3，乘积最大，为 27。

数字10拆为 3+3+4，乘积最大，为 36。
