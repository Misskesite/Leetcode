# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:46:23 2019

@author: liuga
"""
#递归
class Solution(object):
    def scrambleString(self, s1, s2):
        N = len(s1)
        if N ==0 :
            return True
        if N==1:
            return s1==s2
        if sorted(s1) != sorted(s2):
            return False
        
        for i in range(1,N):
            if self.scrambleString(s1[:i], s2[:i]) and self.scrambleString(s1[i:], s2[i:]):
                return True
            elif self.scrambleString(s1[:i],s2[-i:]) and self.scrambleString(s1[i:], s2[0:-i]):
                return True
        return False


# DP with memorization
def __init__(self):
    self.dic = {}
    
def isScramble(self, s1, s2):
    if (s1, s2) in self.dic:
        return self.dic[(s1, s2)]
    if len(s1) != len(s2) or sorted(s1) != sorted(s2): # prunning
        self.dic[(s1, s2)] = False
        return False
    if s1 == s2:
        self.dic[(s1, s2)] = True
        return True
    for i in xrange(1, len(s1)):
        if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
        (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
            self.dic[(s1, s2)] = True
            return True
    self.dic[(s1, s2)] = False
    return False


#动态规划 三维数组, 柱体
class Solution(object):
    def scrambleString(self, s, t):
        n1 = len(s)
        n2 = len(s)

        #一些特例
        if n1 != n2:
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False


        dp = [[[False]*(n1+1) for _ in range(n1)] for _ in range(n1)]

        #初始化单个字符
        for i in range(n1):
            for j in range(n2):
                dp[i][j][1] = (s1[i] == s2[j])

        
        for k in range(2, n1+1):
            #枚举S中的起点位置 i
            for i in range(n1 -k +1):
                # 枚举T中的起点位置 j
                for j in range(n2 -k +1):
                    #枚举划分位置
                    for w in range(1, k):
                        #第一种情况: s1->t1 s2->t2
                        if dp[i][j][w] and dp[i+w][j+w][k-w]:
                            dp[i][j][w]= True
                            break

                        #第二种情况: s1->t2, s2-> t1
                        if dp[i][j+k-w][w] and dp[i+w][j][k-w]:
                            dp[i][j][k] = True
                            break

        return dp[0][0][n1]
                        
        
