def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))
print(power(5,2))
print(power(5,3))
print('######################')
# 而对于n > 2的其他情况，就必须明确地传入n，比如power(5, 3)。
# 从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
# 举个例子，我们写个一年级小学生注册的函数，需要传入name和gender两个参数：
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)
enroll('Sarah','F')
print('######################')
# 如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。
# 我们可以把年龄和城市设为默认参数：
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
enroll('Sarah','F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')
print('######################')
enroll('Adam', 'M', city='Tianjin')
# 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
# 先定义一个函数，传入一个list，添加一个END再返回：
print('添加END')
def add_end(L=[]):
    L.append('END')
    return L
#当你正常调用时，结果似乎不错：
print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
print(add_end())
print(add_end())
print(add_end())
#定义默认参数要牢记一点：默认参数必须指向不变对象！ 
#要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

#现在，无论调用多少次，都不会有问题：
print(add_end())
print(add_end())
