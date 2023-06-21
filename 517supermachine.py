# -*- coding: utf-8 -*-
"""
Created on Fri May 15 10:51:49 2020

@author: liuga
"""
#让n台洗衣机衣服最少的操作 贪心算法 根据贪心，最大需要减少的num都达到平衡了，其他需要减少的肯定也达到平衡了。
#只能邻里操作
class Solution(object):
    def supermachine(self, machines):
        s = sum(machines)
        l = len(machines)
        if s % l != 0:
            return -1
        
        target = int(s/l)
        res = 0
        balance = 0
        for i in range(l):
            balance += machines[i] - target
            res = max(res, machines[i]-target, abs(balance)) #abs(balance)数组分2部分，一部分的差值和绝对值最大值(一定等于第二部分，这样最终才能平衡 ) machines[i]-target情况是有一个machine值特别大
        return res
    
the max steps is max(max(throughput of every washer), max(give out of every washer)
find the max/peak 'throughput' going from the leftmost washer to the rightmost washer, and the max of the 'GIVE-OUT' washer. 
