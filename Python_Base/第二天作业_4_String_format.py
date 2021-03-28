department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_ bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

line_1 = 'Department1 name:%s\tManager:%s\tCOURSE FEES:%f\tThe End!'  % (department1,depart1_m,COURSE_FEES_SEC)
line_2 = 'Department2 name:{}\t\tManager:{}\t\tCOURSE FEES:{}\t\tThe End!'.format(department2,depart2_m,COURSE_FEES_Python)

length=len(line_1)
print('='*length)
print(line_1)
print(line_2)
print('='*length)