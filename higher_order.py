#高阶函数
#由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向
#在其它模块也生效，要用import builtins; builtins.abs = 10。
#传入函数
#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，
#这种函数就称之为高阶函数。
#一个最简单的高阶函数：
def add(x, y, f):
    return f(x) + f(y)
#当我们调用add(-5, 6, abs)时，参数x，y和f分别接收-5，6和abs，
#根据函数定义，我们可以推导计算过程为：
# x = -5
# y = 6
# f = abs
# f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
# return 11
#用代码验证一下：
# -*- coding: utf-8 -*
def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6, abs))
#编写高阶函数，就是让函数的参数能够接收别的函数。
#小结
#把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。