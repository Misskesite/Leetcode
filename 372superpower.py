# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:44:05 2020

@author: liuga
"""
(a*b)%c = (a%c)*(b%c)
# a b=[2,5,4] -> a^250 * a^4 = (a^25)^10 * a^4 = ((a^2)^10 * a^5)^10 * a^4
# if b = [2,5] a^25 = (a^2)^10 * a^5
class Solution(object):
    def superpower(self,a,b):
        res = 1
        for x in b:
            res = self.power(res, 10) * self.power(a, x) % 1337
        return res
    
    def power(self, a, b):
        if b == 0 or a ==1:
            return 1
        if b % 2:
            return a*self.power(a, b-1) % 1337
        return self.power((a*a)%1337, b/2) % 1337


class Solution:
  def superPow(self, a: int, b: List[int]) -> int:
    def powMod(x: int, y: int) -> int:
      pow = 1
      for _ in range(y):
        pow = (pow * x) % k
      return pow

    k = 1337
    ans = 1

    for i in b:
      ans = powMod(ans, 10) * powMod(a, i) % k

    return ans   

#快速幂的方法  二分思路 a**n = a**(n-1)*a (奇数) 偶数 a**(n/2)*a**(n/2)
MOD = 1337
class Solution2:
    def superPow(self, a: int, b: List[int]) -> int:
        def dfs(i):
            if i == -1:
                return 1
            return quickPow(dfs(i - 1), 10) * quickPow(a, b[i]) % MOD
        
        def quickPow(x, y):
            ans = 1
            x %= MOD
            while y:
                if y & 1:
                    ans = ans * x % MOD
                x = x * x % MOD  #偶数？
                y >>= 1
            return ans
        
        a %= MOD
        return dfs(len(b) - 1)

'''
输入：a = 2, b = [1,0]
输出：1024

输入：a = 2147483647, b = [2,0,0]
输出：1198
        
