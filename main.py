#!/usr/bin/env python
import threading
import wifisniffer
import btsniffer
import server.server as web
import macaddr
import Queue
import time
import push
from collections import OrderedDict

MAX_QUEUE = 1<<14
MAX_REMEMBER = 512

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

    seen = OrderedDict()

    try:
        while True:
            interface, mac, when = events.get()
            name = '"%s"'%macaddr.identify(mac)
            notes = "Occurred %s" % time.ctime(when)
            if mac in seen:
                del seen[mac]
            else:
                push.note(interface, name, mac, notes)
            if len(seen) >= MAX_REMEMBER:
                seen.popitem()
            seen[mac] = when
    finally:
        macaddr.save_cache()

if __name__ == '__main__':
    main()
