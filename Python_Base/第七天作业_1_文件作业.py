import os
# os.mkdir('test')
# os.chdir('test')
# qytang1 = open('qytang1','w')
# qytang1.write('test file\n')
# qytang1.write('this is qytang\n')
# qytang1.close()
# qytang2 = open('qytang2','w')
# qytang2.write('test file\n')
# qytang2.write('qytang python\n')
# qytang2.close()
# qytang3 = open('qytang3','w')
# qytang3.write('test file\n')
# qytang3.write('this is python\n')
# qytang3.close()
# os.mkdir('qytang4')
# os.mkdir('qytang5')
# os.chdir('qytang5')
# qytang5 = open('qytang5','w')
# qytang5.write('test file\n')
# qytang5.write('this is python\n')
# qytang5.close()
# print('方案1')
# os.chdir('test')
# print('文件中包含”qytang“关键字的文件为：')
# for file_or_dir in os.listdir(os.getcwd()):
#     if os.path.isfile(file_or_dir):
#         for hang in open(file_or_dir):
#             if "qytang" in hang:
#                 print(file_or_dir)
#                 break
'''
os.walk的函数声明为:
walk(top, topdown=True, οnerrοr=None, followlinks=False)
参数
top 是你所要便利的目录的地址
topdown 为真，则优先遍历top目录，否则优先遍历top的子目录(默认为开启)onerror 需要一个callable对象，当walk需要异常时，会调用
followlinks 如果为真，则会遍历目录下的快捷方式(linux下是symbolic link)实际所指的目录(默认关闭)
os.walk 的返回值是一个生成器(generator), 也就是说我们需要不断的遍历它，来获得所有的内容。

每次遍历的对象都是返回的是一个三元组(root, dirs, files)

root    所指的是当前正在遍历的这个文件夹的本身的地址
dirs    是一个list ，内容是该文件夹中所有的目录的名字(不包括子目录)
files   同样是list, 内容是该文件夹中所有的文件(不包括子目录)如果topdown参数为真，walk会遍历top文件夹，与top文件夹中每一个子目录。
'''
print('方案2')
for root,dirs,files in os.walk(os.getcwd(),topdown=False):
    for file_name in files:
        for line in open(os.path.join(root,file_name)):
            if "qytang" in line:
                print ('\t'+os.path.join(root,file_name))
                break













