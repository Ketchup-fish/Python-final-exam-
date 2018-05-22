#在Python中，这种一边循环一边计算的机制，称为生成器：generator。
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，
#就创建了一个generator：
g = (x * x for x in range(10))
for n in g:
    print(n)
#generator非常强大。如果推算的算法比较复杂，
#用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
#比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，
#任意一个数都可由前两个数相加得到：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
for n in fib(6):
    print(n)
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
#这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，
#那么这个函数就不再是一个普通函数，而是一个generator：
#这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，
#遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
#在每次调用next()的时候执行，
#遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
print('###########################')
#练习
#杨辉三角定义如下：

          # 1
         # / \
        # 1   1
       # / \ / \
      # 1   2   1
     # / \ / \ / \
    # 1   3   3   1
   # / \ / \ / \ / \
  # 1   4   6   4   1
 # / \ / \ / \ / \ / \
# 1   5   10  10  5   1

# 把每一行看做一个list，试写一个generator，不断输出下一行的list：
print('方法一：')
#我的思路：上一行的两个数组元素递增的两两相加，得到下一行对应的值，且每行的长度递增1
#观察半天数据结构，发现在每行的首尾加一个“0”，更能用while循环生成下一行，
#生成结果用list[1:-1]切片
def triangles(): 
    l = [0, 1, 0] 
    l1 = [] 
    n, count = 0, 0 
    while n < 10:
        yield l[1:-1] 
        while count + 1 < len(l): 
            l1.append(l[count] + l[count + 1]) 
            count += 1 
        count = 0 
        n += 1 
        l = l1 
        l1 = [] 
        l.insert(0, 0) 
        l.append(0)
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
	
print('##########################')
print('方法二：')
def triangles(): 
    L = [1] 
    n = 0 
    while True: 
        yield L 
        L = [1] + [L[i] + L[i+1] for i in range(n)] + [1] 
        n = n + 1 
    return 
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

for i in range(10):
    print(i)
#请注意区分普通函数和generator函数，普通函数调用直接返回结果：
#generator函数的“调用”实际返回一个generator对象：


