# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:09:20 2020

@author: liuga
"""

class Solution(object):
    def guessNumber(self, n, guess):
        left, right = n,1
        while True:
            mid = (left+right)/2
            if guess[mid] == 1:
                left = mid+1
            elif guess[mid] == -1:
                right = mid -1
            else:
                return mid
                
                
                 
                 
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low <= high:
            mid = (low + high)//2
            res =  guess(mid)
            if res == 0 :
                return mid
            elif res == -1:
                high = mid - 1
            else:
                low = mid + 1

        '''
        while low < high:
            mid = (low + high)//2
            res =  guess(mid)
            if res == 0 :
                return mid
            elif res == -1:
                high = mid 
            else:
                low = mid + 1
