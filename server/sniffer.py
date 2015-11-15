#!/usr/bin/evn python
from scapy.all import *
def print_summary(pkt):
    if IP in pkt:
        ip_src=pkt[IP].src
        ip_dst=pkt[IP].dst
    if TCP in pkt:
        tcp_sport=pkt[TCP].sport
        tcp_dport=pkt[TCP].dport

        print " IP src " + str(ip_src) + " TCP sport " + str(tcp_sport) 
        print " IP dst " + str(ip_dst) + " TCP dport " + str(tcp_dport)

    # you can filter with something like that
    if ( ( pkt[IP].src == "192.168.0.1") or ( pkt[IP].dst == "192.168.0.1") ):
        print("!")

sniff(filter="ip",prn=print_summary)
# or it possible to filter with filter parameter...!
sniff(filter="ip and host 192.168.0.1",prn=print_summary)
