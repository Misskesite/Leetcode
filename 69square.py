# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:41:48 2019

@author: liuga
"""
#牛顿迭代法?

class Solution(object):
    def Squrt(self, x):
        
        result = 1.0
        while (result * result-x) > 0.1:
            
             result = (result + x/result) /2
             
        return int(result)
    
#二分查找法   时间log(n) 空间log(1) 此解法为主
class Solution2(object):
    def mySqrt(self, x):
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans  #这里可以返回r？ 最后r 等于l-1(ans)
    
    #改写
    def mySqrt(self, x):
        l, r = 0, x+1
        while l < r:
            mid = l + (r -l)//2
            if mid**2 == x:
                retrun mid
            if mid**2 < x:
                l = mid + 1
            else:
                r = mid
        return l - 1
    
#以防万一，用x = 2验证会不会死循环
class Solution2(object):
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x

        l = 0
        r = x -1
        while l < r:
            mid = (l + r + 1)//2 #第二步，当mid**2 > target,才可以排除mid，指针向左移动
            if (mid+1)**2 > x:
                r = mid - 1
            else:
                l = mid
        return l+1
