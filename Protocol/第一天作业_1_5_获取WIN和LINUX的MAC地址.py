import netifaces
import platform


def get_mac(ifname):
    if platform.system() == "Linux":
        try:
            return netifaces.ifaddresses(ifname)[netifaces.AF_LINK][0]['addr']  #AF_LINK代表MAC地址
        except ValueError:
            return None
    elif platform.system() == "Windows":
        from 第一天作业_1_3_获取WIN下的唯一网卡码 import win_from_name_get_id
        if_id = win_from_name_get_id(ifname)
        if not if_id:
            return
        else:
            return netifaces.ifaddresses(if_id)[netifaces.AF_LINK][0]['addr']
    else:
        print('操作系统不支持,本脚本只能工作在Windows或者Linux环境!')


if __name__ == "__main__":
    if platform.system() == "Linux":
        print(get_mac('ens33'))
    elif platform.system() == "Windows":
        print(get_mac('VMware Network Adapter VMnet1'))
