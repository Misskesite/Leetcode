# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:38:17 2020

@author: liuga
"""

class Solution(object):
    def validIP(self, ip):
        def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP and self.checkipV4(queryIP):
            return 'IPv4'
        elif ':' in queryIP and self.checkipV6(queryIP):
            return 'IPv6'
        else:
            return 'Neither'
        
    def checkipV4(self, ip):
        numbers = ip.split('.')
        if len(numbers) != 4:
            return False
        for num in numbers:
            if not num or (not num.isdecimal()) or (num[0] == '0' and len(num) > 1) or int(num)> 255 or len(num) > 3: #字符加‘’
                return False
        return True
    
    def checkipV6(self,ip):
        valid16 = "0123456789ABCDEFabcdef"        
        numbers = ip.split(':')
        if len(numbers) != 8:
            return False
        for num in numbers:
            if not num or len(num)> 4:
                return False

            for n in num:
                if n not in valid16:
                    return False
        return True
    
    
    
import re
class Solution2(object):
    chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')
    
    chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
    patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')

    def validIPAddress(self, IP: str) -> str:        
        if '.' in IP:
            return "IPv4" if self.patten_IPv4.match(IP) else "Neither" 
        if ':' in IP:
            return "IPv6" if self.patten_IPv6.match(IP) else "Neither" 
        return "Neither"

    
