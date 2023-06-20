# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:48:11 2019

@author: liuga
"""

class Solution(object):
    def repeateDNA(self,s):
        seen = set()
        repeated = set()
        n = len(s)
        for i in range(n-9):
            cur = s[i:i+10]
            if cur in seen:
                repeated.add(cur)
            seen.add(cur)
        return list(repeated)

import collections
class Solution(object):
    def findrepeatDNA(self, s):
        ans = []
        cnt = defaultdict(int)
        for i in range(len(s)- L + 1):
            sub = s[i:i+L]
            cnt[sub] += 1
            if cnt[sub] == 2:
                ans.append(sub)

        return ans
