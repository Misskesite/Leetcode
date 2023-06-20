# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 20:18:40 2020

@author: liuga
"""
#时间复杂度O(n*3) dp[i][j]依次以从i到j，里面的点作为分割点(猜的数) minimize the maximum loss you could possibly face 最糟糕的情况下付出的钱，保证赢
class Solution(object):
    def getmoneyAmount(self, n):
        dp =[[0]*(n+1) for _ in range(n+1)]
        for l in range(n, 0, -1):
            for r in range(l+1, n+1):
                dp[l][r] = min(i + max(dp[l][i-1], dp[i+1][r]) for i in range(l, r))
        
        return dp[1][n]
    
    
#递归方法 n = 10 数字范围[1,10] 输出16
class Solution2(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        return self.solve(dp, 1, n)

    def solve(self, dp, L, R): #取两边最大，保证游戏能玩下去。最小是比较每个分割点的需要的钱数，最小花费
        if L >= R: 
            return 0 #一个数字 直接猜对
        if dp[L][R]: 
            return dp[L][R]
        dp[L][R] = min(i + max(self.solve(dp, L, i - 1), self.solve(dp, i + 1, R)) for i in range(L, R + 1))
        return dp[L][R]


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        f = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                f[i][j] = j + f[i][j - 1]
                for k in range (i, j):
                    f[i][j] = min(f[i][j], k + max(f[i][k - 1], f[k + 1][j]))
        return f[1][n]


#top down
class Solution:
  def getMoneyAmount(self, n: int) -> int:
    # Dp(i, j) := min money you need to guarantee a win of picking i..j
    @functools.lru_cache(None)
    def dp(i: int, j: int) -> int:
        if i >= j:
            return 0

        ans = math.inf

        for k in range(i, j + 1):
           ans = min(ans, max(dp(i, k - 1), dp(k + 1, j)) + k)

        return ans

    return dp(1, n)

#改写 重复情况：先选1，后选2(先选2，后选1) dp[i][j] 表示从数字i到j之间猜中任意一个数字最少需要花费的钱数
  def getMoneyAmount(self, n: int) -> int:
      dp = [[0] * (n + 1) for _ in range(n + 1)]
      def dfs(i, j):
          if i >= j :
              return 0
           if dp[i][j] != 0:
               return dp[i][j]

           ans = math.inf

           for k in range(i, j + 1):
               ans = min(ans, max(dfs(i, k - 1), dfs(k + 1, j)) + k) #The cost is the maximum between the left side and the right side, Choose pivot which will cause minimum cost

           dp[i][j] = ans
           return ans
       return dp[1][n]

#To find out how much money I need to win the range lo..hi (the game starts with the range 1..n), I try each possible x in the range (except hi, which is pointless because hi-1 costs less and provides more information),
#calculate how much I need when using that x, and take the minimum of those amounts.

#Bottom-up dynamic programming:

def getMoneyAmount(self, n):
    need = [[0] * (n+1) for _ in range(n+1)]
    for lo in range(n, 0, -1): # n -> 1
        for hi in range(lo+1, n+1):
            need[lo][hi] = min(x + max(need[lo][x-1], need[x+1][hi])
                               for x in range(lo, hi))
    return need[1][n]
          
