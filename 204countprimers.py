# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:46:17 2020

@author: liuga
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        not_prime = [False] * n
        count = 0
        for i in xrange(2, n):
            if not not_prime[i]:
                count += 1
                j = 2
                while i*j < n:
                    not_prime[i*j] = True
                    j += 1
                    
        return count
                
#Once the current number is prime then all of it’s product is prime
#and the product must be smaller or equal than n        
class Solution(object):
    def countPrimers(self, n):
        if n < 2 :
            return 0
        prime = [True]*n
        prime[0] = prime[1] = False
        for i in range(2, n):
            if prime[i]:
                for j in range(i+i, n ,i):
                    prime[j] = False

        return prime.count(True)
            
            

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        isPrime = [0] * 2 + [1] * (n - 2)

        for i in range(2, int(n**0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = 0

        return sum(isPrime)
