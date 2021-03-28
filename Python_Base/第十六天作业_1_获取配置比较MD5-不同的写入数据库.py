import sqlite3
import re
import hashlib
import paramiko

device_list = ['192.168.1.167','192.168.1.168']
username = "cisco"
password = "cisco"

def qytang_ssh(ip,username,password,cmd,port):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username=username, password=password,timeout=3, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

def make_config_md5(ip, username, password):
    config_raw = qytang_ssh(ip, username, password, cmd='show run', port=22)
    config_result = re.split(r'hostname\s+\S+',config_raw)
    device_result = config_raw.replace(config_result[0],'\n').strip()
    m = hashlib.md5()
    m.update(device_result.encode())
    md5_value=m.hexdigest()
    return device_result,md5_value

def write_config_to_db():
    conn = sqlite3.connect('qytang_config_db.sqlite')
    cursor = conn.cursor()
    for device in device_list:
        get_info = make_config_md5(device, username, password)
        cursor.execute('select * from config_db where IP地址=?',(device,))
        md5_info = cursor.fetchall()
        if not md5_info:
            cursor.execute("insert into config_db values (?,?,?)", (device , get_info[0] , get_info[1]))
            conn.commit()
        else:
            if md5_info[0][2] != get_info[1]:
                cursor.execute("insert into config_db values (?,?,?)", (device, get_info[0], get_info[1]))
                conn.commit()
            else:
                continue

    cursor.execute('select * from config_db')
    result_all = cursor.fetchall()
    print(result_all)
    for x in result_all:
        print(x[0],x[2])
    conn.close()

if __name__ == '__main__':
    # print(make_config_md5(ip,username,password))
    # import os
    # if  os.path.exists('qytang_config_db.sqlite'):
    #     os.remove('qytang_config_db.sqlite')
    #
    # conn = sqlite3.connect('qytang_config_db.sqlite')
    # cursor = conn.cursor()
    #
    # cursor.execute("create table config_db('IP地址' varchar(40),'配置' varchar(40),'MD5' varchar(40))")
    # conn.commit()
    # conn.close()
    write_config_to_db()


