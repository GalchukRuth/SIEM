from scapy.all import *
from datetime import datetime

# Getting all interfaces
def getInterfaces():
    """returns a list of available network interfaces"""
    interfaces = []
    for iface_name in sorted(ifaces.data.keys()):
        dev = ifaces.data[iface_name]
        i = str(dev.name).ljust(4)
        interfaces.append(i)
    return interfaces

# Sniffing network packets
def sniffPackets(file_path):
    lst = []
    log_line = sniff(count=5,iface='Broadcom 802.11n Network Adapter',
          prn=packet2Log,
          lfilter=lambda pkt: (IP in pkt) and (TCP in pkt))
    # with open (file_path, 'a') as file:
    #     file.write(log_line)
    print 'type', type(log_line)
    return lst

def packet2Log(packet):
    pkt_time = str(datetime.now()).split('.')[0]
    log_line = "{} {} {} {} {}".format(pkt_time,
                                     packet[IP].src,
                                     packet[IP].dst,
                                     packet[TCP].dport,
                                     "PASS")
    return log_line

# Writing log_line to file
def log2File(file_path):
    log_line = sniffPackets()
    with open (file_path, 'a') as file:
        file.write(log_line)

print sniffPackets(r'C:\Users\Owner\PycharmProjects\SIEM\Sniff_Log.txt')
# log2File(r'C:\Users\Owner\PycharmProjects\SIEM\Sniff_Log.txt')
# print  getInterfaces()