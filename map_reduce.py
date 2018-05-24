#map/reduce
#我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
#map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，
#Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
#map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，
#还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
t=list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(t)
#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须
#接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#比方说对一个序列求和，就可以用reduce实现：
from functools import reduce
def add(x, y):
    return x + y
print(reduce(add, [1, 3, 5, 7, 9]))
def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7,9]))
#这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，对上面的例子稍加改动，
#配合map()，我们就可以写出把str转换为int的函数：
def fn(x, y):
    return x * 10 + y
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(reduce(fn, map(char2num, '13579')))
#整理成一个str2int的函数就是：
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
print(str2int('1120170710'))
print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))
#还可以用lambda函数进一步简化成：
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
#也就是说，假设Python没有提供int()函数，你完全可以自己写一个把字符串转化为
#整数的函数，而且只需要几行代码！
#lambda函数的用法在后面介绍。
#练习
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
print('输入：[\'adam\', \'LISA\', \'barT\']，输出：[\'Adam\', \'Lisa\', \'Bart\']：')
# -*- coding: utf-8 -*-
print('方法一')
def normalize(name):
    return name[0].upper()+name[1:].lower()
# 测试:
L1=['adam', 'LISA', 'barT']
L2=list(map(normalize, L1))
print(L2)
print('方法二')
def normalize(name):
    def low(name):
	    return name.lower()
    def up(name):
	    return name[0].upper()+name[1:]
    return up(low(name))
# 测试:
L1=['adam', 'LISA', 'barT']
L2=list(map(normalize, L1))
print(L2)
#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，
#可以接受一个list并利用reduce()求积：
# -*- coding: utf-8 -*-
from functools import reduce
def prod(L):
    def multi(x, y):
        return x * y
    return(reduce(multi, L))
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# -*- coding: utf-8 -*-
from functools import reduce
CHAR_TO_FLOAT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.': -1}
def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))