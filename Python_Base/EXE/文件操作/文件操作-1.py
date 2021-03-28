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
for (root, dirs, files) in os.walk(os.getcwd()):
    for file_name in files:
        for line in os.path.join(root,file_name):
            if "qytang" in line:
                print(file_name)
