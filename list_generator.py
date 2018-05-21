#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式.
#举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
t=list(range(1, 11))
print(t)
#但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
#但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list:
t1=[x * x for x in range(1, 11)]
print(t1)
#写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，
#就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
t2=[x * x for x in range(1, 11) if x % 2 == 0]
print(t2)
#还可以使用两层循环，可以生成全排列：
t3=[m + n for m in 'ABC' for n in 'XYZ']
print(t3)
#三层和三层以上的循环就很少用到了。
#运用列表生成式，可以写出非常简洁的代码。
#例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os # 导入os模块，模块的概念后面讲到
t4=[d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print(t4)
#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)
#因此，列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
t5=[k + '=' + v for k, v in d.items()]
print(t5)
#最后把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
t6=[s.lower() for s in L]
print(t6)
#练习
#如果list中既包含字符串，又包含整数，
#由于非字符串类型没有lower()方法，所以列表生成式会报错：
#使用内建的isinstance函数可以判断一个变量是不是字符串：
x = 'abc'
y = 123
t6=isinstance(x, str)
print(t6)
t7=isinstance(y, str)
print(t7)
#请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() for s in L1 if isinstance(s, str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')