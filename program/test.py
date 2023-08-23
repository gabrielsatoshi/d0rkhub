from scapy.all import *
import sys

def scan_ports(target, low_port, high_port):
    ip_address = target.resolve()
    try:
        response = sr1(IP(dst=ip_address)/tcp, sport=(low_port, high_port), verbose=0)
    except:
        print("Host is down / not reachable")
        exit()
    print("Port Scan of Site : %s on Ports : %s to %s" % (ip_address, low_port, high_port))
    for p in response:
        if p.haslayer(("TCP", "FIN", "SYN", "ACK", "URG")) == False:
            port = p.dport
            print("Port %d is CLOSED" % port)
        elif p.haslayer(("TCP")) == False:
            port = p.dport + 1
            print("Port %d is filtered" % port)
        else:
          port = p.dport
          print("Port %d is OPEN" % port)

scan_ports("www.example.com", 0, 1024)

#from datetime import datetime
#print(datetime.now().strftime('[%H:%M:%S]'))
