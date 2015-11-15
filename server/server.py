#!/usr/bin/env python2
 

import threading
import BaseHTTPServer
import CGIHTTPServer

class HoneyServer(threading.Thread):
    def run(self):
        import cgitb; cgitb.enable()  ## This line enables CGI error reporting

        server = BaseHTTPServer.HTTPServer
        handler = CGIHTTPServer.CGIHTTPRequestHandler
        server_address = ("", 8080)
         
        httpd = server(server_address, handler)
        httpd.serve_forever()

if __name__ == '__main__':
    H = HoneyServer()
    H.start()

