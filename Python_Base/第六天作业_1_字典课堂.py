import re
asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n " \
           "TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"
asa_dict = {}
conn = ()
# re_result = re.match(r'\w+\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).\s+\w+\s+\d+.\d+.\d+.\s+\w+\s+(\d+).\s+\w+\s+(\w+)',asa_conn).groups()
# print(re_result)
for conn in asa_conn.split('\n'):
    re_result = re.match(r'\w+\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).\s+\w+\s+\d+.\d+.\d+.\s+\w+\s+(\d+).\s+\w+\s+(\w+)',asa_conn).groups()
    asa_dict[re_result[0],re_result[1],re_result[2],re_result[3]] = (re_result[4],re_result[5])
    print('打印分析后的字典！\n')
    print(asa_dict)

# src = 'src'
# src_ip = 'src_ip'
# dst = 'dst'
# dst_ip = 'dst_ip'
# bytes_name = 'bytes'
# flags = 'flags'
# format_str1 =
# format_str2 =
#
# print('\n格式化打印输出\n')
#
# for key,value in asa_dict.items():

