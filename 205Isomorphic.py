# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:54:34 2020

@author: liuga
"""

class Solution(object):
    def isomophic(self, s, t):
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = t[i]  #s[i]映射到t[i]
            elif hashmap[s[i]] != t[i]:
                return False
        mapval = [hashmap[k] for k in hashmap]
        return len(mapval) == len(set(mapval))
                
            
            
class Solution(object):
    def isIsmomorphic(self, s, t):
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
                else:
                    dic[s[i]] = t[i]

        return True
    
 def isIsomorphic4(self, s, t): 
        return [s.find(i) for i in s] == [t.find(j) for j in t]

    
#follow up 分组
input:
['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']

return:
[
['xyx'], 
['xyz', 'abc', 'def'], 
['aab', 'xxy']
]


def groupIsomorphic(strs):
    def encode(s):
        d = {}
        return str([d.setdefault(c, len(d)) for c in s])
    '''
    def encode(word):
        first_show_dic = {}
        for i, c in enumerate(word):
            if c not in first_show_dic:
                first_show_dic[c] = i
        return tuple([first_show_dic[c] for c in word])
    '''
#You could also record the order of unique characters as the dictionary key, adding each word as a dictionary value to that:

from collections import defaultdict
def isomorphic_groups(words):
res = []
d = defaultdict(list)
for w in words:
order = [str(w.find(i)) for i in w]
o = ",".join(order)
d[o].append(w)

 for k, v in d.items():
     res.append(d[k])
 return res
'''

    def encode(s):
        d = {}
        encoded = []
        for c in s:
            if c not in d:
                d[c] = len(d)
            encoded.append(d[c])
        return str(encoded)

    '''

    groups = collections.defaultdict(list)
    for s in strs:
        groups[encode(s)].append(s)

    return list(groups.values())
