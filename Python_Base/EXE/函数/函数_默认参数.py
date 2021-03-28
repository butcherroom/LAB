#调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值：
print('以下实例中演示了函数参数的使用不需要使用指定顺序：')
def printinfo(name,age=35):
    print('名字：',name)
    print('年龄：',age)
    return

#调用printinfo函数，修改默认参数
print('指定特定的年龄：')
printinfo(age=50,name='runoob')

#调用printinfo函数，默认参数不指定，则显示默认值35
print('不指定年龄：')
printinfo (name='tanzj')
