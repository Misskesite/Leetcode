# -*- coding: utf-8 -*-
"""
Created on Sun May 24 12:03:01 2020

@author: liuga
"""

class Solution(object):
    def complexNumber(self,a,b):
        for i in range(len(a)):
            if a[i]== "+":
                real1 = a[:i]
                imag1 = a[i+1:-1]
        
        for i in range(len(b)):
            if b[i]== "+":
                real2 = b[:i]
                imag2 = b[i+1:-1]
        
        real = real1*real2 - imag1*imag2
        imag = real1*imag2 + real2*imag1
        return str(real) + "+" + str(imag) + "i"



class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        for i in range(len(num1)):
            if num1[i]== "+":
                real1 = int(num1[:i])
                imag1 = int(num1[i+1:-1])
        
        for i in range(len(num2)):
            if num2[i]== "+":
                real2 = int(num2[:i])
                imag2 = int(num2[i+1:-1])
        
        real = real1*real2 - imag1*imag2
        imag = real1*imag2 + real2*imag1
        return str(real) + "+" + str(imag) + "i"
