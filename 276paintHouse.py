# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 10:21:43 2020

@author: liuga
"""
#n = 3, k =2 no more than 2 ajacent fence have same color
#第三根柱子要么跟第一个不是一个颜色，要么跟第二个不是一个颜色。 第一个格子k种，第二个k-1种
#相同部分颜色的刷法和上一个格子的不同颜色刷法相同，因为下一格的颜色和之前那个格子颜色刷成一样的即可，最后总共的刷法就是把不同和相同两个刷法加起来
class Solution(object):
    def painthouse(self, n, k):
        if n == 0:
            return 0
        same = 0
        diff = k
        for i in range(2,n+1):
            t = diff
            diff = (same + diff)*(k-1)
            same = t
        return same + diff

#n是列数
class Solution(self, n, k):
    def paintHouse(self, n, k):
        if n == 0:
            return 0
        if n == 1:
            return k
        same = k, diff = k*(k-1) #when n == 2
        for i in range(3, n+1):
            same, diff = diff, (same + diff)*(k-1) #颜色与上一步相同，颜色与上一步不同
            
        return same + diff
'''
规定了不能有超过连续两根柱子是一个颜色，也就意味着第三根柱子要么根第一个柱子不是一个颜色，要么跟第二根柱子不是一个颜色
'''
#跟上一步不同，跟上一步相同(跟上上步不同) 此法为主
class Solution(self, n, k):
    def paintHouse(self, n, k):
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k*k
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = k
        dp[2] = k*k

        for i in range(3, n+1):
            dp[i] = dp[i-1]*(k-1) + dp[i-2]*(k-1)

        return dp[n]            
