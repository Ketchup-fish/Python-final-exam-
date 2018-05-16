def power(x):
    return x * x
print('power(5)=',power(5))
print('power(15)=',power(15))
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5,2))
print(power(5,3))
#修改后的power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，
#调用函数时，传入的两个值按照位置顺序依次赋给参数x和n