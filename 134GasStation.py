# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:26:06 2019

@author: liuga
"""
#找从0出发总（gas-cost）的最低点，那么解就是最低点的下一个点，因为总（gas-cost）是大于等于0的，所以前面损失的gas我从最低点下一个点开始都会拿回来
class Solution(object):
    def gasStation(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        min_sum, index, total = 0,0,0
        
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            
            if total < min_sum:
                min_sum  = total
                min_index = i+1 #最低点的下一个点，保证从下一个节点起步，每一步剩余的(gas - cost) > 0

        if total < 0:
            return -1
        else:
            return min_index



class Solution:
  def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
      ans = 0
      net = 0
      summ = 0

      for i in range(len(gas)):
          net += gas[i] - cost[i]
          summ += gas[i] - cost[i]
          if summ < 0:
              summ = 0
              ans = i + 1

      return -1 if net < 0 else ans
