# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:22:52 2020

@author: liuga
"""
import collections
#bcabc 输出 abc 单调栈问题
class Solution(object):
    def removeDuplicate(self, s):
        count = collections.Counter(s)
        stack = []
        visited = collections.defaultdict(bool)
        for c in s:
            count[c] -= 1
            if visited[c]:
                continue
            while stack and count[stack[-1]] and stack[-1] > c:
                visited[stack[-1]] = False
                stack.pop()
            visited[c] = True
            stack.append(c)
        return "".join(stack)

#last_index is a mapping from character to its last appearing index
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        index = {c:i for i,c in enumerate(s)}
        stack = []
        visited = set()
        
        for i, c in enumerate(s):
            if c not in stack:
                while stack and stack[-1] > c and index[stack[-1]] > i:
                    visited.remove(stack.pop())
                stack.append(c)
                visited.add(c)
            
        return ''.join(stack)

We traverse sequentially on the string
For each s[i], we check whether it's already in stack or not
if its not in the stack, we need to push it to the stack	
If s[i] is not in the stack (we can check using this in O(1) using a set), and it is smaller than previous elements in stack (lexicographically), and those elements are repeating in future (can check with last_occ),
we need to pop these elements		
		
    

class Solution:
  def removeDuplicateLetters(self, s: str) -> str:
    ans = []
    count = Counter(s)
    used = [False] * 26

    for c in s:
      count[c] -= 1
      if used[ord(c) - ord('a')]:
        continue
      while ans and ans[-1] > c and count[ans[-1]] > 0:
        used[ord(ans[-1]) - ord('a')] = False
        ans.pop()
      ans.append(c)
      used[ord(ans[-1]) - ord('a')] = True

    return ''.join(ans)
        
#如果栈中相邻的元素字典序更大，那么我们选择丢弃相邻的栈中的元素。
class Solution2(object):
    def removeDuplicateLetters(self, s):
        stack = []
        seen = set()
        remain_counter = collections.Counter(s)

        for c in s:
            if c not in seen:
                while stack and c < stack[-1] and remain_counter[stack[-1]] > 0:
                    seen.discard(stack.pop())
                seen.add(c)
                    
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)

