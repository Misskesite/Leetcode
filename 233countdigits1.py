# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 23:25:47 2020

@author: liuga
"""
class Solution(object):
    def countDigitOne(self, n):
        ones, m = 0, 1
        while m <= n:
            ones += (n/m + 8) / 10 * m + (n/m % 10 == 1) * (n % m + 1)
            m *= 10
        return ones


#动态规划
class Solution2(object):
    def countDigitOne(n):
        def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n < 10:
            return 1 
        dp_dic = {1:1}

        def dfs(j):
            if j not in dp_dic: 
                dp_dic[j] = dfs(j-1)*10 + 10**(j-1)
            return dp_dic[j]

        def res_count(n):
            while n[:1] == '0':
                n = n[1:]
            if not n: 
                return 0
            length = len(n)
            if length == 1: 
                return 1
            if n[:1] == '1':
                return dfs(length-1) + int(n[1:]) + 1 + res_count(n[1:])
            else:
                return 10**(length-1) + dfs(length-1)*int(n[:1]) + res_count(n[1:])
        return res_count(str(n))
    

#找规律 n = 2021,个位数出现1的概率是每10个数出现一次，202+1
#每100个数出现10个十位数为1的数字，如果最后2位小于10，则不用额外加次数
#count = (n / (i * 10) * i) + w, w要看i及右边的位数。即 x= n%(i*10) 和i的比较
# x<i, w = 0. [i,2i）w = x-i+1. [2i ) w = i. 总的 w = min(max(x - i + 1, 0), i)
class Solution3(object):
    def countDigitOne(n):
        ans = 0
        for i in range(1, n+1):
            ans += (n / (i * 10)* i + min(max(n % (i * 10) - i + 1, 0), i)
        return ans

    public: # 13 = 2 + 1*3
    int countDigitOne(int n) {
        int res = 0, a = 1, b = 1;
        while (n > 0) {
            res += (n + 8) / 10 * a + (n % 10 == 1) * b; #(n + 8) / 10 判断是否>=2
            b += n % 10 * a;
            a *= 10;
            n /= 10;
        }
        return res;
    }
                    
#十位数上的数字(加1)就代表1出现的个数，这时候再把多出的 10 个加上即可。比如 56 就有 (5+1)+10=16 个。如何知道是否要加上多出的 10 个呢，就要看十位上的数字是否大于等于2，是的话就要加上多余的 10 个 ‘1
#对于三位数区间 [100, 199] 内的数也是一样，除了 [110, 119] 之间多出的10个数之外，共 21 个 ‘1’，其余的每 10 个数的区间都只有 11 个 ‘1’，所以 [100, 199] 内共有 21 + 11 * 9 = 120 个 ‘1’
'''
范围        个    十    百    千     万     1总和
1-9         1                              1      
10-99       9    90                        20     10 + 10*1  = 20
100-999     90   90    100                 300    100 + 10*20 = 300
1000-9999   900  900   900  1000           4000   1000 + 10*300 = 4000
10000-99999 9000 9000  9000 9000  10000    50000  10000 + 10*4000 = 50000
f(i) = 10**(i-1) + 10*f(i-1)
f(i) = i*10**(i-1)
'''
class Solution(object):
    def countOne(self, n):
        if n < 10:
            return 1 if n else 0
        num = str(n)
        x = len(num) - 1
        nxt = int(num[1:])
        if nums[0] == '1':
            res = self.f(x-1) + nxt + 1 + self.countOne(nxt)
        else:
            res = self.f(x)*int(nums[0]) + self.countOne(nxt)

    @lru_cache(None)
    def f(self, i):
        # return i * 10 ** (i-1)
        return 10 ** (i-1) + 10 * self.f(i-1) if i else 0

                
                    

    class Solution {
    public int countDigitOne(int n) {
        int res = 0;
        for (long i = 1; i <= n; i *= 10) {
            int prefix = (int)(n/(i*10));
            int digit = (int)((n/i)%10); 
            int suffix = (int)(n%i);
            if (digit == 0) {
                res += prefix*i;
            } else if (digit == 1) {
                res += prefix*i + suffix + 1;
            } else {
                res += (prefix + 1)*i;
            }
        }
        return res;   
