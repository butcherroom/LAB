import os
import re
route_n_result = os.popen("route -n").read()

fine_gw = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+0\.0\.0\.0+\s+UG',route_n_result)
route_gw = '%-5s%s' % ('默认网关为：',fine_gw[0])
print(route_gw)
