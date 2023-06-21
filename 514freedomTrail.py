# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:07:09 2020

@author: liuga
"""

import collections

class Solution(object):
    def freedomTrail(self, ring,key):
         rlist = collections.defaultdict(list)
         #记录圆环上字符到索引的映射
         for i, r in enumerate(ring):
             rlist[r].append(i)
         n = len(ring)
         dp0 = {0:0} #最初指向12点的方向
         for c in key:
             dp  = {}
             for i in rlist[c]: #多个字符
                 dp[i] = 0x7fffffff
                 for j in dp0: #j是索引？
                     dp[i] = min(dp[i], dp0[j]+ min(abs(i-j), n-abs(i-j))) #abs(i-j)拨动指针的次数，顺时针，逆时针
                 dp0 = dp
         return min(dp.value()+ len(key))

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        pos, n, dp = defaultdict(list), len(ring), [(0,0)]
        for i, c in enumerate(ring):
            pos[c].append(i)
        for c in key:
            dp = [min([(1 + pre_cost + min(abs(i - pre_pos), n - abs(i - pre_pos)), i) for pre_cost, pre_pos in dp]) for i in pos[c]]
        return min(dp)[0]

 class Solution:
  def findRotateSteps(self, ring: str, key: str) -> int:
    # Number of rotates of ring to match key[index:]
    @functools.lru_cache(None)
      def dfs(ring: str, index: int) -> int:
          if index == len(key):
            return 0

          ans = math.inf

      # For each ring[i] == key[index]
      # We rotate the ring to match ring[i] w/ key[index]
      # Then recursively match newRing w/ key[index + 1:]
          for i, r in enumerate(ring):
              if r == key[index]:
                  minRotates = min(i, len(ring) - i)
                  newRing = ring[i:] + ring[:i]
                  remainingRotates = dfs(newRing, index + 1)
                  ans = min(ans, minRotates + remainingRotates)

        return ans

    return dfs(ring, 0) + len(key)

             

from collections import defaultdict as d

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        Choices = d()  # 把每个key对应的可选的ring的字母的index做成字典。
        for k in key:
            if k in Choices:
                continue
            else:
                Choices[k] = []
                for ri, r in enumerate(ring):
                    if r == k:
                        Choices[k].append(ri)

        counter = [{0 : 0}]
        Path = d()

        for i in range(len(key)): # 一共len(key)个格子。
            counter.append({})
            for k in Choices[key[i]]:  # k是表示对于在key上第i个字母来说，ring里有哪几个位置的字母可以选择。
                temp = []
                for j in counter[i].keys():  # j表示上一个格子里，有几种情况可以到达当前的k。
                    prev_distance = counter[i][j]

                    s = str(j) + "-" + str(k)
                    if s not in Path:
                        d1 = abs(k - j)
                        d2 = abs(len(ring) - d1)
                        newc = min(d1, d2)
                        Path[s] = newc

                    temp.append(prev_distance + Path[s])

                counter[i + 1][k] = min(temp) + 1  # 只需要保留最小值  再加1表示按下按钮。

        
        final = min(counter[-1].values())

        return final

'''
对于 key 里的任何一个字母比如 x ，我们去查找 ring 里的所有可能的 x 去匹配。并计算距离，找到最小的距离，进行距离累计。就是到达这个 x 的最小花费。
我们需要查看 key 里的最后一个字母，所对应的几种情况的花费并且找出来最小的那个数就可以了。

ring = "abcabcb" key = "ab"
{0:0} 从0开始距离是0

{0:0  {0:1         
 3:0}  3:4}

{1:0  {1:3
 4:0   4:5
 6:0}  6:3}
