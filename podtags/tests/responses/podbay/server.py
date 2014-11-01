#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- python -*-
# use 4 spaces to indent, NO TAB
# vim: ai ts=4 sts=4 et sw=4
"""
Basic http server to serve example html files and urls
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os

PORT_NUMBER = 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class testHTMLServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Handle GET requests
        Map specific URLs to specific HTML files
        """
        if self.path == "/browse/games-and-hobbies":
    	    self.path = "directory.html"
        elif self.path == "/show/123456789":
            self.path = "123456789.html"
        elif self.path == "/show/123456789/reviews":
            self.path = "reviews.html"

        try:
            # Serve the static file mapped to the URL 
            f = open(os.path.join(BASE_DIR, self.path))
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
            return
        except IOError:
            self.send_error(
                404,
                'File Not Found: {}'.format(self.path)
            )

try:
    server = HTTPServer(('', PORT_NUMBER), testHTMLServer)
    print(
        'Started httpserver on port {}'.format(PORT_NUMBER)
    )
    server.serve_forever()
except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
