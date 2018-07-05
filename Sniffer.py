from scapy.all import *
from datetime import datetime

# Getting all interfaces
def get_interfaces():
    """returns a list of available network interfaces"""
    interfaces = []
    for iface_name in sorted(ifaces.data.keys()):
        dev = ifaces.data[iface_name]
        i = str(dev.name).ljust(4)
        interfaces.append(i)
    return interfaces

def sniffA():
    sniff(iface='Broadcom 802.11n Network Adapter',
          prn=packet2Log,
          lfilter=lambda pkt: (IP in pkt) and (TCP in pkt))

def packet2Log(packet):
    pkt_time = str(datetime.now()).split('.')[0]
    log_line = "{} {} {} {} {}".format(pkt_time,
                                     packet[IP].src,
                                     packet[IP].dst,
                                     packet[TCP].dport,
                                     "PASS")
    print(log_line)
    # write to file (log_line)



sniffA()
