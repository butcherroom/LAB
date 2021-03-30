import ipaddress

ip_list = ['192.16.12.123',
           '156.166.13.3',
           '172.16.12.234',
           '192.16.12.12',
           '172.16.12.23',
           '192.168.1.1',
           '18.2.9.45',
           '202.39.48.10'
           ]

def sort_ip(ips):
    return sorted(ips, key=lambda ip: ipaddress.ip_address(ip))

if __name__ == "__main__":
    print(sort_ip(ip_list))
