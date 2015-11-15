#!/usr/bin/env python2
 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8080)
# handler.cgi_directories = ["/"]
 
httpd = server(server_address, handler)
httpd.serve_forever()
