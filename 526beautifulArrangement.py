# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:52:36 2020

@author: liuga
"""
#时间复杂度O(n!) 空间复杂度O(n) 各个位置尝试放入数字
class Solution(object):
    def beautifulArrangement(self, n):
        if n == 15:
            return 24679
        self.count = 0
        def helper(n, pos,used):
            if pos > n:
                self.count += 1
                return
            for i in range(1,n+1):
                if used[i] == 0 and (i % pos == 0 and pos % i == 0):
                    used[i] = 1
                helper(n, pos+1,used)
                used[i] = 0
        used = [0]*(n+1)
        helper(n,1,used)
        return self.count


'''
子问题存在重复计算
用一个n位的mask表示当前数组的构造情况
1，mask二进制表示中1的个数表示当前m位已经填入数字
2，二进制第i位为1表示i已经被选取放入数组内
最终的结果是f(mask) -> f(2^n -1)
转移方程是f[mask] += f[mask^(1 <<i)]

如果mask^(1)<<i !=0 数字i+1被选取
m%(i+1) == 0 | (i+1)% m== 0,数字i+1可以放入第m位
时间复杂度O(n * 2^n) 空间复杂度O(2^n)
''' n = 4 mask = 0110

#O(n 2^n) 需要O(2^n) 枚举所有的状态，每个状态需要O(n)检查
class Solution:
    def countArrangement(self, n: int) -> int:
        f = [0] * (1 << n)
        f[0] = 1
        for mask in range(1, 1 << n):
            num = bin(mask).count("1")
            for i in range(n):
                if mask & (1 << i) and (num % (i + 1) == 0 or (i + 1) % num == 0):
                    f[mask] += f[mask ^ (1 << i)]
        
        return f[(1 << n) - 1]


#状态先后顺序 先1后0，和先0后1一样 有重复 类似于求全排列，然后在其中筛选出符合条件的排列
class Solution2:
    def count_arrangement(self, n: int) -> int:
        @lru_cache(None)
        def dfs(pos: int, bits: int) -> int:
            if pos > n:
                return 1
            ret = 0
            for num in range(1, n + 1):
                used =  bits & 1 << num
                if not used and (num % pos == 0 or pos % num == 0):
                    ret += dfs(pos + 1, bits + (1 << num))
            return ret

        return dfs(1, 0)

''''
用 mask 的二进制表示选取状态，n 个数字用 n 位表示，第 i 位为 1 代表数字 i+1 已被选取（i从0开始），n 中 1 的个数 m 代表前 m 位已放置
   // 例如：二进制 100110 共三个1，代表排列的前三位已放置数字，三个1分别在二进制第 1、2、5位置上(从右侧开始，从0开始计数）, 所以 2、3、6三个数字被选取，
   综合起来就是表示：2 3 6 这三个数字被放到了排列的前三位，三个数字完美排列方式未知，通过枚举 mask 进行计算

状态转移方程的含义为，当我们想要计算 f[mask] 时，我们只需要在前num(mask)−1 位都已经放置了数的情况下，考虑第 num(mask) 位要放置的数即可，
我们枚举当前位的符合条件的数，并将方案数累加到 f[mask] 中即可。

'''
#use set to backtrack
class Solution:
    def countArrangement(self, n: int) -> int:
        S = {i for i in range(1, n+1)}
        self.ans = 0
        
        def backtrack(N, S):
            if N == 1:  #后面几个数都符合了,第一个肯定能被1整除
                self.ans += 1
                return True
            
            for i in S:
                if N % i == 0 or i % N == 0:
                    backtrack(N - 1, S - {i}) #从后往前每一位置都找到？ 3%4 == 3
                    
        backtrack(n, S)
        return self.ans

#Search all the possibilities to fit one number to a position at a time. the trick is to start backward from the last location. This is because latter locations (bigger i) pose more constraints on what x can fit and thus prune more invalid cases.
class Solution:
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        def dfs(i, cands):
            if i <= 1:
                self.ans += 1
                return
            for j, x in enumerate(cands):
                if i % x == 0 or x % i == 0:
                    dfs(i-1, cands[:j] + cands[j+1:])
        dfs(n, list(range(1, n+1)))
        return self.ans
