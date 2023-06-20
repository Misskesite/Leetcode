# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:57:22 2020

@author: liuga
"""
import heapq

class Solution(object):
    def superUglynumber(self, n, primes):
        if not primes:
            return 
        uglies = [1]
        def gen(prime):
            for ugly in uglies:
                yield ugly*prime
        
        merged = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            ugly = next(merged)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]
            
        
#暴力Heap容易TLE
'''
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        seen = {1}

        for i in range(1, n+1):
            curr = heapq.heappop(heap)

            if i == n:
                return curr
            # 生成每一层的丑数
            for item in primes:
                next_item = curr * item

                # 重复的数跳过
                if next_item not in seen:
                    heapq.heappush(heap, next_item)
                    seen.add(next_item)

'''

import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp, heap, visited = [1], [], set()
        for i, p in enumerate(primes):
            heapq.heappush(heap, (p, i, 0))
        
        while len(dp) < n:
            val, prime_idx, dp_idx = heapq.heappop(heap)
            if val not in visited:
                dp.append(val)
                visited.add(val)
            heapq.heappush(heap, (primes[prime_idx] * dp[dp_idx + 1], prime_idx, dp_idx + 1))
        
        return dp[-1]
