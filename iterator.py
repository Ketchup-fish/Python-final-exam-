#我们已经知道，可以直接作用于for循环的数据类型有以下几种：
#一类是集合数据类型，如list、tuple、dict、set、str等；
#一类是generator，包括生成器和带yield的generator function。
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#可以使用isinstance()判断一个对象是否是Iterable对象：
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))
#而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
#直到最后抛出StopIteration错误表示无法继续返回下一个值了。
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#可以使用isinstance()判断一个对象是否是Iterator对象：
print('判断Iterator')
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))
#你可能会问，为什么list、dict、str等数据类型不是Iterator？
#这是因为Python的Iterator对象表示的是一个数据流，Iterator对象
#可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出
#StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前
#知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator
#的计算是惰性的，只有在需要返回下一个数据时它才会计算。
#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。
#而使用list是永远不可能存储全体自然数的。
#小结
#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
#Python的for循环本质上就是通过不断调用next()函数实现的，例如：
# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)
	
print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}
# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)
	
# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)
	
# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)