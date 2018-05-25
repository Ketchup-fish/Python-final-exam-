#闭包
#注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，
#其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
#另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，
#它们所引用的变量i已经变成了3，因此最终结果为9。
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
#无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    fs = []
    def f(j):
        def g():
            return j*j
        return g
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
#缺点是代码较长，可利用lambda函数缩短代码。
#练习
#利用闭包返回一个计数器函数，每次调用它返回递增整数：
# -*- coding: utf-8 -*-
def createCounter():
    i=0
    def counter():
        nonlocal i
        i=i+1
        return i
    return counter
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')









