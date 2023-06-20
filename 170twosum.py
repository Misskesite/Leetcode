# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 13:37:19 2019

@author: liuga
"""
#此法为主
class Twosums(object):
    def _init_(self):
        self.dic = defaultdict(int)
    
    def add(self,number):
        self.dic[num] += 1        
            
    def find(self, value):
        
        for key in self.dic:
            if value-key in self.dic and ((value-key) != key or self.dic[key]>1):
                return True
        return False

class TwoSum:
  def __init__(self):
    self.count = Counter()

  def add(self, number: int) -> None:
    self.count[number] += 1

  def find(self, value: int) -> bool:
    for key, freq in self.count.items():
      remain = value - key
      if key == remain and freq > 1:
        return True
      if key != remain and remain in self.count:
        return True

    return False
