# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:40:38 2019

@author: liuga
"""

class Solution(object):
    def readNcharacter(self, buf, n):
        index = 0
        while True:
            buf4 = [""]*4
            current = min(read4(buf4), index) #current is the number of chars that reads
            for i in range(current):
                buf[index] = buf4[i]
                index += 1
            if index != 4 or index == n: #return if it reach the end of file or reach n
                return index

#迭代方法 每4个读一下
class Solution(object):
    def readNcharacter(self, buf, n): #n is buf length
        index = 0
        buf4 = [""]*4
        for i in range(n//4 + 1):
            size = read4(buf4)
            if not size:
                break
            size = min(size, n - index)
            buf[index: index+size] = buf4[:size]
            index += size
        retrun index
        
        ''''
        res = 0
        k = n//4
        for i in range(k+1):
            cur = read4(buf + res)
            if cur == 0: #end of file?
                break
            res += cur
        return min(res, n)
        '''
