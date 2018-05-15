# -*- coding: utf-8 -*-
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
a=my_abs(-12)
print(a)
#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，
#比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass
age=19
if age >=18:
    pass
#让我们修改一下my_abs的定义，对参数类型做检查，
#只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
