import re
str='166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

if_show = re.match(r'(\d{0,5})\s+(\w{4}\.\w{4}\.\w{4})\s+(\w+)\s+(\w+/\d+/\d+)',str).groups()

#######################字串符拼接##########################
# print('-'*120)
# print('接口\t\t:',if_show[0])
# print('IP地址\t:',if_show[1])
# print('类型\t:',if_show[2])
# print('状态\t\t:',if_show[3])

#######################f-string##########################
vid_info = 'Vlan'
mac_info  = 'MAC'
type_info = 'Type'
interface_info = 'Interface'

vlan_id = if_show[0]
mac = if_show[1]
type    = if_show[2]
interface = if_show[3]
maohao = ":"

f_string_1 = f'{vid_info:10}{maohao:^6}{vlan_id:10}'
f_string_2 = f'{mac_info:10}{maohao:^6}{mac:10}'
f_string_3 = f'{type_info:10}{maohao:^6}{type:10}'
f_string_4 = f'{interface_info:10}{maohao:^6}{interface:10}'

print(f_string_1)
print(f_string_2)
print(f_string_3)
print(f_string_4)