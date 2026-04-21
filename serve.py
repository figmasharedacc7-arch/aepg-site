#!/usr/bin/env python3
"""Serve the aepg-site locally. Run: python3 serve.py"""
import http.server, socketserver, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()
    def do_GET(self):
        # serve pretty URLs: /contact -> /contact.html
        if self.path != '/' and '.' not in os.path.basename(self.path.split('?')[0]):
            candidate = self.path.strip('/').split('?')[0] + '.html'
            if os.path.exists(candidate):
                self.path = '/' + candidate
        super().do_GET()

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print(f'serving on http://localhost:{PORT}/')
    httpd.serve_forever()
