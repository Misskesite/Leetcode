# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:47:48 2020

@author: liuga
"""
#dp[i] 硬币之和等于amount的组合数 对比377 class Solution(object):
    def coinChange(self, amount, coins):
        dp = [0]*(amount+1)
        dp[0] = 1          #不选任何硬币，金额和为0
        for coin in coins: #选择第k个硬币能凑成金额i的方案。 内外循环不能置换?
            for i in range(1,amount+1): #for i in range(coin ,amount+1):
                if coin <= i:
                    dp[i] += dp[i-coin] #选和不选当前硬币
        return dp[amount]

'''
amount = 5  coins [1，2，5]
5 = 5
5 = 2 + 2 + 1
5 = 2 + 1 + 1 + 1
5 = 1 + 1 + 1 +1 + 1

如果只有一个硬币的话，那么给定钱数的组成方式就最多有1种，就看此钱数能否整除该硬币值。当有两个硬币的话，组成某个钱数的方式就可能有多种
比如我们有两个硬币 [1,2]，钱数为5，那么钱数的5的组成方法是可以看作两部分组成，一种是由硬币1单独组成，那么仅有一种情况 (1+1+1+1+1)；
另一种是由1和2共同组成，说明组成方法中至少需要有一个2，所以此时先取出一个硬币2，然后只要拼出钱数为3即可，


dp[i][j] 表示用前i个硬币组成钱数为j的不同组合方法，我们采用的方法是一个硬币一个硬币的增加，每增加一个硬币，都从1遍历到 amount
对于遍历到的当前钱数j，组成方法就是不加上当前硬币的拼法 dp[i-1][j]，还要加上，去掉当前硬币值的钱数的组成方法，当然钱数j要大于当前硬币值，状态转移方程也在上面的分析中得到了：

dp[i][j] = dp[i - 1][j] + (j >= coins[i - 1] ? dp[i][j - coins[i - 1]] : 0)
'''
dp[i][j] 表示用前i个硬币组成钱数为j的不同组合方法
class Solution(object):
    def change(self, amount, coins):
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        
        dp[0][0] = 1
        for i in range(1, n+1):
            dp[i][0] = 1
            for j in range(1, amount+1):
                if j >= coins[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]] #不加上当前硬币的拼法 dp[i-1][j]，还要加上，去掉当前硬币值的钱数的组成方法
                else:
                    dp[i][j] = dp[i-1][j] 
        return dp[-1][-1]


#完全背包 这里是dp[i][j - coins[i-1]]， 如果是0/1 背包，则是dp[i-1]
