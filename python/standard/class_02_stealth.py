import nmap

# plz, check first
# 1. already installed nmap on windows system https://nmap.org/download.html
# 2. run as administrator
nm = nmap.PortScanner()\
# what is -sS option
# https://nmap.org/book/synscan.html#:~:text=SYN%20scan%20is%20the%20default,not%20hampered%20by%20intrusive%20firewalls.&text=SYN%20scan%20may%20be%20requested,the%20%2DsS%20option%20to%20Nmap.

nm.scan('127.0.0.1', '7770-7780', arguments='-sS')
for host in nm.all_hosts():
    print('-------------------------------------------------')
    print('Host : %s (%s)' %(host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    proto = 'tcp'
    print('--------')
    print('Protocol : %s' %proto)
    lport = nm[host][proto].keys()
    for port in lport:
      print ('port : %s\tstate : %s' % (port,
      str(nm[host][proto][port]['state'])))
print("all complete")

# UDP
# nm.scan('127.0.0.1', '7777', arguments='-sU')
# print(nm)
# for host in nm.all_hosts():
#     print('-------------------------------------------------')
#     print('Host : %s (%s)' %(host, nm[host].hostname()))
#     print('State : %s' % nm[host].state())
#     proto = 'udp'
#     print('--------')
#     print('Protocol : %s' %proto)
#     lport = nm[host][proto].keys()
#     for port in lport:
#       print ('port : %s\tstate : %s' % (port,
#       str(nm[host][proto][port]['state'])))
# print("all complete")