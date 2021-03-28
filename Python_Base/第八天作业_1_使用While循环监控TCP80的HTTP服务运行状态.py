import os
import re
import time
while True:
    netstat_info = os.popen("netstat -tulnp").read()
    ifnot = False
    for line in netstat_info.split('\n'):
        netstat_find = re.findall(r'tcp\s+\w+\s+\w+\s+0\.0\.0\.0:80\s+',line)
        if netstat_find:
            print("HTTP (TCP/80)服务已经被打开")
            ifnot = True
            break
    if ifnot:
        break
    print("等待一秒重新开始监控！")
    time.sleep(1)



