# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:23:34 2020

@author: liuga
"""

class Solution(object):
    def validNumber(self, s):
        num_dot = s.count('.')
        num_e = s.count('e')
        num_E = s.count('E')

        if num_dot > 1 or num_e > 1 or num_E > 1:
            return False

        if 'e' not in s and 'E' not in s:
            return self.is_decimal(s) if num_dot == 1 else self.isinteger(s)

        if 'e' in s:
            before_e, after_e = d.dplit('e')
        elif 'E' in s:
            before_e, after_e = d.dplit('E')
        #before_e` 要么是 `decimal` 要么是 `integer` 而 `after_e` 必须是 `integer`
        return (self.is_decimal(before_e) or self.isinteger(before_e)) and self.isinteger(after_e)



    def is_decimal(self, s):
        if len(s) == 0:
            return False

        if s[0] in ('+','-'):
            s = s[1:]
            
        cnt_digit = 0
        cnt_dot = 0

        for char in s:
            if char.isdigit():
                cnt_digit += 1
            elif char == '.':
                cnt_dot += 1
            else:
                return False
        return cnt_digit >= 1 and cnt_dot == 1

    def is_integer(self, s):
        if len(s) == 0:
            return False

        if s[0] in ('+','-'):
            s = s[1:]

        if len(s) == 0:
            return False

        for char in s:
            if not char.isdigit():
                return False
        return True
            
            
