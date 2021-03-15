import re
asa_conn = "ddd fff ccc eeee"
for conn in asa_conn.split(" "):
    aaa = re.match(r'(\w+)',conn).groups()
    print(aaa)