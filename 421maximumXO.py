# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:14:51 2020

@author: -
"""
#贪心算法，二进制尽量选择从左边，高位为1 进行异或时应该尽量选择高位异或结果为“1”的。
#a^b = c, 根据异或的特征， a^c = b, 把所有数字的最高位放在hashset里面，用1与里面的所有数字进行异或
#如果得出的结果仍然在set里面，最终结果的最高位必然为1， 否则为0
class Solution(object):
    def maximumXO(self, nums):
        ans = 0
        mask = 0
        for i in range(32, -1, -1) #e.g. 10000, &以后，set里面有2个元素10000，00000
            mask += 1 << i        #mask = mask | 1 << i
            prefixset = set([n & mask for n in nums])
            temp = ans | 1 << i
            
            for prefix in prefixset:
                if temp ^ prefix in prefixset:
                    ans = temp  #prefx(num&mask) ^ temp(b) = c(prefix set) -> prefix ^ c = temp
                    break
        return ans
    
#位异或运算，不进位  [3,10,5,25,2,8] 输出 28   [8, 10, 2] 输出10
class Solution2(object):
    def findMaxXOR(self, nums):
        HIGH_BIT = 30

        x = 0
        for k in range(HIGHBIT, -1, -1):
            seen = set()
            #将所有的pre^k (a_j)放入哈希表中
            for num in nums:
                #如果想保留从最高位到第k个二进制位为止的部分，将其右移k位
                seen.add(num >>k)

            x_next = x*2 + 1 #x的第k个二进制为1
            found = False

            #枚举i
            for num in nums:
                if x_next ^ (num >>k) in seen:
                    found = True
                    break
            if found:
                x = x_next
            else:
                # 如果没有找到满足等式的a_i 和 a_j ，那么x的第k个二进制只能为0 即 x = x*2
                x = x_next - 1

        return x

#try to build the biggest XOR number binary digit by digit.  first question we are going to ask, is there two numbers, such that its XOR starts with 1
class Solution:
    def findMaximumXOR(self, nums):
        ans, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1<<i
            found = set([num & mask for num in nums])
                
            start = ans | 1<<i
            for pref in found:
                if start^pref in found:
                    ans = start
                    break
         
        return ans

# 1 We iterate, starting from the first digit in binary representation of number and go to the right.
# 2 For each traversed digit we update our binary mask: in the beginning it is 10000...000, then it is 11000...000, 11100...000 and in the end 11111...111.
#   We need this mask to quickly extract information about first several digits of our number.
# 3 Create set of all possible starts of numbers, using num & mask: on the first iterations it will be first digit, on the next one first two digits and so on.
# 4 Apply TwoSum problem: if we found two numbers with XOR starting with start, then we are happy: we update our ans and break for inner loop: so we continue to look at the next digit.
