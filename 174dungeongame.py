# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 15:50:05 2019

@author: liuga
"""
#类似于64最小路径和,这里是怎么样在路径上损失最少的生命值。 但是这里有负值  前位置的血量是由右边和下边房间的可生存血量(更小的值)决定
#dp[i][j]有可能是0或者负数，这种情况骑士没法存活，骑士的最小血量是1, 要求初始状态血量最小值，就是要到达右下角之后血量为1
class Solution(object):
    def dungeonGame(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[1000 for i in range(m + 1)] for j in range(n + 1)]
        #dp[n−1][m−1] 转移需要用到的dp[n−1][m]和dp[n][m−1] 均为无效值，因此我们给这两个值赋值为 1
        #到达公主房间后，骑士火拼完的血量至少为1，那么此时公主房间的右边和下边房间里的数字我们就都设置为1，这样到达公主房间的生存血量就是1减去公主房间的数字和1相比较，取较大值
        dp[m][n-1] = 1
        dp[m-1][n] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] =  max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
        return dp[0][0]
    
    
#反向DP, dp[i][j]表示从[i,j]到终点需要的最小血量
#dungeon[i][j] == 0，那么，dp[i][j] = min(dp[i+1][j], dp[i][j+1])
#dungeon[i][j] < 0，那么，dp[i][j] = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
#dungeon[i][j] > 0，那么，dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
#统一起来  dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
class Solution2(object):
    def dungeonGame(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[1000 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1 :
                    dp[i][j] = max(1, 1 - dungeon[m-1][n-1]) #最后一个值?

                elif i == m-1:
                    dp[i][j] = max(1, dp[i][j+1] - dungeon[i][j])

                elif j == n-1:
                    dp[i][j] = max(1, dp[i+1][j] - dungeon[i][j])

                else:
                    dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])

        return dp[0][0]
                    

#降维 dp[j] = max(1, min(dp[j], dp[j + 1]) - dungeon[i][j]) 不停覆盖原有的值
class Solution3(object):
    def dungeonGame(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])

        dp = [float('inf')]*(n+1)

        dp[n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[j] = max(1, min(dp[j], dp[j+1]) - dungeon[i][j])

        return dp[0]

