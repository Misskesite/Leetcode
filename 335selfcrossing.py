# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:50:11 2020

@author: liuga
"""

class Solution(object):
    def selfcrossing(self, x):
        if len(x) < 4:  return False
        
        for i in range(2, len(x)):      # 一直外卷 必须满足while i< n and x[i] > x[i-2]
            if x[i] <= x[i-2]:
                break #不满足，跳出
        #向外卷变成向内卷， i-1的长度 减去i-3的长度
        if i >= 4 and x[i] + x[i-4] >= x[i-2] or i == 3 and x[i] == x[i-2]:
            x[i-1] -= x[i-3]
            
        for j in range(i+1, len(x)):    # 内卷
            if x[j] >= x[j-2]:
                return True
        return False


#换种写法 3种相交情况
    for i in range(3, len(x)): #第i条和i-3相交
        if i >= 3 and x[i-1] <= x[i-3] and x[i] >= x[i-2]:
            return True

        elif i >= 4 and x[i-3] == x[i-1] and x[i] + x[i-4] >= x[i-2]:
            return True        #第i条和i-4相交

        elif i >= 5 && x[i] + x[i-4] >= x[i-2]  && x[i-1] + x[i-5] >= x[i-3] && x[i-2] > x[i-4] && x[i-3] > x[i-1])：
            return True        #第i和i-5相交

    return False

class Solution2(object):
    def isSelfcrossing(self,x):
        l = len(x)
        m = 0               #表示状态
        bound = [0,0,0,0,0] #上左下右界+temp
        loc = (0,0)         #当前位置
        vecx = (0,-1,0,1)
        vecy = (1,0,-1,0)
        j = 0

        for i in range(l):
            j = i % 4
            k = (i+1) %2
            loc = (loc[0] + vecx[j] * x[i],loc[1] + vecy[j] * x[i])
            if m == 0:
                if (loc[k]-bound[j])*(vecx[j] + vecy[j]) <= 0:
                    if (loc[k]-bound[-1])*(vecx[j] + vecy[j]) >= 0:
                        bound[(j+1)%4] = bound[-1]
                    m = 1
                bound[-1] = bound[j]
            elif (loc[k]-bound[j])*(vecx[j]+vecy[j]) >= 0:
                return True
            bound[j] = loc[k]

                
        return False



class Solution {
    public boolean isSelfCrossing(int[] d) {
        int n = d.length;
        if (n < 4):
            return false
        for (int i = 3; i < n; i++) {
            if (d[i] >= d[i - 2] && d[i - 1] <= d[i - 3]) return true;
            if (i >= 4 && d[i - 1] == d[i - 3] && d[i] + d[i - 4] >= d[i - 2]) return true;
            if (i >= 5 && d[i - 1] <= d[i - 3] && d[i - 2] > d[i - 4] && d[i] + d[i - 4] >= d[i - 2] && d[i - 1] + d[i - 5] >= d[i - 3]) return true;
        }
        return false;
    }
}

