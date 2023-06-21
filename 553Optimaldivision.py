# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:47:31 2020

@author: liuga
"""

class Solution(object):
    def optimalDivision(self, nums):
        nums = map(str, nums)
        if len(nums) <= 2 :
            return '/'.join(nums)
        return '{}/({})'.format(nums[0],'/'.join(nums[1:]))
        

#贪心算法 最后肯定能化简得到 a/b 的的形式，要使得结果最大化，要么使分子(Numerator)变大，要么使分母(denominator)变小，在这道题中，所有的数都是大于 1 的，所以，把后面所有的数相除做为分母显然是可以使结果最大化的。

class Solution2(object):
    def optimalDivision(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return '{}/{}'.format(nums[0], nums[1])
        return '{}/({})'.format(nums[0], '/'.join(str(num) for num in nums[1:]))


class Solution2(object):
    def optimalDivision(self, nums):
        ans = str(nums[0])

        if len(nums) == 1:
            return ans

        if len(nums) == 2:
            return ans + '/' + str(nums[1])

        ans += '/(' + str(nums[1])
        for i in range(2, len(nums[i])):
            ans += '/' + str(nums[i])

        ans += ')'
        return ans

#x1 / (x2 / x3 / … / xn) x2-xn变成乘数
X1/X2/X3/../Xn will always be equal to (X1/X2) * Y, no matter how you place parentheses. i.e no matter how you place parentheses,
X1 always goes to the numerator and X2 always goes to the denominator. Hence you just need to maximize Y. And Y is maximized when it is equal to X3 *..*Xn. So the answer is always X1/(X2/X3/../Xn) = (X1 *X3 *..*Xn)/X2
