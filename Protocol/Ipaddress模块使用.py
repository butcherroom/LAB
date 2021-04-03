import ipaddress

ip_list=['192.168.1.1','127.16.1.1','192.2.3.4']
for ip in ip_list:
    ipaddr = ipaddress.ip_address(ip)   #ipaddress.ip_address中不能使用可迭代属性，需要通过for循环吧IP字符串提取出来
    print(ip)


for ipx in ipaddress.ip_network('192.168.1.0/24'):  #使用ip_network,至一定要是一个网段的网络号+掩码位（即192.168.1.0/24，不可为192.168.1.33/24）
    print(ipx)

net = ipaddress.ip_network('19.1.1.0/29')
a = ipaddress.ip_address('19.1.1.1')
b = ipaddress.ip_address('192.1.1.1')
if a in net:
    print('地址在范围内！')

if b in net:
    print('地址在范围内！')
else:
    print('地址不在范围内！')