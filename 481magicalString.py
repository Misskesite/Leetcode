                                                                                                                                               # -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:41:44 2020

@author: liuga
"""
#构造string 前三位122，然后从i=2位置向后遍历, 奇数位置的s[i]：向后面添加s[i]个2。偶数位置的s[i]，向后添加s[i]个1
class Solution(object):
    def magicalString(self,n):
        s = [1,2,2]
        idx = 2
        while len(s) < n:
            s += [3 - s[-1]]*s[idx] #1变成2， 2变成1
            idx += 1
        return s[:n].count(1)
    
    #改写
    def magicalString2(self,n):
        s = [1,2,2]
        idx = 2
        while len(s) < n:
            if idx % 2 == 0:
                ch = 1
            else:
                ch = 2
            if s[idx] == 1:
                s.append(ch)
            else:
                s.extend([ch,ch])
            idx += 1
        res = 0
        for i in range(n):
            if s[i] == 1:
                res += 1
        return res
    

class Solution2(object):
    def magicalString(self, n):
        if n == 0: 
            return 0
        magic, index, cur, res = [1,0,0], 2, 1, 1
        while len(magic)<n: 
            magic.append(cur)
            res += cur
            if magic[index] == 0 and len(magic) < n:
                magic.append(cur)
                res += cur
            cur ^= 1
            index += 1
        return res
    
'''
规律‘1’，‘2’是交替添加，添加了‘1’后添加’2’，添加了’2’后添加’1’，如此循环，而添加的个数与这个字符串本身有关。 代码详细注释 https://blog.csdn.net/qq_41855420/article/details/89022165

str的构造：
index = 0，str = “”，尾部添加一个'1'，str更新为“1”
index = 1，str = “1”，尾部添加str[index] - '0' = 2个 ‘2’，str 更新为 “122”，
index = 2，str = “122”，尾部添加str[index] - '0' = 2个 ‘1’，str 更新为 “122 11”，
index = 3，str = “12211”，尾部添加str[index] - '0' = 1个 ‘2’，str更新为“12211 2”
index = 4，str = “122112”，尾部添加str[index] - '0' = 1个 ‘1’，str更新 “122112 1”，
index = 5，str = “1221121”，尾部添加str[index] - '0' = 2个 ‘2’，str更新为“1221121 22”
index = 6，str = “122112122”，尾部添加str[index] - '0' = 1个‘1’，str 更新 “122112122 1”，
index = 7，str = “1221121221”，尾部添加str[index] - '0' = 2个‘2’，str更新为“1221121221 22”
