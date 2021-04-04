import platform

def get_ifname(ifname):
    if platform.system() == "Linux":
        return ifname
    elif platform.system() == "Windows":
        from 第一天作业_1_3_获取WIN下的唯一网卡码 import win_from_name_get_id
        return win_from_name_get_id(ifname)
    else:
        return None


if __name__ == "__main__":
    import platform
    if platform.system() == "Linux":
        print(get_ifname('ens33'))
    elif platform.system() == "Windows":
        print(get_ifname('VMware Network Adapter VMnet1'))
