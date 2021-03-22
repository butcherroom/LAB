#######作用域1#########
# A = 1  #全局变量
# def func(B,C): #B、C为函数本地变量
#     Z=A+B+C     #A为全局变量，赋值需要使用‘global’，但是读取并不需要‘global’
#     return Z
#
# print(func(2,3))

#######作用域2#########
# A = 1  #全局变量
# def func(A,B,C): #A、B、C为函数本地变量
#     Z=A+B+C      #函数本地变量A,与全局变量A没有关系
#     return Z     #函数运行结束后本地变量就会消失
#
# print(func(4,5,6)) #A被赋值为4，B赋值为5，C赋值为6
# print(A)     # A的值还为全局变量


#######Global-1#########
# X=88
# def globalfunc():
#     global X
#     X = 99
#
# globalfunc()
# print(X)

#######Global-2#########
y,z=1,2
def all_global():
    global x    #没有这个全局标量，就创建一个
    x = y + z

all_global()
print(x)