from 第四天作业_1_安装matplotlib模块并测试饼状图 import mat_bing
import paramiko
import re

def ssh_cmd(ip,username,password,cmd,port=22):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=22, username=username, password=password,timeout=3, compress=True)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        x = stdout.read().decode()
        ssh.close()
        return x
    except Exception as e:
        print('%stErrorn %s'%(ip,e))

def get_netflow_app(ip,username,password,cmd,port=22):
    show_result = ssh_cmd(ip,username,password,cmd,port=22)
    app_name_list = []
    app_bytes_list = []
    for line in show_result.strip().split('\n'):
        app_bytes = re.findall(r'[port|layer7]\s+(\w+)\s+(\d+)',line)
        if app_bytes:
            app_name_list.append(app_bytes[0][0])
            app_bytes_list.append(int(app_bytes[0][1]))
            print(app_name_list)
            print(app_bytes_list)
    mat_bing(app_bytes_list,app_name_list)

if __name__ == '__main__':
    get_netflow_app('192.168.100.150','cisco','cisco','show flow monitor name qytang-monitor cache format table')
