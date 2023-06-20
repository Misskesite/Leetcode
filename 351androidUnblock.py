# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:05:26 2020

@author: liuga
"""

class Solution(object):
    def androidUnblock(m, n):
        if m < 1 or n <1:
            return 0        
        
        visited = [False]*10
        visited[0] = True
        mp = [[0]*10 for _ in range(10)]
        mp[1][3] = mp[3][1] = 2 #两个数字键之间是否有中间键
        mp[1][7] = mp[7][1] = 4
        mp[3][9] = mp[9][3] = 6
        mp[7][9] = mp[9][7] = 8
        mp[2][8] = mp[8][2] = mp[4][6] = mp[6][4] = 5
        mp[1][9] = mp[9][1] = mp[3][7] = mp[7][3] = 5
        
        def dfs(m, n, len, num):
            cnt = 0
            if _len >= m:
                cnt += 1
            _len = _len + 1
            
            if _len > n:
                return cnt
            
            visited[num] = True
            for i in range(1,10):
                if not visited[i] and visited[mp[num][i]]:
                    cnt += dfs(m, n, _len, i)
            visited[num]= False
            return cnt
        return dfs(m,n,1,1)*4 + dfs(m,n,1,2)*4 + dfs(m,n,1,5) # (1 3 7 9对称 *4) (2， 4， 6 ，9 也是对称 *4) 单独的5

#改写  此解法为主
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        seen = set()
        accross = [[0] * 10 for _ in range(10)]

        accross[1][3] = accross[3][1] = 2
        accross[1][7] = accross[7][1] = 4
        accross[3][9] = accross[9][3] = 6
        accross[7][9] = accross[9][7] = 8
        accross[1][9] = accross[9][1] = accross[2][8] = accross[8][2] = \
            accross[3][7] = accross[7][3] = accross[4][6] = accross[6][4] = 5

        def dfs(u: int, depth: int) -> int:
            if depth > n:
                return 0

            seen.add(u)
            ans = 1 if depth >= m else 0

            for v in range(1, 10):
                if v == u or v in seen:
                    continue
                mid = accross[u][v]
                if not mid or mid in seen: # not pass through other dot
                    ans += dfs(v, depth + 1)

            seen.remove(u)
            return ans

        # 1, 3, 7, 9 are symmetric
        # 2, 4, 6, 8 are symmetric
        return dfs(1, 1) * 4 + dfs(2, 1) * 4 + dfs(5, 1)

#上面改写 
class Solution(object):
    def androidUnblock(m, n):
        
        def dfs(m, n, step, num):
            cnt = 0
            if step == 1:
                return 1            
            
            visited[num] = True
            
            for i in range(1,10):
                if not visited[i] and (mp[num][i] == 0 or visited[mp[num][i]]:
                    cnt += dfs(m, n, step-1, i)
                                       
            visited[num]= False
            return cnt


        if m < 1 or n <1:
            return 0        
        
        visited = [False]*10
        visited[0] = True
        mp = [[0]*10 for _ in range(10)]
        mp[1][3] = mp[3][1] = 2 #两个数字键之间是否有中间键
        mp[1][7] = mp[7][1] = 4
        mp[3][9] = mp[9][3] = 6
        mp[7][9] = mp[9][7] = 8
        mp[2][8] = mp[8][2] = mp[4][6] = mp[6][4] = 5
        mp[1][9] = mp[9][1] = mp[3][7] = mp[7][3] = 5

        res = 0
        for i in range(m, n+1):
            res = dfs(m,n,i,1)*4 + dfs(m,n,i,2)*4 + dfs(m,n,i,5)
            
        return  res # (1 3 7 9对称 *4) (2， 4， 6 ，9 也是对称 *4) 单独的5
        
''''        
分类
1 3 7 9
2 8 (2 4 6 8类似，可以去其它任何节点，除了5)
4 6
5(最中间，可以往其它走)
        
backacking
1 保证没有被访问(visited)
2 没有cross num, 或者有cross. 中间的mid有访问过

1 2 3
4 5 6
7 8 9
'''
#求number of unblock patterns
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        seen = set()
        accross = [[0] * 10 for _ in range(10)]

        accross[1][3] = accross[3][1] = 2
        accross[1][7] = accross[7][1] = 4
        accross[3][9] = accross[9][3] = 6
        accross[7][9] = accross[9][7] = 8
        accross[1][9] = accross[9][1] = accross[2][8] = accross[8][2] = accross[3][7] = accross[7][3] = accross[4][6] = accross[6][4] = 5

        def dfs(u: int, depth: int) -> int:
            if depth > n:
                return 0

            seen.add(u)
            ans = 1 if depth >= m else 0

            for v in range(1, 10):
                if v == u or v in seen:
                    continue
                accrossed = accross[u][v]
                if not accrossed or accrossed in seen:
                    ans += dfs(v, depth + 1)

            seen.remove(u) #计算完要回溯，因为后面从其它点出发，会到达这个点
            return ans

        # 1, 3, 7, 9 are symmetric
        # 2, 4, 6, 8 are symmetric
        return dfs(1, 1) * 4 + dfs(2, 1) * 4 + dfs(5, 1)
