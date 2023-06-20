# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:07:25 2020

@author: liuga
"""
#bfs
class Solution(object):
    def removeinvalidParenthesis(self, s):
        if not s:
            return ['']
        q = [s]
        ans = []
        vis = set([s])
        found = False
        while q:
            cur = q.pop(0)
            if self.isvalid(cur):
                found = True
                ans.append(cur)
            
            elif not found:
                for i in range(len(cur)):
                    if cur[i] == '(' or cur[i] == ')':
                        t = cur[:i] + cur[i+1:]
                        if t not in vis:
                            q.append(t)
                            vis.add(t)
        return ans
    
    #改写 保证找到后不继续搜索
        q = deque([s])
        while q:
            cur = q.popleft()
            if isvalid(cur):
                found = True
                ans.append(cur)
            if found:
                continue
            #generate different state
            for i in range(len(cur)):
                    if cur[i] == '(' or cur[i] == ')':
                        t = cur[:i] + cur[i+1:]
                        if t not in vis:
                            q.append(t)
                            vis.add(t)
        return ans
''''
with the input string s, we generate all possible states by removing one ( or ), check if they are valid, if found valid ones on the current level, put them to the final result list and we are done, otherwise, add them to a queue and carry on to the next level.
The good thing of using BFS is that we can guarantee the number of parentheses that need to be removed is minimal,
On the first level, there's only one string which is the input string s, let's say the length of it is n, to check whether it's valid, we need O(n) time. On the second level, we remove one ( or ) from the first level, so there are C(n, n-1) new strings, each of them has n-1 character

if (found) continue;
this ensures once we've found a valid parentheses pattern, we don't do any further bfs using items pending in the queue since any further bfs would only yield strings of smaller length. However the items already in queue need to be processed since there could be other solutions of the same length.
'''
    
    
    #左括号数量小于等于右括号
    def isvalid(self, s):
        cnt = 0
        for c in s:
            if c =='(':
                cnt += 1
            elif c == ')':
                cnt -= 1
                if cnt < 0:
                    return False
                
        return cnt == 0

#DFS 统计多余的左括号，右括号数量,要么都为0，要么一个大于0，一个等于0，要么2个大于0(右括号在前面)
class Solution(object):
    def isvalid(self, s):
        cnt = 0
        for c in s:
            if c =='(':
                cnt += 1
            elif c == ')':
                cnt -= 1
            if cnt < 0:
                return False                
        return cnt == 0
    
    def removeInvalidParentheses(self, s):
        l, r = 0 , 0
        ans = []
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l == 0:
                    r += 1
                else:            
                    l -= 1
                    
        #l, r 表示要移除的括号数
        def dfs(self, s, start, l, r, ans):
            if l == 0  and r == 0：
                if self.isValid(s):
                    ans.append(s)
                    return
            #only remove the first parenthese when there are duplication
            #每次递归从start开始，避免重复计算
            for i in range(start, len(s)):
                if i != start and s[i] == s[i-1]:
                    continue

                if s[i] == '(' ans s[i] == ')':
                    cur = s[i+1:]
                    if r > 0 and s[i] == ')':
                        self.dfs(s[:i] + s[i+1:], i, l, r-1, ans)
                    elif l > 0 and s[i] == '(':
                        self.dfs(s[:i] + s[i+1:], i , l-1, r, ans)

            
        dfs(s, 0, l, r, ans)
        return ans 
        
                
                    
#second method BFS
class Solution2(object):
    def removeinvalidParenthesis2(self,s):
        def isvalid(self, s):
            cnt = 0
            for c in s:
                if c =='(':
                    cnt +=1
                elif c == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0
        
        level = {s}  # 用set避免重复
        while True:
            valid = list(filter(isvalid, level))  
            if valid:
                return valid # 如果当前valid是非空的，说明已经有合法的产生了
            '''
            for ss in level:
                if isvalid(ss):
                    ans.append(ss)
            if len(ans) > 0:
                return ans

            '''
            
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":    # 如果item[i]这个char是个括号就删了，如果不是括号就留着
                        next_level.add(item[:i]+item[i+1:])
            level = next_level

#上一种方法的简写
class Solution3(object):
    def removeinvalidParenthesis(self, s):
        if not s: 
            return ['']
            q = {s}
            while q:
                ans = filter(self.isvalid, q)
                if ans:
                    return ans #每次删除一个括号，剔除不合法的，合法的就是答案了
                q = {cur[:i] + cur[i + 1:] for cur in q for i in range(len(cur))}


#dfs
class Solution3(object):
    def removeInvalidparenthesis(self,s):
        self.ans = []
        self.dfs(s, ')',0)
        return self.ans
    
    def dfs(self, s, ch, last):
        cnt = 0
        for i in range(len(s)):
            if s[i] == '(' or s[i] == ')':
                if s[i] == ch:
                    cnt += 1
                else:
                    cnt -= 1
            if cnt <= 0:
                continue
            for j in range(last, i+1):
                if s[j] == ch and (j == last or s[j-1] != s[j]):
                    self.dfs(s[:j] + s[j+1:], ch, j)
            return
        
        s = list(s)
        s.reverse()
        s = ''.join(s)
        if ch == ')':
            self.dfs(s,'(',0)
            return 
        self.ans.append(s)


                    
            
