# -*- coding: utf-8 -*-
"""
Created on Wed May 27 20:59:33 2020

@author: liuga
"""

class Solution(object):
    def studentAttendent(self, s):
        return s.count('A') <2 and 'LLL' not in s
    
    
import re
class Solution2(object):
    def studentAttendent(self, s):
        return not re.match(".*A.*A.*", s) and not re.match(".*LLL.*", s)
    
    
