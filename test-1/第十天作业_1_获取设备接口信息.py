from 第八天作业_3_创建一个简单的ping函数 import qytang_ping
from 第九天作业_1_SSH登录 import qytang_ssh
import re
import pprint

def get_int_info(*ips,username,password):
    intf_dirc = {}
    for ip in ips:
        if_dict = {}
        if qytang_ping(ip):
            for line in qytang_ssh(ip,username,password,'show ip int b').split('\n'):
                intf_ip = re.match(r'(\w+\d/\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',line.strip())
                if intf_ip:
                    if_dict[intf_ip.groups()[0]] = intf_ip.groups()[1]
                intf_dirc[ip] = if_dict
    return intf_dirc

if __name__ == '__main__':
    pprint.pprint(get_int_info('192.168.31.20','192.168.31.19',username = 'cisco',password = 'cisco'),indent=4)

# 测试正则表达式
# i = 'Ethernet0/0                192.168.1.63    YES DHCP   up                    up'
# dir = {}
# m = re.match(r'(\w+\d/\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',i).groups()
# dir[m[0]] = m[1]
# print(dir)



