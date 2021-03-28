import paramiko
from argparse import ArgumentParser
def qytang_ssh(ip,username,password,cmd,port):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=username, password=password,timeout=3, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

usage = 'usage: python Simple_SSH_Client -i ipaddr -u username -p password -c command'

parser = ArgumentParser(usage=usage)

parser.add_argument('-i','--ipaddr',dest='ip',help='show this help message and exit',default='192.168.1.167',type=str)
parser.add_argument('-u','--USERNAME',dest='username',help='SSH Username',default='cisco',type=str)
parser.add_argument('-p','--PASSWORD',dest='password',help='SSH Password',default='cisco',type=str)
parser.add_argument('-c','--cmd',dest='command',help='Shell Command',default='show ip int brief',type=str)
args = parser.parse_args()

print(qytang_ssh(args.ip, args.username, args.password, cmd=args.command, port = 22))

if __name__ == '__main__':
    # print(qytang_ssh('192.168.1.167','cisco','cisco','show run'))
    pass



