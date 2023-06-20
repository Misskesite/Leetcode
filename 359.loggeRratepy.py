# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:57:57 2020

@author: liuga
"""
#使用字典保存每个log上次输出的时间，如果超过10s就输出，并更新时间
class Solution(object):
    def _init_(self):
        self.dic = dict()
        
    def loggerate(self, timestamp, message):
        if message not in self.dic or timestamp-self.dic[message] >= 10:
            self.dic[message] = timestamp
            return True
        else:
            return False
