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
        with hb.html() as root:
            root(hb.head())(hb.body())(hb.title())('MKV Info Server')
            with root(hb.body()) as body:
                body(hb.h1())('Hello World!')
                with body(hb.p()) as request_path_p:
                    request_path_p('request path:')
                    request_path_p(self.path)
                with body(hb.p()) as info_files_p:
                    info_files_p('Info Files:')
                    with info_files_p(hb.ul()) as info_files_ul:
                        for info_file in _FindMKVInfoFiles():
                            info_files_ul(hb.li())(info_file)
            self.wfile.write(bytes(root.Render(), 'utf-8'))


def main():
    port = 8080
    httpd = http.server.ThreadingHTTPServer(
            ('', port), _Handler)
    print(f'listening on port {port}')
    httpd.serve_forever()


if __name__ == '__main__':
    main()
