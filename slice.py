#切片
#取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取前3个元素，应该怎么做？
#笨办法：
print([L[0], L[1], L[2]])
#之所以是笨办法是因为扩展一下，取前N个元素就没辙了。
#取前N个元素，也就是索引为0-(N-1)的元素，可以用循环：
r = []
n=3
for i in range(n):
    r.append(L[i])
print(r)
#对这种经常取指定索引范围的操作，用循环十分繁琐，
#因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
print('对应上面的问题，取前3个元素，用一行代码就可以完成切片：')
print(L[0:3])
#L[0:3]表示，从索引0开始取，直到索引3为止，
#但不包括索引3。即索引0，1，2，正好是3个元素。
#如果第一个索引是0，还可以省略：
print(L[:3])
#也可以从索引1开始，取出2个元素出来：
print(L[1:3])
#类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
print('类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：')
print(L[-2:])
print(L[-2:-1])
#记住倒数第一个元素的索引是-1。
#切片操作十分有用。我们先创建一个0-99的数列：
print('创建一个0-99的数列')
L = list(range(100))
print(L)
print('前10个数:')
print(L[:10])
print('后10个数：')
print(L[-10:])
print('前11-20个数:')
print( L[10:20])
print('前10个数，每两个取一个:')
print(L[:10:2])
print('所有数，每5个取一个：')
print(L[::5])
print('只写[:]就可以原样复制一个list：')
print(L[:])
#tuple也是一种list，唯一区别是tuple不可变。
#因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0, 1, 2, 3, 4, 5)[:3])
#字符串'xxx'也可以看成是一种list，
#每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])
#练习
#利用切片操作，实现一个trim()函数，
#去除字符串首尾的空格，注意不要调用str的strip()方法：
# -*- coding: utf-8 -*-
print('方法一：')
def trim(s): 
    if len(s) == 0: 
        return "" 
    head = 0 
    tail = len(s) 
    while s[head] == " ": 
        head += 1 
        if head == len(s): 
            return "" 
    while s[tail - 1] == " ": 
        tail -= 1 
    return s[head:tail]
# 测试:
print('trim(hello   ) =',trim('hello   '))
print('trim(  hello) =', trim('  hello'))
print('trim(  hello  ) =', trim('  hello  '))
print('trim(  hello  world  ) =', trim('  hello  world  '))
print('trim('') =', trim(''))
print('trim('    ') =', trim(''))
if trim('hello ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
print('方法二：')
def trim(s):
    if len(s) == 0: 
        return "" 
    if s[:1] == " ": 
        return trim(s[1:]) 
    elif s[-1:] == " ": 
        return trim(s[:-1]) 
    else: 
        return s
# 测试:
print('trim(hello   ) =',trim('hello   '))
print('trim(  hello) =', trim('  hello'))
print('trim(  hello  ) =', trim('  hello  '))
print('trim(  hello  world  ) =', trim('  hello  world  '))
print('trim('') =', trim(''))
print('trim('    ') =', trim(''))
if trim('hello ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


