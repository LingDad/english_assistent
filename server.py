#!/usr/bin/env python3
"""
English Assistant — local server + Kimi Code API proxy
Run:   python3 server.py
Open:  http://localhost:8080
"""
import json
import urllib.request
import urllib.error
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT         = 8080
KIMI_API_URL = 'https://api.kimi.com/coding/v1/chat/completions'


class Handler(SimpleHTTPRequestHandler):

    def log_message(self, *_):
        pass  # keep console clean

    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_POST(self):
        if self.path != '/api/proxy':
            self.send_error(404)
            return

        length = int(self.headers.get('Content-Length', 0))
        body   = self.rfile.read(length)
        auth   = self.headers.get('Authorization', '')

        req = urllib.request.Request(
            KIMI_API_URL,
            data    = body,
            headers = {'Content-Type': 'application/json', 'Authorization': auth},
            method  = 'POST',
        )

        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                self._reply(r.status, r.read())
        except urllib.error.HTTPError as e:
            self._reply(e.code, e.read())
        except Exception as e:
            self._reply(500, json.dumps({'error': {'message': str(e)}}).encode())

    def _reply(self, status, body):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self._cors()
        self.end_headers()
        self.wfile.write(body)


if __name__ == '__main__':
    srv = HTTPServer(('localhost', PORT), Handler)
    print(f'  App  →  http://localhost:{PORT}')
    print('  Press Ctrl+C to stop\n')
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print('Stopped.')
