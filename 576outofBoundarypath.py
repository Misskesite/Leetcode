# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:54:00 2020

@author: liuga
"""
#类似于62，63，688
#从边界往里算，算到出发点
class Solution(object):
    def findPath(self, m, n, N, i, j): #N是maxmove,(i,j)是起始点坐标
        dp = [[[0] * n ] for _ in range(m)] for _ in range(N + 1)]
        for k in range(1, N+1): #走的步数
            for x in range(m):
                for y in range(n):
                    v1 = 1 if x == 0 else dp[k - 1][x - 1][y] #x取边界值一步出界，为1
                    v2 = 1 if x == m - 1 else dp[k - 1][x + 1][y]
                    v3 = 1 if y == 0 else dp[k - 1][x][y - 1] #y取边界为1
                    v4 = 1 if y == n - 1 else dp[k - 1][x][y + 1]
                    dp[k][x][y] = (v1 + v2 + v3 + v4) % (10**9 + 7)
        return dp[N][i][j]

    #可以简化空间
    def findPath(self, m, n, N, i, j):
        MOD = (10**9 + 7)
        dp = [[0] * n for _ in range(m)]

        for s in range(1, N+1):
            curStatus = [[0] * n for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    v1 = 1 if x == 0 else dp[x - 1][y]
                    v2 = 1 if x == m - 1 else dp[x + 1][y]
                    v3 = 1 if y == 0 else dp[x][y - 1]
                    v4 = 1 if y == n - 1 else dp[x][y + 1]
                    curStatus[x][y] = (v1 + v2+ v3+ v4)% MOD
            dp = curStatus
        return dp[i][j]


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
		# define the dp array
        dp = [[[-1]*(maxMove+1) for _ in range(n+1)] for _ in range(m+1)]
        
        def solve(i, j, maxMove):
            if maxMove < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            
			# if the dp array at this position contains some value(not -1) then it means it has been computed earlier
			# so we don't need to compute again, hence return whatever value is present in dp.
            if dp[i][j][maxMove] != -1:
                return dp[i][j][maxMove]
            
			# otherwise compute the value
            a = solve(i-1, j, maxMove - 1)
            b = solve(i+1, j, maxMove - 1)
            c = solve(i, j-1, maxMove - 1)
            d = solve(i, j+1, maxMove - 1)
            
			# store the computed value in dp array so that we do not need to compute it again when the same input occurs again.
            dp[i][j][maxMove] = a + b + c + d
            return dp[i][j][maxMove]
        
        return solve(startRow, startColumn, maxMove) % 1000000007

    
    #改写 对于遍历到的每个位置，都遍历其四个相邻位置，如果相邻位置越界了，那么我们用当前位置的dp值更新结果res，因为此时dp值的意义就是从(i,j)到越界位置的路径数
    # 如果没有越界，我们将当前位置的dp值赋给t数组的对应位置 使用了BFS搜索，以(i, j)为起始点 最多移动N步
    def findPath(self, m, n, N, i, j):
        MOD = (10**9 + 7)
        dirs = [(1,0),(-1, 0),(0,1)(0,-1)]
        dp = [[0] * n for _ in range(m)]
        dp[i][j] = 1
        
        for k in range(1, N+1):
            t = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    for dir in dirs:
                        x = r + dir[0]
                        y = c + dir[1]
                        if x < 0 or x >= m or y < 0 or y >= n: #出界？
                            res = (res + dp[r][c])% MOD #r为0或者m-1, c为0或者n-1?
                        else:
                            t[x][y] = (t[x][y] + dp[r][c])%MOD
            dp = t
        return res
                    
'''
dp[i][j]表示到达当前位置的路径数量，初始化dp的时候把dp[startRow][startColumn] = 1，因为0步时只有1条路径到达出发点

然后开始按照移动次数来遍历，每次都用一个cur来存储遍历后的结果

对于每个点，如果该点为0，则说明在当前步数下没有能到达该点的路径，不用管

如果不为0，则判断其四个方向的点，如果某一点出界了，那就说明有dp[i][j]条路径可以出界，加到ans中；如果某一点没出界，那么就在cur中标记这个点有dp[i][j]条路径可以到达

遍历所有点后把dp = cur

'''

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7

        outCounts = 0
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        for i in range(maxMove):
            dpNew = [[0] * n for _ in range(m)]
            for j in range(m):
                for k in range(n):
                    if dp[j][k] > 0:
                        for j1, k1 in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
                            if 0 <= j1 < m and 0 <= k1 < n:
                                dpNew[j1][k1] = (dpNew[j1][k1] + dp[j][k]) % MOD #标记这一点有多少路径可以到达
                            else: #出界？ + 1 (dp[startRow][startColumn])
                                outCounts = (outCounts + dp[j][k]) % MOD
                                
            dp = dpNew
        
        return outCounts 
    

#dp存储走i步骤
class Solution2(object):
    def findPath(self, m, n, N, i, j):
        dp = [{} for _ in range(N+1)]
        dp[0][(i,j)] = 1
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        ans = 0
        for step in range(1, N+1):
            for r, c in dp[step-1]:
                count = dp[step-1][(r,c)] #(r,c)对应上面的x，y
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if nr >= m or nc >= n or nr < 0 or nc < 0:
                        ans += count #移动后的坐标超出边界就累加
                        ans %= (10**9 + 7)
                    elif (nr, nc) in dp[step]:
                        dp[step][(nr, nc)] += count
                    else:
                        dp[step][(nr,nc)] = count
        return ans
                        
                        

'''
dp[i]存储走i步后，小球可能在的位置，用set存储，这样不用每次都O(m*n)
dp[i+1]就是dp[i]所有可达位置的上下左右移动
若移动后的坐标超出边界，那么ans就累加



