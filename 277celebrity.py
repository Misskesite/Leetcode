# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:02:03 2020

@author: liuga
"""
#设定候选人为0,对于遍历到的人i，若候选人candidate认识i，则将候选人设置为i
#完成一遍遍历后，检测候选人res是否是真正的名人
class Solution(object):
    def findcelebrity(self, n):
        candidate = 0
        # Find the candidate
        for i in range(1, n):
            if knows(candidate,i):
                candidate = i 
        # Verify the candidate
        for i in range(n):
            if i != candidate and (knows(candidate, i)) or not knows(i, candidate):
                return -1
        return candidate


bool know(a, b) #a是否认识b, 如果a认识b那么b可能是名人，如果a不认识b 那么a不是名人
class Solution2(object):
    def findcelebrity(self, n):
        for i in range(n):
            for j in range(n):
                if i != j and (knows(i, j) or !knows(j,i)): #i认识j说明i不是名人(名人不认识其他人)。j不认识i，i肯定不是名人？
                    break

            if j == n:
                return i

        return -1
                
''''
每次调用know排除一个人
