#!/usr/bin/env python
"""
Servidor simples em python
Pelo cmd::
    ./dummy-web-server.py [<port>]
GET:
    curl http://localhost
HEAD:
    curl -I http://localhost
POST:
    curl -d "foo=bar&bin=baz" http://localhost
"""
from http.server import BaseHTTPRequestHandler, HTTPServer

class httpserver(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>Ola!\nObrigado por visitar o site!</h1></body></html>".encode('ascii'))

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Não faz nada com o dado postado
        self._set_headers()
        self.wfile.write("<html><body><h1>Voce tentou dar um post!</h1></body></html>".encode('ascii'))
        
def run(server_class=HTTPServer, handler_class=httpserver, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Iniciando httpd...')
    print('Servidor iniciado.')
    httpd.serve_forever()

if __name__ == "__main__":
    port = input('Escolha a porta em que quer rodar o servidor: ')
    run(port=int(port))