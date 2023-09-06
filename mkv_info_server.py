#! /usr/bin/python3


import http.server
import textwrap


class _Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(textwrap.dedent('''\
                <html>
                    <head>
                        <title>MKV Info Server</title>
                    </head>
                    <body>
                        <h1>Hello World!</h1>
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
