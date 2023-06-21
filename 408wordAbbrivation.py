# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:42:45 2020

@author: liuga
"""
#Given s = "internationalization", abbr = "i12iz4n": return True
#此解法为准
class Solution(object):
    def wordAbbrivation(self, word, abbr):
        size = len(word)
        cnt = index = 0
        
        for w in abbr:
            if w.isdigit():
                if w == '0' and cnt == 0: #说明是开头的0
                    return False
                cnt = cnt*10 + int(w)
            else:
                index += cnt
                cnt = 0
                if index >= size or word[index] != w: # index >= size必须放前面，避免越界
                    return False
                index += 1
        return index + cnt == size
        

class Solution2(object):
    def wordAbbrivation(self, word, abbr):
        i= 0
        j = 0
        alen = len(abbr)
        while i < alen:
            if j >= len(word):
                return False
            if not abbr[i].isdigit():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
                
            else:
                if abbr[i] == '0':
                    return False
                n = ""
                while abbr[i].isdigit() and i < alen:
                    n += abbr[i]
                    i += 1
                j += int(n)
        return j == len(word)
                
#改写
    def wordAbbrivation(self, word, abbr):
        wp, ap = 0, 0
        m = len(word)
        n = len(abbr)
        while wp < m and ap < n:
            if abbbr[ap].isdigit():
                steps = 0
                if abbr[ap] == "0":
                    return False
                while ap < n and abbr[ap].isdigit(): #取出数字
                    steps = steps*10 + int(abbr[ap])
                    ap += 1
                wp += steps
            else:
                if word[wp] != abbr[ap]:
                    return False
                wp += 1
                ap += 1
        return wp == m and ap == n
            
