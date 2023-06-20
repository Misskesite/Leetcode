# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:04:04 2019

@author: liuga
"""
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return '0'
        f = 1
        if numerator < 0 and denominator >0  or numerator >0 and denominator <0:
            f = 0

        sg = False
        ans = []
        dic = {}
        ind = 0

        numerator = abs(numerator)
        denominator = abs(denominator)
        
        #开始循环
        while numerator != 0:
            #是否进入小数部分，开始补0
            if sg:
                numerator = numerator*10
                
            #判断被除数是否重复了,没重复记录该数值对应的索引? 重复就进入循环
            if sg and numerator not in dic:
                dic[numerator] = ind
            elif sg and numerator in dic:
                break

            #判断整数或者小数部分
            if not sg and numerator > denominator:
                ans.append(str(numerator//denominator))
                numerator = numerator % denominator
                
            #进入小数部分的处理
            elif not sg and numerator < denominator:
                if ans:
                    ans.append('.')

                else:
                    ans.append('0.')

                sg = True
                
            #小数部分补0
            elif sg and numerator < denominator:
                ans.append('0')

            elif sg and numerator >= denominator:
                ans.append(str(numerator//denominator))
                numerator = numerator % denominator

            ind += 1

        res = '.'.join(ans[:dic[numerator]])+ ‘(’ + ''.join(abs[dic[numerator]:]) + ')' if numerator!= 0 else ''.join(ans)

        return res if f else '_' + res
                
            
                
#divmod是向下取整, 先转为正数再算           
class Solution2(object):
    def fractionTodecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"

        d = dict()
        ans = "-" if numerator*denominator < 0 else ""
        numerator = abs(numerator)
        denominator = abs(denominator)

        div, mod = divmod(numerator, denominator)
        if mod == 0: #余数为0，能整除？
            return ans + str(div)

        ans += str(div) + "."
        d[mod] = len(ans) #记录repeat出现过的余数的位置(ans里面的index)

        while mod:
            mod *= 10 #余数补0
            div, mod = divmod(mod, denominator) #python3 //
            ans += str(div)

            if mod in d:
                index = d[mod]
                ans = ans[:index] + "(" + ans[index:] + ")" #循环部分用括号围起来
                break
            else:
                d[mod] = len(ans)
        return ans
                            
                                                

class Solution:
  def fractionToDecimal(self, numerator: int, denominator: int) -> str:
      if numerator == 0:
          return '0'

      ans = ''

      if (numerator < 0) ^ (denominator < 0):
          ans += '-'

      numerator = abs(numerator)
      denominator = abs(denominator)
      ans += str(numerator // denominator)

      if numerator % denominator == 0:
          return ans

    ans += '.'
    dic = {}

    remainder = numerator % denominator
    while remainder:
      if remainder in dic:
        ans = ans[:dic[remainder]] + '(' + ans[dic[remainder]:] + ')'
        break
      dic[remainder] = len(ans) #不在字典直接赋值
                                                
      remainder *= 10
      ans += str(remainder // denominator)
      remainder %= denominator

    return ans
            
