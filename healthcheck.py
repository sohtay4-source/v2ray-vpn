from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'OK')
    
    def log_message(self, format, *args):
        pass

PORT = int(os.environ.get('PORT', 80))
server = HTTPServer(('0.0.0.0', PORT), HealthHandler)
print(f"Healthcheck server running on port {PORT}")
server.serve_forever()
