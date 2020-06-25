from http.server import HTTPServer, BaseHTTPRequestHandler
import json

data = {'result': 'this is a test'}
#host = ('localhost', 8889)
host = ('127.0.0.1', 8889)

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        print('------------'+self.requestline)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
