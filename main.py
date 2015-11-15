#!/usr/bin/env python
import threading
import wifisniffer
import btsniffer
import server.server as web
import macaddr
import Queue

MAX_QUEUE = 1<<14

LOGFILE = 'e.log' # lol

def main():
    events = Queue.Queue(MAX_QUEUE)
    wifithread = wifisniffer.Sniffer(events)
    wifithread.daemon = True
    btthread = btsniffer.Sniffer(events)
    btthread.daemon = True
    webthread = web.HoneyServer()
    webthread.daemon = True

    macaddr.init_cache()
    wifithread.start()
    btthread.start()
    webthread.start()

    try:
        while True:
            interface, mac = events.get()
            print macaddr.identify(mac)
    finally:
        macaddr.save_cache()

