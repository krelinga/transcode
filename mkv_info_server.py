#! /usr/bin/python3


import glob
import html
import http.server
from lib import constants
import os
import textwrap


def _FindMKVInfoFiles():
    return glob.glob(
            os.path.join('/mnt/share/*',
                constants.MKV_DIRECTORY_INFO_JSON))


def _HTMLListElement(element):
    return f'<li>{html.escape(element)}</li>'


def _HTMLList(elements):
    return textwrap.dedent(f'''\
            <ul>
                {' '.join([_HTMLListElement(x) for x in elements])}
            </ul>''')


class _Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(textwrap.dedent(f'''\
                <html>
                    <head>
                        <title>MKV Info Server</title>
                    </head>
                    <body>
                        <h1>Hello World!</h1>
                        <p>request path: {html.escape(self.path)}</p>
                        <p>Info Files:{_HTMLList(_FindMKVInfoFiles())}</p>
                    </body>
                </html>'''), 'utf-8'))



def main():
    port = 8080
    httpd = http.server.ThreadingHTTPServer(
            ('', port), _Handler)
    print(f'listening on port {port}')
    httpd.serve_forever()


if __name__ == '__main__':
    main()
