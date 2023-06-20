# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:04:04 2019

@author: liuga
"""
#此解法为主
class Solution(object):
    def compareversion(self,version1,version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        l1 = len(v1)
        l2 = len(v2)
        for i in range(max(l1,l2)):
            temp1 = 0  #如果一个版本长于另一个，短的部分均为0
            temp2 = 0
            if i < l1:
                temp1 = int(v1[i]) #版本的每一段转化为int比较
            if i < l2:
                temp2 = int(v2[i])
                
            if temp1 <  temp2:
                return -1
            elif temp1 > temp2:
                return 1
        return 0


#双指针法 时间复杂度O(m+n), 空间复杂度O(1)
class Solution(object):
    def compareVersion(self, version1, version2):
        m = len(version1)
        n = len(version2)

        i = j  = 0
        while i < m or j < n:
            a = b = 0
            while i < m and version[i] != '.':
                a = 10*a + int(version[i])
                i += 1
            
            while j < n and version2[i] != '.':
                b = 10*b + int(version1[j])
                j += 1

            if a > b:
                return 1
            elif a < b:
                return -1
            
            i += 1  #跳过点号?
            j += 1
        return 0
                
            
