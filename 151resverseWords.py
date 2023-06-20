# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#时间复杂度O(n) 空间复杂度O(n)
class Solution(object):
    def ReverseWord(self, s):
        return " ".join(s.split()[::-1])   #或者" ".join(reversed(s.split()))
    
    if __name__ == "__main__":
    print(Solution().ReverseWord("the sky")) 
