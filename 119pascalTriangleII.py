# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:09:22 2019

@author: liuga
"""
#滚动数组，空间优化，空间复杂度O(k) 第 i+1行的计算仅用到了第 i行的数据，时间复杂度O(rowIndex**2)
class Solution(object):
    def getRow(self, rowIndex):
        result = [1] + [0]*rowIndex
        
        for i in range(rowIndex):
            result[0] = 1
            for j in range(i+1, 0, -1):  #从右向左遍历
                result[j] = result[j] + result[j-1]
                
        return result
                


#res[i][j] = res[i-1][j-1] + res[i-1][j] 空间复杂度O(k*(k+1)/2)
class Solution(object):
    def getRow(self, rowIndex):
        res = [[1 for j in range(i+1)] for i in range(rowIndex+1)]
        for i in range(2, rowIndex + 1):
            for j in range(1, i):                
                res[i][j] = res[i-1][j-1] + res[i-1][j]

         return res[-1]

#此解法为主
#压缩后的一维 dp数组就是之前二维dp数组的 dp[...][j] 那一行
class Solution(object):
    def getRow(self, rowIndex):
        res = [1]*(rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i-1, 0 , -1):
                res[j] += res[j-1]

        return res
