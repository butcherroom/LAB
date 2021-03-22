import hashlib
import time
import re
from 第九天作业_1_SSH登录 import qytang_ssh

def get_config(ip,username,password,cmd,port):
    try:
        config_raw = qytang_ssh(ip,username,password,cmd,port)
        split_result = re.split(r'hostname\s+\S+\r\n',config_raw)
        device_config = config_raw.replace(split_result[0],'').strip()
        return device_config
    except Exception:
        return

def compare_config_diff(ip,username,password,cmd,port):
    before_md5 = ''
    while True:
        device_config = get_config(ip,username,password,cmd,port)
        m = hashlib.md5()
        m.update(str(device_config).encode())
        device_md5 = m.hexdigest()
        print(device_md5)
        if not before_md5:
            before_md5 = device_md5
        elif before_md5 != device_md5:
            print('Device config has be changed!')
            break
        time.sleep(5)

if __name__ == "__main__":
    # print(get_config('192.168.31.19','cisco','cisco','show run','22'))
    print(compare_config_diff('192.168.31.19','cisco','cisco','show run',22))

