import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

def qytang_ping(ip):
    ping_pkt = IP(dst=ip)/ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ip, True
    else:
        return ip, False

if __name__ == '__main__':
   ping_status = qytang_ping('baidu.com')
   if ping_status[0]:
       print(ping_status[0],'通!')
   else:
       print(ping_status[0],'不通')



