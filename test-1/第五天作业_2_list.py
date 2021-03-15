l1 = [4,5,7,1,3,9,0]
l2 = list.copy(l1)
l2.sort(reverse=False)

for i in range(len(l1)):
    print(l1[i],l2[i])