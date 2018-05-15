import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx, ny
# 小结
# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。
print('###############################')
#我们就可以同时获得返回值：
# >>> x, y = move(100, 100, 60, math.pi / 6)
# >>> print(x, y)
# 151.96152422706632 70.0
# 但其实这只是一种假象，Python函数返回的仍然是单一值：
# >>> r = move(100, 100, 60, math.pi / 6)
# >>> print(r)
# (151.96152422706632, 70.0)
