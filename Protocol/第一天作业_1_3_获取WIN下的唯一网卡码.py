import netifaces as ni
import winreg as wr

# a = ni.interfaces()      #windows下返回注册表值(一长串字符)；Linux下则直接返回接口名称(ip addr看到的）
# print(a)

#window输出
#['{D1CDB94E-16B4-4540-A200-CDC5A6C4AC29}', '{3D534196-DED7-447D-B8D5-534694FD8FB8}', '{8D272EBD-2C4B-4620-B699-22556411E735}', '{AF62E3D3-0A6C-4CEA-8AEE-16BEAE33348A}', '{CEF29897-D95C-4A34-81A9-FA4125B056BB}', '{F722A6A3-BC89-4C49-8D0B-CC2E75FD4783}', '{159449A7-803C-4D6C-810A-C4A73CF894C1}', '{40103AAA-3E06-415F-8579-78F92F9265AA}', '{5BEDA34A-D66C-461A-B5C4-0E0FED0339AC}', '{B9B32C12-C1EB-11EA-9309-806E6F6E6963}', '{D211D2F1-A23B-472B-80C8-3ED821F34CCF}']

#Linux输出
# ['lo', 'ens33', 'ens37']

def get_connection_name_from_guid(iface_guids):
    wr = __import__('winreg', globals(), locals(), ['wr'])
    iface_dict = {}
    reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
    reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
    for i in iface_guids:
        try:
            reg_subkey = wr.OpenKey(reg_key, i + r'\Connection')
            iface_dict[wr.QueryValueEx(reg_subkey, 'Name')[0]] = i
        except FileNotFoundError:
            pass
    return iface_dict


def win_from_name_get_id(ifname):
    x = ni.interfaces()
    return get_connection_name_from_guid(x).get(ifname)

if __name__ == "__main__":
    import platform
    if platform.system() == "Windows":
        print(win_from_name_get_id("VMware Network Adapter VMnet8"))

