#! /usr/bin/python3


import http.server


def main():
    port = 8080
    httpd = http.server.ThreadingHTTPServer(
            ('', port), http.server.BaseHTTPRequestHandler)
    print(f'listening on port {port}')
    httpd.serve_forever()


if __name__ == '__main__':
    main()
