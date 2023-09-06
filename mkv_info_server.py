#! /usr/bin/python3


import glob
import html
import http.server
from lib import constants
import lib.html_builder as hb
import os
import textwrap


def _FindMKVInfoFiles():
    return glob.glob(
            os.path.join('/mnt/share/*',
                constants.MKV_DIRECTORY_INFO_JSON))


class _Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html_tree = hb.html(
            hb.head(hb.title('MKV Info Server')),
            hb.body(
                hb.h1('Hello World!'),
                hb.p('request path:', self.path),
                hb.p(
                    'Info Files:',
                    hb.ul([hb.li(x) for x in _FindMKVInfoFiles()]),
                )
            )
        )
        self.wfile.write(bytes(html_tree.Render(), 'utf-8'))


def main():
    port = 8080
    httpd = http.server.ThreadingHTTPServer(
            ('', port), _Handler)
    print(f'listening on port {port}')
    httpd.serve_forever()


if __name__ == '__main__':
    main()
