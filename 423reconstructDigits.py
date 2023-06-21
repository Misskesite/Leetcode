# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:47:34 2020

@author: liuga
"""
#s = "owoztneoer" 012   s = "fviefuro" 45
import collections

class Solution(object):
    def reconstruct(self, s):
         numbers = ['zero','one','two','three' 'four', 'five', 'six', 'seven', 'eight', 'nine']
         count = collections.Counter(s)
         
         res = ''
         for i, num in enumerate(numbers):
             while True:
                 word_count = 0
                 for c in num:
                     if count[c] > 0:
                         word_count += 1
                 if word_count == len(num):
                     res += str(i)
                     count.substract(collections.Counter(num))
                 else:
                     break
                 
         return res
                    
                    
#6028745913 类似于拓扑排序的过程。 six, zero, two, eight, four中分别包含唯一字母x, z, w, g, u；因此6, 0, 2, 8, 4需要排在其余数字之前
#s 进行词频统计，然后根据「英文单词中的字符唯一性」确定构建的顺
class Solution(object):
    def originalDigits(self, s):
        def originalDigits(self, s: str) -> str:
        cnts = collections.Counter(s)
        nums = ["zero","two","four","six","eight","one","three","five","seven","nine"]
        numc = [collections.Counter(num) for num in nums]
        digits = [0,2,4,6,8,1,3,5,7,9]
        ans = [0] * 10
        for idx, num in enumerate(nums):
            cntn = numc[idx]
            t = min(cnts[c] // cntn[c] for c in cntn)
            ans[digits[idx]] = t
            for c in cntn:
                cnts[c] -= t * cntn[c]
        return ''.join(str(i) * n for i, n in enumerate(ans))
    

class Solution:
    def originalDigits(self, s: str) -> str:
        c = Counter(s)

        cnt = [0] * 10
        cnt[0] = c["z"]
        cnt[2] = c["w"]
        cnt[4] = c["u"]
        cnt[6] = c["x"]
        cnt[8] = c["g"]

        cnt[3] = c["h"] - cnt[8]
        cnt[5] = c["f"] - cnt[4]
        cnt[7] = c["s"] - cnt[6]
        
        cnt[1] = c["o"] - cnt[0] - cnt[2] - cnt[4]

        cnt[9] = c["i"] - cnt[5] - cnt[6] - cnt[8]

        return "".join(str(x) * cnt[x] for x in range(10))


class Solution:
  def originalDigits(self, s: str) -> str:
    count = [0] * 10

    for c in s:
      if c == 'z':
        count[0] += 1
      if c == 'o':
        count[1] += 1
      if c == 'w':
        count[2] += 1
      if c == 'h':
        count[3] += 1
      if c == 'u':
        count[4] += 1
      if c == 'f':
        count[5] += 1
      if c == 'x':
        count[6] += 1
      if c == 's':
        count[7] += 1
      if c == 'g':
        count[8] += 1
      if c == 'i':
        count[9] += 1

    count[1] -= count[0] + count[2] + count[4]
    count[3] -= count[8]
    count[5] -= count[4]
    count[7] -= count[6]
    count[9] -= count[5] + count[6] + count[8]

    return ''.join(chr(i + ord('0')) for i, c in enumerate(count) for j in range(c))
