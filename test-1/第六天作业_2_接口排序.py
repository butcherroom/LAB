import re
port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']

for i in port_list:
    port_re = re.match(r'\w+\s+(\d/\d\d\d/\d/\d{1,2})',i).groups()
    print(port_re[1])
# p = (re.match(r'\w+\s+(\d/\d\d\d/\d/\d{1,2})',i).(lambda a,b,c,d:"eth a/b/c/d"))
