import threading
import wifisniffer
import btsniffer
import Queue

MAX_QUEUE = 4096

def main():
    events = Queue.Queue(MAX_QUEUE)
    wifithread = wifisniffer.Sniffer(events)
    wifithread.daemon = True
    btthread = wifisniffer.Sniffer(events)
    btthread.daemon = True

    wifithread.start()
    btthread.start()
    while True:
        events.get()
        
