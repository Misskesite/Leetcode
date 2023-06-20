# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 21:59:53 2020

@author: liuga
"""

class Solution(object):
    def panlindrom(self, words):
         wmap = { w:i for i,w in enumerate(words)}
         
         def ispanlindrom(word):
             return word == word[::-1]
         
         res = set()
         for idx, word in words:
             #word本身为回文，且words中存在空串
             if word and ispanlindrom(word) and "" in wmap:
                 nidx = wmap[""]
                 res.add((idx, nidx))
                 res.add((nidx, idx))
            
             rword = word[::-1]
             #当前单词的逆序在words.坐标不能相同，因为反转后可能是本身
             if word and rword in wmap:
                 nidx = wmap[rword]
                 if idx != nidx:
                     res.add((idx, nidx))
                     res.add((nidx, idx))
                    
             #当前单词左右两半，left为回文，right逆序在words里，或者right为回文，left逆序在words里   
             for x in range(1, len(word)):
                 left, right = word[:x], word[x:]
                 rleft, rright= left[::-1], right[::-1]
                 if ispanlindrom(left) and rright in wmap:
                     res.add((wmap[rright],idx))
                 if ispanlindrom(right) and rleft in wmap:
                     res.add((idx,wmap[rleft]))
                     
             return list(res)

class Solution2(object):
    def palindromePairs(self, words):
        ans = []
        dic = {word[::-1]: i for i, word in enumerate(words)}

        for i, word in enumerate(words):
            if "" in dic and dic[""] != i and word == word[::-1]:#本身为回文？ 
                ans.append([i, dic[""]])

            for j in range(1, len(word)+1):
                l = word[:j]
                r = word[j:]

                if l in dic and dic[l] != i and r == r[::-1]: #right为回文，left逆序在字典里  ["abcd", "dcba"] 这里right为空   不等于i,防止本身是回文(aba)?
                    ans.append([i, dic[l]])
                if r in dic and dic[r] != i and l == l[::-1]: #l为回文，right逆序在字典里  "lls", "ss sll"   "ll s", "s",
                    ans.append([dic[r], i])

        return ans 
         
class Solution2(object):
    def palindromePairs(self, words):
        def is_palindrome(check):
        return check == check[::-1]

        dic = {word: i for i, word in enumerate(words)}
        ans = []
        for word, k in dic.iteritems():
            n = len(word)
            for j in range(n+1):
                l = word[:j]
                r = word[j:]
                if is_palindrome(l): #eg "lls", "s" j也可以取n，这样?    左边为空，右边的对称在字典里面 ["abcd", "dcba"]
                    back = r[::-1]
                    if back != word and back in words:
                        ans.append([words[back],  k])
                if j != n and is_palindrome(r): #右边不为空？避免跟上面重复，+ "lls", "ss sll"
                    back = l[::-1]
                    if back != word and back in words:
                        ans.append([k, words[back]])
        return valid_pals
