from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from io import BytesIO


class HTTPRequestHandler(BaseHTTPRequestHandler):

    logs = {
        'camera_1': {
        'metadata': {
            'updated_at': 123,
            'name': 'Kitchen Camera',
            'location': 'gps_coords', 
            'update_pending': False
        },
        'logs': 
             [
        {'timestamp': 2323,
        'message' : 'sweet potatoes'}
            ]
    }}

    def invalidate_logs(self):
        for key in self.logs:
            print(key)
            self.logs[key].metadata.update_pending = True


    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()            
            f = open("index.html", "r")
            self.wfile.write(f.read().encode())

        elif self.path == '/logs':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(self.logs).encode())

        elif self.path == '/update':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.invalidate_logs()
            self.wfile.write(json.dumps({'msg': 'ok'}).encode())

        elif self.path == '/jobs':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.invalidate_logs()
            self.wfile.write(json.dumps({'msg': 'ok'}).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', 3000), HTTPRequestHandler)
httpd.serve_forever()
