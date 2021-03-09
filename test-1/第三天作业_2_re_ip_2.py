import re
str='TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'


if_show = re.match(r'(\w+)\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,5})\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,5}).\s\w+\s(\d{1,2}.\d{1,2}.\d{1,2}).\s\w+\s(\d{1,10}).\s+\w+\s+(\w+)',str).groups()

idle = if_show[3].split(':')

idle_hour = idle[0]
idle_min = idle[1]
idle_sec = idle[2]

idle_new = '%-2s小时%3s分钟%3s秒' % (idle_hour,idle_min,idle_sec)

line1 = '{0:<15}{1:^2}{2:<5}'.format('Protocol',':',if_show[0])
line2 = '{0:<15}{1:^2}{2:<5}'.format('Server',':',if_show[1])
line3 = '{0:<15}{1:^2}{2:<5}'.format('Localserver',':',if_show[2])
line4 = '{0:<15}{1:^2}{2:<5}'.format('Idle',':',idle_new)
line5 = '{0:<15}{1:^2}{2:<5}'.format('Bytes',':',if_show[4])
line6 = '{0:<15}{1:^2}{2:<5}'.format('Flags',':',if_show[5])

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
