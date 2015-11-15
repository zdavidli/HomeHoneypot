import threading
import wifisniffer
import btsniffer
import server.server as web
import macaddr
import Queue

MAX_QUEUE = 1<<14

def main():
    events = Queue.Queue(MAX_QUEUE)
    wifithread = wifisniffer.Sniffer(events)
    wifithread.daemon = True
    btthread = wifisniffer.Sniffer(events)
    btthread.daemon = True
    webthread = web.HoneyServer()
    webthread.daemon = True

    wifithread.start()
    btthread.start()
    webthread.start()
    while True:
        interface, mac = events.get()
        macaddr.

