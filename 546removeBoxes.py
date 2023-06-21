# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:29:28 2020

@author: liuga
"""
#类似于664 移除某个数，剩下的连续的串不是原串的某个连续子串。用 f(l, r, k)表示移除区间 [l, r]的元素 ar加上该区间右边等于a_r的k个元素组成的这个序列的最大积分
#{ 6, 3, 6, 5, 6, 7, 6, 6, 8, 6 } 我们约定 7 和 8已经先被移除，所以在这个状态下我们可以认为最后四个 6是连续的，也就是说实际上待删除的序列是这样的：{[6,3,6,5,6],6,6,6}
#删除后面的四个 6，再删除前面的这个区间，这样获得的分数为 f(0, 3, 0) + 4^2
class Solution(object):
    def removeBoxes(self, boxes):
        self.color = []
        self.length = []
        for box in boxes:
            if self.color and self.color[-1] == box:
                self.length[-1] += 1
            else:
                self.color.append(box)
                self.length.append(1)
        m = len(self.color)
        n = len(boxes)
        self.dp = [[[0]*n for x in range(m)] for y in range(m)]
        return self.solve(0,m-1,m)
    
    def solve(self, l, r, k):
        if l > r:
            return 0
        if self.dp[l][r][k]:
            return self.dp[l][r][k]
        points = self.solve(l,r-1, 0) + (self.length[r]+k)**2
        for i in range(1,r):
            if self.color[i]== self.color[r]:
                points = max(points, self.solve(l,i,self.length[r]+k)+ self.solve(i+1,r-1,0))
        self.dp[l][r][k] = points
        return points

    #改写
    class Solution(object):
        def removeBoxes(self, boxes):
            @lru_cache(None)
            def calculatorPoints(l, r, k):
                if l > r:
                    return 0
                while r > 1 and boxes[r] == boxes[r-1]:
                    r -= 1
                    k += 1
                res = calculatorPoints(l, r-1,0) +(k+1)**2
                for i in range(l, r):
                    if boxes[i] == boxes[r]:
                        res = max(res, calculatorPoints(l, i, k+1) + calculatorPoints(i+1, r-1,0))
        
#DFS(rebot) + memorization        
class Solution2(object):
    def removeBoxes(self, boxes):
        n = len(boxes)
        dp =[[[0]*n for _ in range(n)]for _ in range(n)]
        return self.rebot(boxes, dp, 0, n-1,0)
    
    def rebot(self, boxes, dp, x,y, k):
        if x > y:
            return 0
        if dp[x][y][k] > 0:
            return dp[x][y][k]
        
        while x < y and boxes[y]==boxes[y-1]:
            y -= 1
            k += 1
        
        dp[x][y][k] = self.rebot(self, boxes,x, y-1) + (k+1)*(k+1)
        for i in range(x,y):
            if boxes[i] == boxes[y]:
                dp[x][y][k] = max(dp[x][y][k], self.rebot(boxes, x, i, k+1), self.rebot(boxes, i+1, y-1,0))
        return dp[x][y][k]
    

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]
        for l in range(n-1,-1,-1):
            for r in range(l,n):
                for k in range(n-r):
                    if r > l and boxes[r] == boxes[r-1]:
                        dp[l][r][k] = dp[l][r-1][k+1] #举例：dp[0][6][2] 与 dp[0][5][3] 实际上是等价的
                        continue
                    # 状态初始化：状态 dp[l][r][k] 不代表 boxes[r] 后面真的有 k 个颜色相
                    # 同的盒子，而是假设存在这么一种状态，并且把这种状态的最大值保留下来
                    dp[l][r][k] = dp[l][r-1][0] + (k+1)**2
                    for i in range(l, r):
                        if boxes[i] == boxes[r]:
                            dp[l][r][k] = max(dp[l][r][k], dp[l][i][k+1] + dp[i+1][r-1][0])
        return dp[0][n-1][0]

#区间dp模板, 默认点击boxes[r]消除， 分不同策略，从后面消，或者从前面部分的中间消(中间的分隔点，是跟后面的r相同的点)
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        N = len(boxes)
        dp = [[[0]* (N+1) for _ in range(N+1)] for _ in range(N+1)]
        for l in range(N):   # l++ 从小段 到 大段
            for i in range(N-l): # i++ 起点 从小到大
                j = i + l ;
                for t in range(N-j): # 尾部tail 同数 从小 到 大
                    dp[i][j][t] = max(dp[i][j][t],dp[i][j-1][0] + pow(t+1,2))
                    for k in range(i,j) : # 枚举 分割点 k
                        if boxes[k] == boxes[j]:
                            dp[i][j][t]= max(dp[i][j][t], dp[i][k][t+1] + dp[k+1][j-1][0])
        return dp[0][N - 1][0]
