import time
import pcap
import struct

def parse(tup):
    time, data = tup



class BtPacket(object):

    @classmethod
    def is_valid(cls, tup):
        return len(tup[1]) == 15+8


    def __init__(tup):
        t, data = tup
        rssi = data[-1]
        if rssi not in {0, 4}:
            self.rssi = rssi-0x100 if rssi & 0x80 else rssi
        else:
            self.rssi = None
        self.time = t
        if len(data) == 18+8:
            rawaddr = data[8+4:8+4+6]
        else:
            

