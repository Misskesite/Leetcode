# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 18:09:44 2019

@author: liuga
"""
#二进制中数字为1的个数(汉明距离)
class Solution(object):
    def hammingWeight(self, n):
        res = 0
        while n:
            res += 1
            n = n & (n-1) #把整数最右边的1变成0
        return res


class Solution:
  def hammingWeight(self, n: int) -> int:
    ans = 0

    for i in range(32):
      if (n >> i) & 1:
        ans += 1

    return ans



class Solution(object):
    def hammingWeight(self, n):
        cnt = 0
        flag = 1
        while flag:
            if n & flag:       #判断最低位是不是1
                cnt += 1
            flag = flag << 1 #把1左移得到2，再和n做运算，就能判断次低位是不是1
        return cnt

grep -oE '[a-z]+' words.txt | sort | uniq -c | sort -nr| awk '{print $2,$1}'

grep -p '^(\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$' file.txt

