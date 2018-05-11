#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
    delta = int(b)*int(b)-(4*int(a)*int(c))
    if delta >= 0:
        x1 = (-int(b)+ math.sqrt(delta))/(2*int(a))
        x2 = (-int(b)- math.sqrt(delta))/(2*int(a))
        return x1,x2
    else:
        return('此方程无解')
print('ax2+bx+c=0求根计算')
a = input('请输入a:')
b = input('请输入b:')
c = input('请输入c:')
if not a.isdigit() and b.isdigit()and c.isdigit():
    print('数据类型错误')
else:
    print(quadratic(a,b,c))
