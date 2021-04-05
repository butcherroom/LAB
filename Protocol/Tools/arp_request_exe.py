# import logging
#
# logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 清除报错
# from kamene.all import *
# # from tools.get_ip_netifaces import get_ip_address  # 获取本机IP地址
# # from tools.get_mac_netifaces import get_mac_address  # 获取本机MAC地址
# # from tools.scapy_iface import scapy_iface  # 获取scapy iface的名字
# # from tools.get_ifname import get_ifname  # 获取接口唯一ID
#
#
# def arp_request(ip_address, ifname='ens33'):
#     # 获取本机IP地址
#     # localip = get_ip_address(ifname)
#     # 获取本机MAC地址
#     # localmac = get_mac_address(ifname)
#     try:  # 发送ARP请求并等待响应
#         result_raw = sr1(ARP(
#                              # 注释掉的都为可选项
#                              # op=1,
#                              # hwsrc=localmac,
#                              # hwdst='00:00:00:00:00:00',
#                              # psrc=localip,
#                              pdst=ip_address),
#                          # iface=scapy_iface(ifname),
#                          timeout=1,
#                          verbose=False)
#         return ip_address, result_raw.getlayer(ARP).fields.get('hwsrc')
#
#     except AttributeError:
#         return ip_address, None
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import kamene                   #from的形式无法导入kamene
from kamene.all import *        #kamene一定要以这个方式导入
def arp_request(ipaddr,ifname='ens33'):
    try:
        arp_raw = sr1(ARP(pdst=ipaddr),timeout=1,verbose=False)
        return ipaddr,arp_raw.getlayer(ARP).fields.get('hwsrc')
    except AttributeError:
        return ipaddr,None

if __name__ == "__main__":
    # Windows Linux均可使用
    arp_result = arp_request('192.168.31.111')
    print("IP地址:", arp_result[0], "MAC地址:", arp_result[1])
