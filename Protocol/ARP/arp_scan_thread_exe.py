import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
import ipaddress
from multiprocessing.pool import ThreadPool
from arp_request_exe import arp_request
from time_decorator_exe import run_time

@run_time()
def kamene_arp_scan(network, ifname):
    net = ipaddress.ip_network(network)
    ip_list = [str(ip) for ip in net]
    pool = ThreadPool(processes=100)
    result = [pool.apply_async(arp_request,args=(i,ifname))for i in ip_list]
    pool.close()
    pool.join()
    scan_dirc = {}
    for r in result:
        if r.get()[1]:
            scan_dirc[r.get()[0]]=r.get()[1]
    return scan_dirc

if __name__ == '__main__':
    # Windows Linux均可使用
    for ip, mac in kamene_arp_scan("192.168.31.0/27", 'ens33').items():
        print('ip地址:'+ip+'是活动的,它的MAC地址是:'+mac)

