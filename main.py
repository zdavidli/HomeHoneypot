#!/usr/bin/env python
import threading
import wifisniffer
import btsniffer
import server.server as web
import macaddr
import Queue
import time

MAX_QUEUE = 1<<14

LOGFILE = 'e.log' # lol

def main():
    events = Queue.Queue(MAX_QUEUE)
    wifithread = wifisniffer.Sniffer(args=(events,))
    wifithread.daemon = True
    btthread = btsniffer.Sniffer(args=(events,))
    btthread.daemon = True
    webthread = web.HoneyServer()
    webthread.daemon = True

    macaddr.init_cache()
    wifithread.start()
    btthread.start()
    webthread.start()

    try:
        while True:
            interface, mac, when = events.get()
            name = '"%s"'%macaddr.identify(mac)
            notes = "Occurred %s" % time.asctime(when)
            push.note(interface, name, mac, notes)
    finally:
        macaddr.save_cache()

if __name__ == '__main__':
    main()