from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
import time

class HTTPRequestHandler(BaseHTTPRequestHandler):

    logs = {
        'camera_1': {
            'metadata': {
                'updated_at': time.time(),
                'name': 'Conference Room',
                'update_pending': True
            },
            'logs': []
        },        
        'camera_2': {
            'metadata': {
                'updated_at': time.time(),
                'name': 'Loading Dock',
                'update_pending': True
            },
            'logs': [{
                'timestamp': time.time(),
                'message': 'Camera offline'
            }]
        }
    }


    ######################
    # Internal Functions #
    ######################

    def logs_invalidate_all(self):
        for key in self.logs:
            self.logs[key]['metadata']['update_pending'] = True

    def logs_update(self, _logs):
        self.logs[_logs['id']] = _logs['data']

    def get_job(self, _id):
        if _id in self.logs:
            if self.logs[_id]['metadata']['update_pending'] == True:
                # I know, I know, multiple returns are bad...
                return 'send_logs'  
        # ...but the code is so much cleaner this way.
        return 'none'


    ################
    # HTTP Section #
    ################

    def init_headers_json(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def init_headers_html(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        
        # Parse the request path
        parsedPath = urlparse(self.path)
        route = parsedPath.path;
        queries = parse_qs(parsedPath.query)

        # Get the frontend client
        if route == '/':
            self.init_headers_html()
            f = open("index.html", "r")
            self.wfile.write(f.read().encode())

        # Get any log data
        elif route == '/logs':
            self.init_headers_json()
            self.wfile.write(json.dumps(self.logs).encode())

        # Update all camera logs
        elif route == '/update':
            self.init_headers_json()
            self.logs_invalidate_all()
            self.wfile.write(json.dumps({'msg': 'ok'}).encode())

        # Get any jobs from the queue
        elif route == '/jobs':
            if 'id' in queries:
                job = self.get_job(queries['id'][0])
                self.init_headers_json()
                self.wfile.write(json.dumps({'msg': 'ok', 'jobs': job}).encode())
            else:
                # Bad Request
                self.send_response(400)
                self.end_headers()

        # Route DNE
        else: 
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        data = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        self.logs_update(data)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({'msg': 'ok'}).encode())


httpd = HTTPServer(('0.0.0.0', 3000), HTTPRequestHandler)
httpd.serve_forever()