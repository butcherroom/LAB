list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

print('方案一：')
for item in list1:
    if item in list2:
        print(item , 'in List1 and List2')
    else:
        print(item, 'only in List1')

print('方案二：')
def find_same(a,b):
    for x in list1:
        print(x,'in list1 and list2') if x in list2 else print(x ,'only in list1')

print(find_same(list1,list2))