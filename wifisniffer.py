#!/usr/bin/evn python

import threading
from scapy.all import *
import subprocess as sp
import Queue
import time

class Sniffer(threading.Thread):
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        sp.check_call(['hostapd', '/etc/hostapd/hostapd.conf'])
        # init stuff here

    def run(self, queue):
        def record(packet, ignore = set()):
            queue.put(("WiFi", packet.src, time.time()))
        sniff(prn=record)
