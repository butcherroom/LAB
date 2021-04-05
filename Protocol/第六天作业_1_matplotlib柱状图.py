from matplotlib import pyplot as plt
from 第五天作业_1_matplotlib饼状图显示netflow信息 import ssh_cmd
import re

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
plt.rcParams['font.family'] = 'sans-serif'
colorlist = ['r', 'b', 'g', 'y']

def mat_zhu(size_list, name_list):
    # 调节图形大小，宽，高
    plt.figure(figsize=(6, 6))

    # 横向柱状图
    # plt.barh(name_list, size_list, height=0.5, color=colorlist)

    # 竖向柱状图
    plt.bar(name_list, size_list, width=0.5, color=colorlist)

    # 添加主题和注释
    plt.title('协议与带宽分布')  # 主题
    plt.xlabel('带宽（M/s）')  # X轴注释
    plt.ylabel('协议')  # Y轴注释

    # 保存到图片
    plt.savefig('result1.png')
    # 绘制图形
    plt.show()

def get_netflow_app_zhutu(ip,username,password,cmd,port=22):
    show_result = ssh_cmd(ip,username,password,cmd,port=22)
    app_name_list = []
    app_bytes_list = []
    for line in show_result.strip().split('\n'):
        app_bytes = re.findall(r'[port|layer7]\s+(\w+)\s+(\d+)',line)
        if app_bytes:
            app_name_list.append(app_bytes[0][0])
            app_bytes_list.append(int(app_bytes[0][1]))
            print(app_name_list)
            print(app_bytes_list)
    mat_zhu(app_bytes_list,app_name_list)   #调用柱状图函数

if __name__ == '__main__':
    get_netflow_app_zhutu('192.168.100.150','cisco','cisco','show flow monitor name qytang-monitor cache format table')
