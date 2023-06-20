# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 22:38:05 2020

@author: liuga
"""
#12345    Twelve Thousand Three Hundred Forty Five  123 One Hundred Twenty Three
#1234567  One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven
class Solution(object):
    def intergertoenglish(self, num):
        self.singles = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]
        
        if num == 0:
            return "zero"
        res = ''
        for i in range(len(self.thousands)):
            if num%1000 != 0:
                res = self.helper(num % 1000) + self.thousands[i] + ' ' + res
            num = num // 1000
        return res.strip()
    
    def helper(self, num): #convertHundred?
        if num == 0:
            return ''
        if num < 20:
            return self.singles[num] + ' '
        
        if num < 100:
            return self.tens[num//10] + ' ' +  self.helper(num % 10)
        
        else:
            return self.singles[num//100] + ' Hundred ' + self.helper(num % 100)
        
            
        
        

singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]
#递归
class Solution2:
    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        def recursion(num):
            s = ""
            if num == 0:
                return s
            elif num < 10:
                s += singles[num] + " "
            elif num < 20:
                s += teens[num - 10] + " "
            elif num < 100:
                s += tens[num // 10] + " " + recursion(num % 10)
            else:
                s += singles[num // 100] + " Hundred " + recursion(num % 100)
            return s

        s = ""
        unit = int(1e9)
        for i in range(3, -1, -1):
            curNum = num // unit
            if curNum:
                num -= curNum * unit
                s += recursion(curNum) + thousands[i] + " "
                unit //= 1000
        return s.strip()


#迭代
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def toEnglish(num: int) -> str:
            s = ""
            if num >= 100:
                s += singles[num // 100] + " Hundred "
                num %= 100
            if num >= 20:
                s += tens[num // 10] + " "
                num %= 10
            if 0 < num < 10:
                s += singles[num] + " "
            elif num >= 10:
                s += teens[num - 10] + " "
            return s

        s = ""
        unit = int(1e9)
        for i in range(3, -1, -1):
            curNum = num // unit
            if curNum:
                num -= curNum * unit
                s += toEnglish(curNum) + thousands[i] + " "
            unit //= 1000
        return s.strip()

