# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 22:12:55 2020

@author: liuga
"""
#flatten操作 x映射到矩阵下标 i = x/n y = x%n
class Solution(object):
    def reshapeMatrix(self, nums, r, c):
        m = len(nums)
        n = len(nums[0])
        row = []
        res = []
        
        if m*n != r*c:
            return nums #不成功返回元数组的拷贝
        for i in range(m):
            for j in range(n):
                row.append(nums[i][j])
                if len(row) == c:
                    res.append(row)
                    row = []
        return res
    
     #时间复杂度O(r*c) 空间复杂度O(1) 
    def reshapeMatrix(self, nums, r, c):
        m = len(nums)
        n = len(nums[0])
        if m*n != r*c:
            return nums

        ans = [[0]*c for _ in range(r)]
        for x in range(m*n):
            ans[x // c][x % c] = nums[x //n][x % n]
        return ans

#遍历拉直后的一维数组的坐标
