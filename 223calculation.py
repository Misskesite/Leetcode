# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 19:52:15 2019

@author: liuga
"""
#左边表达式1，运算符3，右边表达式2 (1和2可以是一个数字，也可以是一个括号包含的表达式)
#栈为了保存左边表达式①的计算结果和运算符③,计算右边表达式2的结果之后，从栈中取出运算符③和①的结果，再进行计算整个表达式的结果。
#(1 + (2 + (3 + 4)))。答案是：栈顶保留的是最里层嵌套的运算. 这种情况时，栈里面保存的是 ["1", "+", "2", "+", "3", "+"]，然后遇到 4，此时计算的是 3 + 4，然后算 7 + 2，再算 9 + 1。可以通过递归来帮助理解
# res表示左边表达式除去栈内保存元素的计算结果
class Solution(object):
    def calculator(self, s):
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():            #num表示当前遇到的数字
                num = 10*num + int(c)
        
            elif c == "+" or c == "-": #更新计算当前计算的结果res, 把数字设为0，sign重新设置
                res = res + sign*num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":             #用栈保存遇到左括号时前面计算好了的结果和运算符
                #如果遇到了(说明遇到了右边的表达式，右边括号里面的需要优先计算，所以要把res, sign进栈，同时更新res, sign
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
                num = 0
            elif c == ")":              #如果遇到),那么说明右边的表达式计算结束，要把之前的结果出栈，计算整个式子的结果
                res = res + num*sign
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res = res + sign*num            #最后一个num更新到res中
        return res


#把括号展开来写 2 - (1 - 3) 展开为 2-1+3
class Solution(object):
    def calculator(self, s):
        sign = [1]
        res = 0
        num = 0
        op = 1
        for ch in s:
            if ch >= '0' and ch <= '9':
                num = num*10 + (ch - '0') #取出完整数值
                continue

            res += op*num #计算一个运算符
            num = 0

            if ch == '+':
                op = sign[0]
            elif ch == '-':
                op = -sign[0]
            elif ch == '(':
                sign.append(op)  #左括号之前的符号置于栈顶
            elif ch == ')':
                sign.pop()       #弹出栈顶符号

        res += op*num            #计算最后一个数

        return res

        

    
class Solution:
    def calculate(self, s: str) -> int:
        presum = 0 
        sign = 1
        st = []

        
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                num = int(s[i])
                while i+1<len(s) and s[i+1].isnumeric():
                    num = num*10 + int(s[i+1])
                    i+=1
                presum = presum + num * sign
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            elif s[i] == "(":
                st.append(presum)
                st.append(sign)
                presum = 0
                sign = 1
            elif s[i] == ")":
                presum = presum * st.pop()
                presum += st.pop()
            i+=1
        return presum

'''
presum 记录之前总和
sign 记录之前的符号
num 记录当前数字

栈 保存括号前的符号 和 sum

这里假设每个符号表达式前边都有“ 0 + ”
s = " 2-1 + 2 "
s = " 0 + 2-1 + 2 "

也是开头的初始化
'''

class Solution:
  def calculate(self, s: str) -> int:
      ans = 0
      num = 0
      sign = 1
      stack = [sign]  # stack[-1]: current env's sign

      for c in s:
          if c.isdigit():
              num = num * 10 + int(c)
          elif c == '(':
              stack.append(sign)
          elif c == ')':
              stack.pop()
          elif c == '+' or c == '-':
              ans += sign * num
              sign = (1 if c == '+' else -1) * stack[-1] #直接展开？
              num = 0

      return ans + sign * num
            
            
