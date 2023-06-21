# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:28:00 2020

@author: liuga
"""
class Solution:
  def minTransfers(self, transactions: List[List[int]]) -> int:
    balance = [0] * 21

    for u, v, amount in transactions:
      balance[u] -= amount
      balance[v] += amount

    debt = [b for b in balance if b]

    def dfs(s: int) -> int:
      while s < len(debt) and not debt[s]:
        s += 1
      if s == len(debt): #逆向递归推，边界条件n为0，逆向+1
        return 0

      ans = math.inf

      for i in range(s + 1, len(debt)):
        if debt[i] * debt[s] < 0:
          debt[i] += debt[s]  # debt[s] is settled
          ans = min(ans, 1 + dfs(s + 1))
          debt[i] -= debt[s]  # backtrack

      return ans

    return dfs(0)            
                    
            
#backacking+枚举可能的方式
class Solution2(object):
    def miniTransfer(self, transactions):
        person = collections.defaultdict(int)
        for x, y, z in transactions:
            person[x] -= z
            person[y] += z
            
        #accounts = list(person.values())
        accounts = [v for k, v in person.items() if v != 0]
        
        res = float("inf")
        
        def dfs(i, cnt): #i is start index
            nonlocal res

            '''
            if cnt >= res: #这一句可以省略？
                return
            '''
            
            while i < len(accounts) and accounts[i] == 0: #while循环跳过所有的为0的账户
                i += 1
                
            #遍历完
            if i == len(accounts):
                res = min(res, cnt)
                return
            
            for j in range(i+1, len(accounts)):
                if accounts[i]*accounts[j] < 0:
                    accounts[j] += accounts[i] 
                    dfs(i+1, cnt+1)
                    accounts[j] -= accounts[i]
        dfs(0,0)
        return res


      

import collections
 
class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        account = collections.defaultdict(int)
        for transaction in transactions:
            account[transaction[0]] += transaction[2]
            account[transaction[1]] -= transaction[2]
 
        debt = []
        for v in account.values():
            if v:
                debt.append(v)
 
        if not debt:
            return 0
 
        n = 1 << len(debt)
        dp, subset = [float("inf")] * n, []
        for i in xrange(1, n):
            net_debt, number = 0, 0
            for j in xrange(len(debt)):
                if i & 1 << j:
                    net_debt += debt[j]
                    number += 1
            if net_debt == 0:
                dp[i] = number - 1
                for s in subset:
                    if (i & s) == s:
                        dp[i] = min(dp[i], dp[s] + dp[i - s])
                subset.append(i)
        return dp[-1]　　
