print('~~~~~~~~~~~~必须参数~~~~~~~~~~~~')
def printme(str):
    "打印任何传入的字串符"
    print (str)
    return

# 调用printme函数，不加参数会报错
# printme()

# 调用printme函数，有参数不报错
printme("菜鸟教程")

print('以下实例中演示了函数参数的使用不需要使用指定顺序：')
def printinfo(name,age):
    print('名字：',name)
    print('年龄：',age)
    return

#调用printinfo函数
printinfo(age=50,name='runoob')
