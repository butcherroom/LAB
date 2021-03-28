from 第九天作业_1_SSH登录 import qytang_ssh
import re

def ssh_route_gw(ip, username, password):
    route_table = qytang_ssh(ip, username, password, cmd='route -n')
    for line in route_table.split('\n')[2:-1]:
        route_gw = re.findall(r'0\.0\.0\.0\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+0\.0\.0\.0\s+(\w+)',line.strip())
        if route_gw:
            if route_gw[0][1] == 'UG':
                return route_gw[0][0]

if __name__ == '__main__':
    print('网关为:',ssh_route_gw('192.168.100.100', 'root', 'Root~123'))





