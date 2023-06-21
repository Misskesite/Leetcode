# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 20:38:13 2020

@author: liuga
"""

class Solution(object):
    def curcularArray(self,nums):
        n = len(nums)
        self.nums = nums
        for i in range(n):
            #if nums[i] == 0: continue
            slow = i
            fast = self.nextpos(i)
            while nums[fast]*nums[i] > 0 and nums[self.nextpos(fast)]*nums[i] > 0: #相同符号,方向相同
                if fast == slow:
                    if slow == self.nextpos(slow): #自成环 比如[1]
                        break
                    return True
                slow = self.nextpos(slow)
                fast = self.nextpos(self.nextpos(fast)) #走两步
        return False
            
            
            
    def nextpos(self,i):
        n = len(self.nums)
        return (i + self.nums[i] + n)% n

'''
Time: O(n), Space O(n)
Note: The starting index can be any index, NOT zero only
Take each unvisited index and start traverse, mark as visited at the meantime
If sign changes or cycle at itself, break the loop; otherwise, if revisited an index, return True
'''
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n, visited = len(nums), set()
        for i in range(n):
            if i not in visited:
                local_s = set()
                while True:
                    if i in local_s: #i位置为起点，经过的位置都存到了 HashMap 中?
                        return True
                    if i in visited:
                        break          
                    visited.add(i)
                    local_s.add(i)
                    prev, i = i, (i + nums[i]) % n
                    if prev == i or (nums[i] > 0) != (nums[prev] > 0):
                        break #自成环[1]，有值为0跳回自己. 或者 方向不相同？
        return False

'''
A cycle must start and end at the same index and the cycle’s length > 1.
Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not consist of both forward and backward movements.
