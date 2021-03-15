import os
import re
ifconfig_result = os.popen('ifconfig '+'ens33').read()

ipv4_add = re.findall(r'inet\s+(\d{1,3}\.\d{1,3}.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
netmask = re.findall(r'netmask\s+(\d{1,3}\.\d{1,3}.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
broadcast = re.findall(r'broadcast\s+(\d{1,3}\.\d{1,3}.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
mac_addr = re.findall(r'ether\s+(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})',ifconfig_result)[0]

format_string_1 = '{0:<10}{1:^3}{2:^10}'.format('ipv4_add',':',ipv4_add)
format_string_2 = '{0:<10}{1:^3}{2:^10}'.format('netmask',':',netmask)
format_string_3 = '{0:<10}{1:^3}{2:^10}'.format('broadcast',':',broadcast)
format_string_4 = '{0:<10}{1:^3}{2:^10}'.format('mac_addr',':',mac_addr)

ipv4_split = re.split('\.',ipv4_add)
ipv4_gw = f'{ipv4_split[0]}.{ipv4_split[1]}.{ipv4_split[2]}.1'

print(format_string_1)
print(format_string_2)
print(format_string_3)
print(format_string_4)

print('\n我们假设网关IP地址最后一位为1，因此网关IP地址为：'+ipv4_gw +'\n')
pint_result = os.popen('ping '+ ipv4_gw + ' -c 1').read()
re_ping_result = re.findall('time=',pint_result)

if re_ping_result:
    print('网关可达！')
else:
    print('网关不可达！')
