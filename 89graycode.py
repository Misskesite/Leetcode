# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:18:17 2019

@author: liuga
"""
#每一位的选择时，会出现01和10的对称情况
#格雷码循环二进制单位距离编码，两个相邻数的代码只有一位二进制数不同的编码
class Solution(object):
    def grayCode(self, n):
        
        result = [i^(i >> 1) for i in range(pow(2, n))]
        return result

#n位元的格雷码可以从n-1位元的格雷码以上下镜射后加上新位元的方式快速的得到
class Solution:
  def grayCode(self, n: int) -> List[int]:
    ans = [0]

    for i in range(n):
      for j in reversed(range(len(ans))):
        ans.append(ans[j] | 1 << i)

    return ans
'''
 关键是搞清楚格雷编码的生成过程, G(i) = i ^ (i/2);
        如 n = 3: 
        G(0) = 000, 
        G(1) = 1 ^ 0 = 001 ^ 000 = 001
        G(2) = 2 ^ 1 = 010 ^ 001 = 011 
        G(3) = 3 ^ 1 = 011 ^ 001 = 010
        G(4) = 4 ^ 2 = 100 ^ 010 = 110
        G(5) = 5 ^ 2 = 101 ^ 010 = 111
        G(6) = 6 ^ 3 = 110 ^ 011 = 101
        G(7) = 7 ^ 3 = 111 ^ 011 = 100
        **/
'''


#从0开始，每次只改变一位二进制位，dfs 直到搜出一组合格的格雷编码
class Solution(object):
    def greyCode(self, n):
        res = []
        hash = [0]*(1 << n)
        dfs(0, 1)

        def dfs(i, k):
            if hash[i]:
                return False
            hash[i] = True
            res.append(i)
            if k == 1 << n:
                return True
            for j in range(n):
                if dfs(i^(1<<j), k+1):
                    return True

            hash[i] = False
            res.pop()
            return False

        return res


#每一位的选择时，会出现01和10的对称情况
class Solution(object):
    def greyCode(self, n):
        res = []
        s = ''
        backtrace(n, s, [0,1])

        def backtrace(n, s, nums):
            if len(s) == n :
                #二进制转化为十进制
                res.append(int('s', 2))
                return
            
            #回溯第一个状态
            s.add(nums[0])
            backtrace(n, s, [0,1])
            s.pop(-1)

            #回溯第二个状态
            s.add(nums[1])
            backtrace(n, s, [1,0])
            s.pop(-1)


#原先的数倒着遍历，并在最高位 添加一个1. 时间复杂度O(2**n)
class Solution:
    def grayCode(self, n):
        res = [0]
        mask = 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] ^ mask)  #或者直接加 1<<i (最高位在之前要么加0，要么加1)
            mask <<= 1
        return res


class Solution:
    def grayCode(self, n: int) -> List[int]:
	r = [0]
	for i in range(n):
	    r.extend([x | 1 << i for x in r[::-1]])
	return r

        
