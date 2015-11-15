import time
import pcap
import struct

import threading
import subprocess as sp
import Queue
from scapy.all import *

# def parse(tup):
#     time, data = tup

# class BtPacket(object):

#     @classmethod
#     def is_valid(cls, tup):
#         return len(tup[1]) == 15+8


#     def __init__(tup):
#         t, data = tup
#         rssi = data[-1]
#         if rssi not in {0, 4}:
#             self.rssi = rssi-0x100 if rssi & 0x80 else rssi
#         else:
#             self.rssi = None
#         self.time = t
#         if len(data) == 18+8:
#             rawaddr = data[8+4:8+4+6]
#         else:
            
class Sniffer(threading.Thread):
    def __init__(self, queue, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.__queue = queue

    def run(self):
        def record(packet, ignore = set()):
            self.__queue.put(("Bluetooth", packet.src, time.time()))
        sniff(prn=record)
