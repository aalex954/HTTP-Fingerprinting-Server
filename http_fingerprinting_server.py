from http.server import BaseHTTPRequestHandler, HTTPServer
import http.server
import socketserver
import json
import signal
import sys
import base64

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        # perform clean up actions here
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    def log_message(self, format, *args):
        with open('access.log', 'a') as f:
            f.write("%s - - [%s] %s\n" %
                    (self.client_address[0],
                     self.log_date_time_string(),
                     format % args))

    def do_OPTIONS(self):           
        self.send_response(200, "ok")       
        self.send_header('Access-Control-Allow-Origin', '*')                
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")        
        self.end_headers()
    
    def do_GET(self):

        if self.path == '/test':
            with open('sample_site.html', 'rb') as f:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())

            self.log_message("-------------------------GET-----------------------------")
            self.log_message(f'{self.client_address[0]} - {self.requestline}')
            for header, value in self.headers.items():
                self.log_message(f'{header}: {value}')
            self.log_message(f'Referer: {self.headers.get("Referer", "")}')
            self.log_message("-------------------------END GET--------------------------")
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"404 Not Found")

    def do_POST(self):
        if self.path == '/fingerprint':
            self.log_message("-------------------------POST-----------------------------")
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Received POST request")

            post_data = base64.b64decode(post_data).decode('utf-8')
            post_data_dict = json.loads(post_data)

            for key, value in post_data_dict.items():
                self.log_message(f"{key}: {value}")

            self.log_message("-------------------------END POST--------------------------")
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"404 Not Found")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()