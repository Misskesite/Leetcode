# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:51:09 2020

@author: liuga
"""
#n = 1 [0 1 8] n = 2 [11 88 69 96]
class Solution(object):
    
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        self.res = 0
        same = (", "0","1","8")
        two = (('0','0') ('1','1') ('6','9') ('8','8') ('9','6'))
        for length in range(len(low),len(high)+1):
            self.dfsHelper(low,high, length, "")
            self.dfsHelper(low,high, length, "1")
            self.dfsHelper(low,high, length, "8")
            self.dfsHelper(low,high, length, "0")
        return self.res
            
        
        
    def dfsHelper(self,low,high,length,path):
        if len(path) > length:
            return
        if len(path) == length:
            if len(path) != 1 and path[0] == '0':
                return
            else:
                if int(path) >= int(low) and int(path) <= int(high):
                    self.res +=1
                return
        self.dfsHelper(low,high, length, '0'+path+'0')
        self.dfsHelper(low,high, length, '6'+path+'9')
        self.dfsHelper(low,high, length, '9'+path+'6')
        self.dfsHelper(low,high, length, '8'+path+'8')
        self.dfsHelper(low,high, length, '1'+path+'1')
            
  
''''
n = 0:   none
n = 1:   0, 1, 8
n = 2:   11, 69, 88, 96
n = 3:   101, 609, 808, 906, 111, 619, 818, 916, 181, 689, 888, 986
n = 4:   1001, 6009, 8008, 9006, 1111, 6119, 8118, 9116, 1691, 6699, 8698, 9696, 1881, 6889, 8888, 9886, 1961, 6969, 8968, 9966

''''

#对称中心可以是奇数位，可以是偶数位
class Solution2(object):
    def Strobogrammatic(self, low, high):
        stro_dict = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        res = 0
        res += self.dfs('', low, high, stro_dict)
        res += self.dfs('0', low, high, stro_dict)
        res += self.dfs('1', low, high, stro_dict)
        res += self.dfs('8', low, high, stro_dict)
        return res

    #看单词长度是否达到，达到后去掉开头为0的多位数，去掉长度等于low小于low，等于high大于high，结果更新，再加上五个对称数，递归调用
    def dfs(self, s, low, high, stro_dict):
        if len(s) > len(high) or (len(s) == len(high) and s > high):
            return 0

        res = 0
        if len(s)> len(low) or (len(s) == len(low) and s >= low):
            res = 1

        if len(s) > 1 and s[0] == '0': #i.e. 08
            res = 0

        for key, value in stro_dict.items():
            res += self.dfs(key + s + value, low, high, stro_dict)

        return res
        
#改写
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        stro_dict = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        same = ("","0","1","8")
        res = 0
        for val in same:
            res += self.dfs(val, low, high, stro_dict)
        return res

    #看单词长度是否达到，达到后去掉开头为0的多位数，去掉长度等于low小于low，等于high大于high，结果更新，再加上五个对称数，递归调用
    def dfs(self, s, low, high, stro_dict):
        if len(s) > len(high) or (len(s) == len(high) and s > high):
            return 0
        
        res = 0
        if len(s)> len(low) or (len(s) == len(low) and s >= low):
            res = 1

        if len(s) > 1 and s[0] == '0': #i.e. 08
            res = 0

        for key, value in stro_dict.items():
            res += self.dfs(key + s + value, low, high, stro_dict)

        return res
