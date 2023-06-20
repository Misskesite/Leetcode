# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:54:36 2020

@author: liuga
"""
#nums = [1,3] n = 6 输出 1(需要加[2])  nums= [1,5,10] n = 20 输出2(需要加[2,4])
#贪心算法 
class Solution(object):
    def patcharray(self, nums, n):
        i, miss, ans = 0,1,0   #miss不能表示的数
        size = len(nums)
        while miss <= n:
            if i < size and nums[i] < miss:
                miss += nums[i] #范围变成[1, miss + nums[i]]
                i += 1
            else:
                miss = miss*2 #补充target,范围变成[1, target*2-1]
                ans += 1
        return ans
            
'''
Combinations of  nums  are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to  nums , the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3]
'''

class Solution:
  def minPatches(self, nums: List[int], n: int) -> int:
      ans = 0
      i = 0     # Point to nums
      miss = 1  # Min sum in [1, n] we might miss

      while miss <= n:
          if i < len(nums) and nums[i] <= miss:
              miss += nums[i]
              i += 1
          else:
              # Greedily add miss itself to increase the range
              # From [1, miss) to [1, 2 * miss)
              miss += miss
              ans += 1

      return ans

'''
给定nums = [1, 2, 4, 11, 30], n = 50，我们需要让[0, 50]之间所有的数字都能被nums中的数字之和表示出来。

首先使用1, 2, 4可能表示出0到7之间的所有数，表示范围为[0, 8)，但我们不能表示8，因为下一个数字11太大了，所以我们要在数组里加上一个8，
此时能表示的范围是[0, 16)，那么我们需要插入16吗，答案是不需要，因为我们数组有1和4，可以组成5，
而下一个数字11，加一起能组成16，所以有了数组中的11，我们此时能表示的范围扩大到[0, 27)，但我们没法表示27，因为30太大了，
所以此时我们给数组中加入一个27，那么现在能表示的范围是[0, 54)，已经满足要求了，我们总共添加了两个数8和27，所以返回2即可。
