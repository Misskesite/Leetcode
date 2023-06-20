# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 22:43:16 2020

@author: liuga
"""
#先统计data[i] 从第 7 位开始往后有多少位连续的1，代表这是一个几字节的字符，记为cnt

class Solution(object):
    def validutf8(self, data):
        cnt =0
        for d in data:
            if cnt == 0:
                if d >>5 == 0b110:
                    cnt = 1
                elif d >>4 == 0b1110:
                    cnt = 2
                elif d >>3 == 0b11110:
                    cnt = 3
                elif d >>7:
                    return False
            else:
                if d >>6 != 0b10:
                    return False
                cnt -= 1
        return cnt == 0


class Solution {
    public boolean validUtf8(int[] data) {
        int n = data.length;
        //0 <= data[i] <= 255(二进制中为11111111，8bit=1byte)，所以每个data[i]占1个字节
        //满足条件的头字节有：0xxxxxxx 110xxxxx 1110xxxx 11110xxx
        for (int i = 0 ; i < n ; ) {
            int t = data[i];
            //1.校验头字节
            int j = 7, cnt = 0; //cnt为头字节中开头1的数量
            while(j >= 0 && ((t >> j) & 1) == 1 && ++cnt >= 0) j--;
            //开头要么是0个1(即1个0)，要么是2-4个1
            if (cnt == 1 || cnt > 4) return false;
            //2.头字节后面的字节数小于 cnt-1个
            if (i + cnt - 1 >= n) return false;
            //3.判断头字节后的cnt-1个字节前两位开头是否为10
            for (int k = i + 1 ; k < i + cnt ; k++) {
                if (((data[k] >> 7) & 1) == 1 && ((data[k] >> 6) & 1) == 0) continue;
                return false;
            }
            //4.当前的字符满足规则，继续向后判断
            //如果cnt=0，即为题目说的1字节的字符，则当前data[i]为一个有效的unicode
            if (cnt == 0) i++;
            //cnt不为0，向后移动cnt个字符
            else i += cnt;
        }
        return true;
