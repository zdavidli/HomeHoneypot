#!/usr/bin/evn python

import threading
from scapy.all import *
import subprocess as sp
import Queue

class Sniffer(threading.Thread):
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.sp.Popen(['hostapd', 'etc/hostapd/hostapd.conf'])
        # init stuff here

    def run(self, queue):
        def record(packet, ignore = set()):
            queue.put(("WiFi", packet.src))
        sniff(prn=record)
