# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:03:18 2019

@author: liuga
"""

#空间优化 时间复杂度O(N*N), 空间复杂度O(N)， 计算dp[i][j] 时，只用到了下一行的dp[i + 1][j] 和 dp[i + 1][j + 1]
#可以把i的维度去掉，dp初始化为最下面一层 从下往上
#时间复杂度O(n*n) 空间复杂度O(n)
class Solution(object):
    def minimumTotal(self, triangle):
        
        n = len(triangle)
        dp = triangle[-1]
        
        for i in range(n-2, -1, -1): #从倒数第二层开始遍历
            for j in range(i+1):     #最大取i
                dp[j] = min(dp[j],dp[j+1]) + triangle[i][j] 
                
        return dp[0]
    
    #最后一行开始递推，dp[i][j]表示从点(i,j)到底边的最小路径和
    #dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j] 从底向上
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = [[0]*(n+1) for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(i+1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]


#动态规划降维： 状态转移方程，如果计算状态 dp[i][j] 需要的都是 dp[i][j] 相邻的状态，那么就可以使用状态压缩技巧

#如果自顶向下要考虑很多的边界条件  第 i 行有 i+1 个元素，它们对应的 j 的范围为 [0, i]
class Solution2(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = [[0]*n for _ in range(n)]
        #初始化三角形的顶点
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            #最左边的一列,只能上方
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            for j in range(1, i):
                #上一层取上方和左上方的最小值，再加上当前值
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            #最右边一列只能左上
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]

        return min(dp[n-1])

    '''
i根据奇偶性映射, i-1映射到另一个一维数组 O(2n)的空间复杂度
        n = len(triangle)
        dp = [[0]*n for _ in range(2)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            cur, pre = i%2, 1- i%2
            dp[cur][0] = dp[pre][0] + triangle[i][0]
            for j in range(1, i):
                dp[cur][j] = min(dp[pre][j-1], dp[pre][j]) + triangle[i][j]
            dp[cur][i] = dp[pre][i-1] + triangle[i][i]

        return min(dp[(n-1)% 2])
            

    '''

#上面方法的空间优化,时间复杂度O(n*n),空间复杂度O(n)
class Solution2(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = [0]*n
        dp[0] = triangle[0][0]

        for i in range(1, n):
            dp[i] = dp[i-1] + triangle[i][i]
            for j in range(i-1, 0, -1):  #注意这里是从右向左
                dp[j] = min(f[j-1], f[j]) + triangle[i][j]
            dp[0] += triangle[i][0]

        return min(dp)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        
        n = len(triangle)
        nums = triangle[-1][:]
        
        for i in range(n-2, -1, -1):
            for j in range(i+1): #跟后面的值有关，所以顺序，如果跟前面的值有关 比如 min(nums[j], nums[j-1]),必须倒序
                nums[j] = min(nums[j], nums[j+1]) + triangle[i][j]
        
        return nums[0]
