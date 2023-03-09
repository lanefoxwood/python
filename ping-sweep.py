import os

#this is a basic ping sweeper to send 5 ICMP echo packets to the target ipaddress range 10.11.1.0/24

for i in range(256):
    i=str(i)
    os.system("ping -c 5 10.11.1."+i)