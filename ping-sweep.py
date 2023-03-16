#import os

#this is a basic ping sweeper to send 5 ICMP echo packets to the target ipaddress range 10.11.1.0/24

#for i in range(256):
#    i=str(i)
#    os.system("ping -c 5 10.11.1."+i)



import os
import sys
#
### this script accepts 3 arguments - the first 3 octets of an ipv4 address, the starting value of the last octet, the ending value of the last octet. arguments 2 and 3 effectively form a range from arg2 to arg3.
### this script prints out one ip per line if the pinged host responds appropriately, otherwise no other output is printed.

### get our arguments from the command line:

arg1=str(sys.argv[1])
arg2=int(sys.argv[2])
arg3=int(sys.argv[3])

### our function

def pingsweep(arg1,arg2,arg3):
    for i in range(arg2,arg3+1):
        host=str(i)
        first3octets=str(arg1)
        response=(os.system("ping -n -c 1 "+first3octets+"."+host+" 2>&1 >/dev/null"))
        if response == 0:
            print(first3octets+"."+host)

pingsweep(arg1,arg2,arg3)

# end of script
