# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:31:39 2020

@author: liuga
"""

class hitCount(object):
    def _init_(self):
        self.data = []
        
    def hit(self, timestamp):
        self.data.append(timestamp)
        
    def gethits(self, timestamp):
        while self.data and timestamp - self.data[0] >= 300:
            self.data.pop(0)
        return len(self.data)
    
