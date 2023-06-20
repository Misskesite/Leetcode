# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 22:54:55 2020

@author: liuga
"""
import math

class Solution(object):
    def bulbSwitch(self, n):
        return int(math.sqrt(n))

'''
// K-th bulb only be switched when k % i == 0.
// So we can reiterate the problem:
// To find # of number <= n that have odd factors.
// Obviously, only square numbers have odd factor(s).
// E.g. n = 10, only 1, 4, and 9 are square numbers that <= 10
