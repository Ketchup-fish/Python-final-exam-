#关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0个或任意个含参数名的参数，
#这些关键字参数在函数内部自动组装为一个dict。请看示例：
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
#函数person除了必选参数name和age外，还接受关键字参数kw。
#在调用该函数时，可以只传入必选参数：
person('Michael', 30)
#也可以传入任意个数的关键字参数：
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
#关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，
#我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，
#我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，
#其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
#当然，上面复杂的调用可以用简化的写法：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
#kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。