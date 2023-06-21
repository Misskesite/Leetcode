# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:24:21 2020

@author: liuga
"""
#stones = [0,1,3,5,6,8,12,17] return True
class Solution(object):
    def frogjump(self, stones):
         if stones[1] !=1:
             return False
         lastjump = {s :set() for s in stones} #到达的新的点: 跳跃步数
         lastjump[1].add(1)
         for s in stones[:-1]:
             for j in lastjump[s]:
                 for k in (j-1, j, j+1):
                     if k > 0 and s+k in lastjump:
                         lastjump[s+k].add(k) #每一个点(stone)加上之前跳跃的步长
         return bool(lastjump[stones[-1]])

#动态规划dp[i][k]青蛙能否到现在所处的石子编号为i，上一次跳跃距离为k的状态
#时间复杂度O(n*n) 空间复杂度O(n*n)
class Solution2(object):
    def canCross(self, stones):
        n = len(stones)
        dp = [[0]*n for _ in range(n)]
        dp[0][0] = True

        for i in range(1, n):
            if stones[i] - stones[i-1] > i: #优化剪枝 石头 i 最大只能跳 i + 1 步，因此 前面的石头 j 到达 石头 i 的距离必须 <= i
                return False

        for i in range(1, n):
            for j in range(i-1, -1, -1):
                k = stones[i] - stones[j]
                if k > j + 1:
                    break
                dp[i][j] = dp[j][k-1] or dp[j][k] or dp[j][k+1]
                if i == n -1 and dp[i][k]:
                    return True
        return False
                
class Solution:
  def canCross(self, stones: List[int]) -> bool:
    n = len(stones)
    # dp[i][j] := True if a frog can make a size j jump from stones[i]
    dp = [[False] * (n + 1) for _ in range(n)]
    dp[0][1] = True

    for i in range(1, n):
      for j in range(i):
        k = stones[i] - stones[j]
        if k <= n and dp[j][k]:
          dp[i][k - 1] = True
          dp[i][k] = True
          dp[i][k + 1] = True

    return any(dp[-1])                

#记忆化递归
class Solution2(object):
    def frogJump(self, stones):
        s = set()
        def dfs(stones, k, idx):
            key = idx*1000 + k
            if key in s:
                return False
            else:
                s.add(key)

            for i in (idx+1, len(stones)): #枚举选项，展开递归分支
                gap = stones[i] - stones[idx]
                if gap < k - 1:
                    continue
                elif gap > k + 1:
                    break
                else:
                    if dfs(stones, gap, i):
                        return True
            return idx = len(stones)- 1

        return dfs(stones, 0 , 0)
            
