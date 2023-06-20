# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:04:45 2020

@author: liuga
"""
#递归
class Solution(object):
    def lastremaining(self, n):
         return self.leftToright(n)
     
    def leftToright(self,n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n%2 == 1:
            return 2*self.rightToleft((n-1)/2)
        else:
            return 2*self.rightToleft(n/2)
    
    def rightToleft(self,n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n%2 == 1:
            return 2*self.leftToright((n-1)/2)
        else:
            return 2*self.leftToright(n/2)-1

        #新递归
        def lastremaining(self, n):
            return self.dfs(n, True)
        
        def dfs(self, n, flag):
            if n == 1:   #最小问题
                return 1
            if flag:
                return 2*dfs(n/2, 0) #从左到右

            #从右到左
            if n%2 == 1:
                return 2*dfs((n-1)/2, 1)
            else:
                return 2*dfs(n/2, 1) - 1


class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n, isLeft):
            if(n==1): return 1
            if(isLeft):
                return 2*helper(n//2, 0)
    # if started from left side the odd elements will be removed, the only remaining ones will the the even i.e.
    #       [1 2 3 4 5 6 7 8 9]==   [2 4 6 8]==     2*[1 2 3 4]
            elif(n%2==1):
                return 2*helper(n//2, 1)
    # same as left side the odd elements will be removed
            else:
                return 2*helper(n//2, 1) - 1
    # even elements will be removed and the only left ones will be [1 2 3 4 5 6 ]== [1 3 5]== 2*[1 2 3] - 1
            
        return helper(n, 1)
        ```
''''

// 奇数长度
if(n & 1) return 2 * help(n / 2,!L2R);
//  1 2 3 4 5 6 7
//    2   4   6  
// 2*(1   2   3  )  
// 偶数长度的情况
return help(n / 2,!L2R) * 2 - 1;
//   1 2 3 4 5 6 7 8
//   1   3   5   7
// 2*(1   2   3   4) - 1  

'''''
            

class Solution:
    @lru_cache(None)
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        
        return 2 * (n//2 + 1 - self.lastRemaining(n//2))

