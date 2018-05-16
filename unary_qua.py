# -*- coding: utf-8 -*-
import math
def quadratic(a, b, c):
    delta_squared=b**2-4*a*c
    if delta_squared<0:
	    return None
    else:
        delta=math.sqrt(delta_squared)
        x=(-b+delta)/(2*a)
        y=(-b-delta)/(2*a)
        return x,y
#测试:
#quadratic(2, 3, 1)
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')	