import paramiko
import time
import re

def qytang_multicmd(ip, username, password, port, cmd_list, enable, wait_time=1, verbose=True):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip ,port, username, password, timeout=5 , compress=True)
    chan = ssh.invoke_shell()
    time.sleep(wait_time)
    x = chan.recv(2048).decode()
    check_enable = re.findall(r'(>$)',x)
    if enable and '>' in check_enable:
        chan.send('enable'.encode())
        chan.send(b'\n\r')
        chan.send(enable.encode())
        chan.send(b'\n\r')
        time.sleep(wait_time)
    elif not enable and '>' in check_enable:
        print('需要Enable密码！')
        return

    for config_cmd in cmd_list:
        chan.send(config_cmd.encode())
        chan.send(b'\n')
        # chan.send(chr(32))     #发送空格使配置输出完整
        time.sleep(wait_time)
        config_status = chan.recv(40960).decode()
        if verbose:
            print(config_status)
    chan.close()
    ssh.close()

if __name__ == '__main__':
    ##函数传递方式一
    # cmd_list1 = ['terminal length 0', 'show ver', 'config t', 'router ospf 1', 'network 0.0.0.0 0.0.0.0 a 0']
    # qytang_multicmd(ip = '192.168.1.167', username = 'cisco', password = 'cisco' , port = 22, cmd_list = cmd_list1 , enable = 'cisco' , wait_time=1, verbose=True)

    ##函数传递方式二
    cmd_list2 = ('192.168.1.167',
                 'cisco',
                 'cisco',
                 '22',
                 ['terminal length 0',
                  'show ver',
                  'config t',
                  'router ospf 1',
                  'network 0.0.0.0 0.0.0.0 a 0'],
                 'cisco',   #enable密码
                 1,
                 True
                 )

    qytang_multicmd(*cmd_list2)





