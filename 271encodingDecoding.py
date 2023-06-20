# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 21:29:01 2020

@author: liuga
"""

class Solution(object):
    def encoding(self, str):
        encode_str = ""
        for s in str:
            encode_str += "%0*x" %(8, len(s)) + s
        return encode_str
    
    def decoding(self, s):
        i = 0
        str = []
        while i < len(s):
            l = int(s[i : i+8], 16)
            str.append(s[i+8:i+16+l])
            i += 8 + l
        return str
