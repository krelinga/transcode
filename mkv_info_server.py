#! /usr/bin/python3


import glob
import html
import http.server
from lib import constants, data
import lib.html_builder as hb
import os
import textwrap
import urllib


def _FindMKVInfoFiles():
    return glob.glob(
            os.path.join('/mnt/share/*',
                constants.MKV_DIRECTORY_INFO_JSON))


class _Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.render_root()
        else:
            self.render_non_root()

    def common_html_header(self):
        return hb.head(
            hb.title('MKV Info Server'),
            hb.link(hb.Attrs(
                rel='stylesheet',
                href='https://cdn.simplecss.org/simple.min.css'
            )),
            # The CSS Body is too narrow by default, make it wider.
            hb.style(textwrap.dedent('''\
                body {
                    grid-template-columns: 1fr 90% 1fr;
                }'''))
        )

    def render_root(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html_tree = hb.html(
            self.common_html_header(),
            hb.body(
                hb.h1('All Known .mkvinfo.json Files'),
                hb.p('request path:', self.path),
                hb.p(
                    'Info Files:',
                    hb.ul([hb.li(x) for x in _FindMKVInfoFiles()]),
                )
            )
        )
        self.wfile.write(bytes(html_tree.Render(), 'utf-8'))

    def render_non_root(self):
        path = urllib.parse.unquote(self.path)
        if (not os.path.isfile(path) or
            not path.endswith(constants.MKV_DIRECTORY_INFO_JSON)):
            self.render_404()
            return

        mkv_directory = None
        with open(path, 'r') as json_file:
            mkv_directory = data.MKVDirectory.FromJson(json_file)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        def render_one_track(track):
            return hb.tr(
                hb.td(track.track_id),
                hb.td(track.track_name),
                hb.td(track.track_type),
                hb.td(track.language),
                hb.td(track.audio_channels),
                hb.td(track.default_track),
                hb.td(track.forced_track),
            )

        def render_one_file(mkv_file):
            return hb.article(
                hb.h3(mkv_file.file_path),
                hb.table(
                    hb.tr(
                        hb.th("Track ID"),
                        hb.th("Track Name"),
                        hb.th("Track Type"),
                        hb.th("Language"),
                        hb.th("Audio Channels"),
                        hb.th("Default Track?"),
                        hb.th("Forced Track?"),
                    ),
                    [
                        render_one_track(x) for x in mkv_file.tracks
                    ],
                ),
            )

        html_tree = hb.html(
            self.common_html_header(),
            hb.body(
                hb.h1(path, 'exists!'),
                [
                    render_one_file(x)
                    for x in sorted(mkv_directory.files, key=lambda x: x.file_path)
                ]
            )
        )
        self.wfile.write(bytes(html_tree.Render(), 'utf-8'))

    def render_404(self):
        self.send_response(404)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(textwrap.dedent('''\
                <html>
                    <head>
                        <title>Unknown page</title>
                    </head>
                    <body>
                        <h1>404</h1>
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
