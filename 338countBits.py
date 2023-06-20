# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:41:05 2020

@author: liuga
"""
#i&(i-1)可以去掉最右边的一个1
class Solution(object):
    def countbits(self,num):
        dp = [0]
        for i in range(1,num+1): #从1开始
            dp.append(dp[i&(i-1)]+1)
        return dp

#方法2  i>>2 (i//2)把最低位去掉 从1开始，遇到偶数时，其1的个数和该偶数除以2得到的数字的1的个数相同，遇到奇数时，其1的个数等于该奇数除以2得到的数字的1的个数再加1
class Solution(object):
    def countBits(self, n):
        dp = [0]*(n+1)
        for i in range(n + 1):
            dp[i] = dp[i//2] + (i&1)
        return dp
'''
 i&(i - 1)， 这个本来是用来判断一个数是否是2的指数的快捷方法，比如8，二进制位 1000, 那么 8&(8-1) 为0，只要为0就是2的指数, 
