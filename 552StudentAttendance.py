# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:24:41 2020

@author: liuga
"""
#回溯的时间复杂度太高  类似于33？
#时间复杂度O(n) 空间复杂度O(n) dp[i] the numbe of all possible attendance(without 'A') with the length i
class Solution(object):
    def checkRecord(self,n):
        if n == 0:
            return 0
        if n == 1:
            return 3
        if n == 2:
            return 8
        
        MAX = 1000000007
        dp  = [1,2,4]
        i = 3
        while i < n:
            dp.append((dp[i-1] + dp[i-2] + dp[i-3])% MAX)
            i += 1
        res = (dp[n-1] + dp[n-2] + dp[n-3]) % MAX #是否是dp[n]
        for i in range(n):
            res += dp[i]*dp[n-i-1] % MAX
            res %= MAX
        return res

'''
没有A
1)end with "P"
dp[i-1]

2)
end with one L 'PL'  dp[i-2]
end with 'PLL' dp[i-3]
end with 'LLL' is not alllowed
so dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

2)end with "L"
dp[i-1] - dp[i-4](3个连续的L, PLLL) (带入公式 dp[i] = 2dp[i-1] - dp[i-4] )

有A ,index为i
分为3部分 0..i-1, A, n-i
dp[i]*dp[n-1-i]


'''

#记忆化DFS
class Solution(object):
    def checkRecord(self, n):
        cache = [[[-1] for _ in range(n+1) for _ in range(2)] for _ in range(3)]
        MAX = 1000000007

        def dfs(u, acnt, lcnt):
            if acnt >= 2:
                return 0
            if lcnt >= 3:
                return 0
            if u == 0:
                return 1
            if cache[u][acnt][lcnt] != -1:
                return cache[u][acnt][lcnt]

            ans = 0
            ans = dfs(u-1, acnt+1, 0)% MAX      #A
            ans += dfs(u-1, acnt, lcnt+1)% MAX  #L
            ans += dfs(u-1, acnt, 0)% MAX       #p
            cache[u][acnt][lcnt] = ans
            return ans

''''
定义了三个 DP 数组 P, L, A，其中 P[i] 表示数组 [0,i] 范围内以P结尾的所有排列方式
结果求 P[n-1] + L[n-1] + A[n-1]
P字符没有限制，可以跟在任何一个字符后面
P[i] = A[i-1] + P[i-1] + L[i-1]
L不能超过2个L, P和L后面可以加L，如果前面是L，要看更前一位(P, A可以加)
L[i] = A[i-1] + P[i-1] + A[i-2] + P[i-2]
A最多有一个
A[i] = A[i-1] + A[i-2] + A[i-3]

'''
A的数量(0 or 1) 以及 字符串末尾连续L的数量(0 or 1 or 2)
排列组合一下就是6种状态
#排列组合 dp[i][j][k] 表示数组前i个数字中，最多有j个A，最多有k个连续L的组合方式,即求dp[n][1][2]


