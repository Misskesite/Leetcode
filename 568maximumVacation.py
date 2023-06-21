# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:33:17 2020

@author: liuga
"""
#此法为主，从后往前？                        
#定义dp[i][j]表示目前在城市i,在第j周，获得的休假总日子数。最后从dp[i][0]找到最大值 (i in [0, n-1])
class Solution(object):
    def maxVacationdays(self, flights, days):
        n = len(flights)
        k = len(days[0])
        res = 0
        dp = [[0]*k for _ in range(n)]
        for j in range(k-1, -1, -1):
            for i in range(n): #i对应城市，每周都可以飞?
                dp[i][j] = days[i][j] #初始化
                for p in range(n): #上一周可能还在城市i，也可能在其他城市p, 城市p有直飞城市i的飞机，可以用上一个状态的值 dp[p][j+1] 来更新当前值dp[i][j]
                    if (i == p or flights[i][p]) and j < k-1: #从倒数第二周开始更新
                        dp[i][j] = max(dp[i][j], dp[p][j+1] + days[i][j])

                    if j == 0 and (i == 0 or flights[0][i]): #可以从0飞到其他城市
                        res = max(res, dp[i][0])
        return res


def maxVacationdays(self, flights, days):
        n = len(flights)
        k = len(days[0])
        dp = [[0]*(k+1) for _ in range(n)]
        for j in range(k-1, -1, -1):
            for i in range(n):
                dp[i][j] = days[i][j] + dp[i][j + 1]
                for p in range(n): 
                    if flights[i][p] == 1:
                        dp[i][j] = max(dp[i][j], dp[p][j+1] + days[p][j])

        return dp[0][0]

        
        
                              
#dp[i][j] = max(dp[i-1][k] + days[j][i])(if we can go from city k to city j) 从前往后算，上周从别的城市飞过来

#降到1维 dp[i]当前城市i获得最大假期数 dp[i] the maximum vacation days if you stay at city i at current week.
# dp[precity] = -1 -> precity is nor reachable
class Solution(object):
    def maxVacationdays(self, flights, days):
        n = len(flights)
        k = len(days[0])
        dp = [float('-inf')]*n
        dp[0] = 0

        for w in range(k):
            tmp = [float('-inf')]*n
            for city in range(n):
                for pre in range(n): #city = pre =0 说明在第一个城市
                    if city == pre or flights[pre][city] == 1:  #如何保证dp[pre] >=0?
                        tmp[city] = max(tmp[city], dp[pre] + days[city][w])
            dp = tmp
        return max(dp)

            

