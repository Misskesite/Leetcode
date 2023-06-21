# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:20:32 2020

@author: liuga
"""
#1+2+...+mid <= n   1+2+...+ mid + mid + 1 > n 二分法
class Solution(object):
    def arrangeCoin(self,n):
        left, right = 0,n+1
        while left < right:
            mid = left + (right-left)/2
            if mid*(mid+1)/2 <= n:
                left = mid+1
                #res = mid
            else:
                right = mid
        return left -1
    
                
            
        
class Solution:
    def arrangeCoins(self, n):
        total = lambda k: (1+k)*k//2
        i,j  = 0,n
        best = 0
        
        while i<=j:
            m = (i+j)//2
            s = total(m)
            if s<=n:
                best = m
                i    = m + 1 # Check if bigger numbers also work
            else:
                j    = m - 1 # m was too high
        return best
