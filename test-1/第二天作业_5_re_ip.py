import re
str='port-channel1.189      192.168.189.254   YES    CONFIG    up'

if_show = re.match(r'([a-z]+-[a-z]+\d?\.\d*)\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\S.*(\w{2})$', str).groups()

print('-'*120)
print('接口\t\t:',if_show[0])
print('IP地址\t:',if_show[1])
print('状态\t\t:',if_show[2])
