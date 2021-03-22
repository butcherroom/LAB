print('~~~~~~~~~~~~传可变对象~~~~~~~~~~~~')
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1,2,3,4])
    print ('函数内取值：',mylist)
    return

# 调用changeme函数
mylist = [10,20,30]
changeme(mylist)
print("函数外取值：",mylist)

'''
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
'''