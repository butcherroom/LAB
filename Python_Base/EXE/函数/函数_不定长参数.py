print('加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数')
# 可写函数说明
def printinfo(arg1,*vartuple):
    print("输出：")
    print(arg1)
    print(vartuple)
    return

#调用printinfo函数
printinfo(70,60,50)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：')
def printinfo(arg1,*vartuple1):
    print("输出：")
    print(arg1)
    for var in vartuple1:
        print(var)
    return

#调用printinfo函数
printinfo(10)
printinfo(70,60,50)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('加了两个星号 ** 的参数会以字典的形式导入')

# 可写函数说明
def printinfo(arg1, **vardict2):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict2)

# 调用printinfo 函数
printinfo(1, a=2, b=3)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('声明函数时，参数中星号 * 可以单独出现，如果单独出现星号 * 后的参数必须用关键字传入')
def f(a,b,*,c):
    return a+b+c

#f(1,2,3)   # 报错
f(1,2,c=3)  # 正常