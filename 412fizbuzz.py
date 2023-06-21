# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 22:43:50 2020

@author: liuga
"""
#此法为主
class Solution(object):
    def fizzbuzz(self, n):
        res = []
        for i in range(1, n+1):
            if i % 3 == 0 or i % 5 == 0:
                res.append("Fizz"*(i % 3 == 0) + "Buzz"*(i % 5 == 0))
            else:
                res.append(str(i))
        return res


class Solution:
  def fizzBuzz(self, n: int) -> List[str]:
    d = {3: 'Fizz', 5: 'Buzz'}
    return [''.join([d[k] for k in d if i % k == 0]) or str(i) for i in range(1, n + 1)]
